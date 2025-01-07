import spacy
from knowledge_base import knowledge_base

nlp = spacy.load("en_core_web_sm")
asked_symptoms = set()


###############################################################################
# Helper Functions
###############################################################################

def find_relevant_disorders(kb, matched_facts):
    """
    The find_relevant_disorders function scans all rules in the knowledge base and checks whether any of the user’s 
    initially matched facts (symptoms) appear as required (set to True) in a rule’s “if” conditions. 
    If it finds at least one matching fact in a rule, it adds that rule’s “then” diagnosis to a set of relevant disorders. 
    In this way, the method narrows the focus to only those disorders that explicitly require the symptoms the user has already mentioned, 
    rather than considering every possible disorder at once.
    """
    relevant = set()
    for rule in kb["rules"]:
        diagnosis = rule["then"]
        conditions = rule["if"]
        for fact in matched_facts:
            if fact in conditions and conditions[fact]:
                relevant.add(diagnosis)
                break
    return list(relevant)

def extract_keywords(user_input, fact_keys):
    '''
    The user’s input is first converted to lowercase, then tokenized by spaCy into individual tokens. 
    Each token is checked against the list of known fact keys in two ways—first by its exact text (e.g., “sad”), 
    and if not found, by its lemma (e.g., the base form “feel” for “feeling”). 
    Any matches are stored in a set to avoid duplicates, and the function finally returns those matched symptoms as a list. 
    This ensures that variations in word forms (like “feels” vs. “feel”) can still be recognized, provided the lemma matches a known key in your knowledge base.
    '''
    text = user_input.lower()
    doc = nlp(text)
    matched = set()
    for token in doc:
        if token.text in fact_keys:
            matched.add(token.text)
        elif token.lemma_ in fact_keys:
            matched.add(token.lemma_)
    return list(matched)

def calculate_match_percentage(rule_conditions, facts):
    '''
    This function calculates how many of a rule’s required symptoms match the current facts. 
    It loops through each required symptom, increments a counter if that symptom is satisfied in facts, 
    and then computes the ratio by dividing the matched count by the total number of required symptoms. 
    If there are no required symptoms, it returns zero for the ratio. Finally, it returns the ratio, the matched count, and the total required count.
    '''
    required_count = len(rule_conditions)
    matched_count = 0
    for fact_key, required_value in rule_conditions.items():
        if facts.get(fact_key, False) == required_value:
            matched_count += 1
    ratio = matched_count / required_count if required_count else 0
    return (ratio, matched_count, required_count)

def check_disorders_with_threshold(kb, threshold=0.6):
    '''
    This function checks each rule in the knowledge base to see if its required symptoms meet or exceed a specified match ratio. 
    For every rule, it calculates how many required symptoms are currently satisfied, then compares that ratio to the threshold. 
    If it’s high enough, the rule’s diagnosis is recorded in the potential dictionary along with its ratio, matched symptom count, and total required.
    '''
    potential = {}
    facts = kb["facts"]
    for rule in kb["rules"]:
        conditions = rule["if"]
        diagnosis = rule["then"]
        ratio, matched, req = calculate_match_percentage(conditions, facts)
        if ratio >= threshold:
            potential[diagnosis] = (ratio, matched, req)
    return potential

def gather_missing_symptoms_for_disorders(kb, disorders, asked_symptoms):
    '''
    This function asks the user about any required symptoms that remain unknown for the given disorders. 
    It skips questions already asked (using asked_symptoms), updates the user’s yes/no responses in facts, and counts how many times the user denies required symptoms. 
    If the user says “no” to more than half of a disorder’s required symptoms, that disorder is removed from consideration.
    '''
    facts = kb["facts"]
    to_remove = set()

    for rule in kb["rules"]:
        diag = rule["then"]
        if diag in disorders:
            conditions = rule["if"]
            required_count = sum(1 for val in conditions.values() if val)
            missing = [f_key for f_key, needed in conditions.items()
                       if needed and not facts[f_key]]

            no_count = 0
            for symptom in missing:
                if symptom in asked_symptoms:
                    continue

                answer = input(f"\nDo you experience '{symptom}'? (yes/no) ")
                asked_symptoms.add(symptom)  # mark it asked

                if answer.lower() in ["yes", "y"]:
                    facts[symptom] = True
                else:
                    facts[symptom] = False
                    no_count += 1

                if no_count > (required_count / 2):
                    to_remove.add(diag)
                    print(f"Removing {diag} because you denied more than half its symptoms.")
                    break
    for d in to_remove:
        disorders.remove(d)

def summarize_unasked_symptoms(kb, diagnosis):
    '''
    This function looks up the rule for the specified diagnosis, then collects any symptoms required by that rule but still marked False in the knowledge base. 
    It returns a list of those “unasked” or unconfirmed symptoms so the system knows which questions remain.
    '''
    facts = kb["facts"]
    unasked = []
    for rule in kb["rules"]:
        if rule["then"] == diagnosis:
            for f_key, val in rule["if"].items():
                if val and not facts[f_key]:
                    unasked.append(f_key)
            break
    return unasked

def finalize_diagnosis(kb, diagnosis, ratio, matched_count, required_count):
    '''
    This function announces the final diagnosis by printing a summary of which required symptoms were met and showing any remaining symptoms that were never asked about. 
    It then displays the match ratio, indicating how many symptoms were satisfied out of the total required, 
    and concludes with a disclaimer that it’s not a formal medical diagnosis.
    '''
    not_asked = summarize_unasked_symptoms(kb, diagnosis)
    if not_asked:
        print(f"\nWe haven't asked about all possible symptoms, "
              f"but we have enough information to suspect '{diagnosis}'.")
        print("You may also be experiencing these unconfirmed symptoms:")
        for s in not_asked:
            print(f" - {s}")

    print(f"\nConclusion: It's most likely '{diagnosis}' based on current data.")
    print(f"You matched {matched_count} out of {required_count} required symptoms "
          f"({ratio*100:.0f}%).")
    print("Note: This is not a formal diagnosis. Please consult a professional.")

###############################################################################
# 2. Main Expert System Flow
###############################################################################

def run_expert_system(kb):

    '''
    This function run_expert_system starts by asking the user about their current feelings, extracts any matching symptoms using extract_keywords, 
    and focuses on disorders whose rules directly reference those symptoms. If none match, it broadens to consider all disorders. After asking relevant questions, 
    it checks which disorders meet at least 60% of their required symptoms, and either narrows them down further or finalizes a diagnosis. 
    If exactly one disorder remains above the threshold, the user can finalize it or explore more questions. 
    If multiple remain, the user can attempt to differentiate them or stop early, and if none remain above 60%, the system concludes that more data may be needed.
    '''
    facts = kb["facts"]

    print("Hello! Please describe how you feel.")
    user_input = input("> ")

    # Extract initial facts
    matched = extract_keywords(user_input, list(facts.keys()))
    for m in matched:
        facts[m] = True

    # Find disorders that mention any of these matched facts
    relevant_disorders = find_relevant_disorders(kb, matched)

    if relevant_disorders:
        print(f"Based on your initial symptom(s) {matched}, "
              f"we'll focus first on: {relevant_disorders}")
        gather_missing_symptoms_for_disorders(kb, relevant_disorders, asked_symptoms)
    else:
        print("\nYour initial symptom(s) don't match any specific disorder's rule directly, "
              "so we'll do a broader check.")
        all_disorders = [r["then"] for r in kb["rules"]]
        gather_missing_symptoms_for_disorders(kb, all_disorders, asked_symptoms)

    # Now check partial matches
    potential = check_disorders_with_threshold(kb, 0.6)

    if not potential:
        print("\nNo disorder is currently >= 60% after this first pass.")
    else:
        print(f"\nCurrently, these disorders are >= 60%: {list(potential.keys())}")

    # Proceed with your usual loop logic
    while True:
        if len(potential) == 1:
            diag = list(potential.keys())[0]
            ratio, matched_s, req_s = potential[diag]
            if ratio >= 0.6:
                ans = input(f"\nWe have '{diag}' at {ratio*100:.0f}% match. "
                            "Finalize or ask more? (finalize/more) ")
                if ans.lower() == "finalize":
                    finalize_diagnosis(kb, diag, ratio, matched_s, req_s)
                    break
                else:
                    gather_missing_symptoms_for_disorders(kb, [diag], asked_symptoms)
                    potential = check_disorders_with_threshold(kb, 0.6)
            else:
                gather_missing_symptoms_for_disorders(kb, [diag], asked_symptoms)
                potential = check_disorders_with_threshold(kb, 0.6)

        elif len(potential) > 1:
            print(f"\nMultiple possible: {', '.join(potential.keys())}")
            ans = input("Try to narrow down further? (yes/no) ")
            if ans.lower() not in ["yes", "y"]:
                for p in potential:
                    r, m, c = potential[p]
                    print(f"- {p}: {m}/{c} = {r*100:.0f}%")
                break
            else:
                gather_missing_symptoms_for_disorders(kb, list(potential.keys()), asked_symptoms)
                potential = check_disorders_with_threshold(kb, 0.6)

        else:
            print("\nNo disorder is >= 60% now. Possibly more info is needed.")
            break


run_expert_system(knowledge_base)