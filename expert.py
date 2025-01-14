import spacy
from knowledge_base import knowledge_base
from do_action import do_action
# tokenize user input and extract keywords.
nlp = spacy.load("en_core_web_sm")

asked_symptoms = set()


###############################################################################
# Helper Functions
###############################################################################

def find_relevant_disorders(kb, matched_facts):
    """
    Purpose: Narrows down relevant disorders based on initial user-provided symptoms.
    Logic:
    Loops through rules in the knowledge base (kb).
    For each rule, checks if any matched symptom is listed as True in the "if" conditions.
    If a match is found, adds the corresponding disorder to the relevant list.
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
    Purpose: Extracts symptoms (keywords) from user input.
    Logic:
    Converts the input to lowercase and tokenizes it using spaCy.
    Checks each token's text and lemma against known fact keys from the knowledge base.
    Collects matching keywords in a set to avoid duplicates.
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
    Purpose: Calculates the proportion of symptoms that match a rule's conditions.
    Logic:
    Counts the total required symptoms and the number of matched symptoms.
    Computes the match ratio as matched_count / required_count.
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
    Purpose: Identifies disorders whose match ratio exceeds the given threshold.
    Logic:
    Loops through all rules, calculates match ratios using calculate_match_percentage.
    If a disorder meets the threshold, stores it in a dictionary with match details.
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
    Purpose: Queries the user about missing symptoms for given disorders.
    Logic:
    Finds symptoms not yet confirmed (False in facts).
    Asks the user about these symptoms and updates the facts based on their response.
    If the user denies more than half of a disorder's required symptoms, removes it from consideration.
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
    Purpose: Identifies symptoms for a specific diagnosis that remain unasked.
    Logic:
    Finds the rule corresponding to the diagnosis.
    Collects symptoms that are required (True) but still False in facts
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
    Purpose: Outputs the final diagnosis summary.
    Logic:
    Lists unasked symptoms, match percentage, and disclaimer.
    Provides a summary of the diagnostic process.
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

    follow_up_answer = input(f"\nWould you like to see additional questions about {diagnosis}? (yes/no) ")
    if follow_up_answer.lower() in ["yes", "y"]:
        post_diagnosis_followup_from_kb(kb, diagnosis)
    else:
        print("No worries. You can always run the system again if you need more info.")
        print("\nNote: This is not a formal diagnosis. Please consult a professional :)")



def post_diagnosis_followup_from_kb(kb, diagnosis):
    """
    Looks up the follow-up data for the given diagnosis from the knowledge base.
    1. Asks the user the specified questions (storing answers in a dict).
    2. Evaluates the mini-rules (in "logic") to see which actions to trigger.
    3. Calls do_action(...) for each matching rule.

    :param kb: The overall knowledge base (dict).
    :param diagnosis: The diagnosis name (string).
    """
    # Convert to lowercase to match the key in kb["follow_up"], if needed
    follow_up_data = kb.get("follow_up", {}).get(diagnosis.lower(), {})
    if not follow_up_data:
        # No follow-up info for this diagnosis
        return

    # --------------------------------------------------------------------
    # 1) Ask the follow-up questions, parse user input, store in `answers`
    # --------------------------------------------------------------------
    answers = {}
    questions = follow_up_data.get("questions", [])

    for q in questions:
        user_input = input(f"\n{q['text']} ")

        # Parse the answer based on "type" (int, bool, or default/string)
        if q["type"] == "int":
            try:
                answers[q["id"]] = int(user_input)
            except ValueError:
                # If input is invalid, default to 0 or handle differently
                answers[q["id"]] = 0  

        elif q["type"] == "bool":
            # Convert "yes"/"y"/"true" => True, everything else => False
            answers[q["id"]] = user_input.strip().lower() in ["yes", "y", "true"]

        else:
            # For anything else, store the raw string
            answers[q["id"]] = user_input.strip()

    # ---------------------------------------------
    # 2) Evaluate each mini-rule in the "logic" list
    # ---------------------------------------------
    logic_rules = follow_up_data.get("logic", [])
    
    for rule in logic_rules:
        condition_dict = rule["if"]  # e.g. {"duration": "<2", "taking_meds": False}
        all_conditions_met = True

        for answer_key, condition_value in condition_dict.items():
            user_val = answers.get(answer_key, None)

            # A) Check for numeric comparisons (e.g. "<2", ">=6")
            if (
                isinstance(condition_value, str) 
                and (condition_value.startswith("<") or
                     condition_value.startswith(">") or
                     condition_value.startswith("<=") or
                     condition_value.startswith(">="))
                and isinstance(user_val, int)
            ):
                # Identify the comparator
                comparator = condition_value[0]
                comp_val_str = condition_value[1:]
                if condition_value.startswith(">=") or condition_value.startswith("<="):
                    comparator = condition_value[:2]  # <= or >=
                    comp_val_str = condition_value[2:]

                # Convert comparison value to an integer
                try:
                    comp_val = int(comp_val_str)
                except ValueError:
                    comp_val = 0  # fallback or handle differently

                # Perform the comparison
                if comparator == "<" and not (user_val < comp_val):
                    all_conditions_met = False
                elif comparator == ">" and not (user_val > comp_val):
                    all_conditions_met = False
                elif comparator == "<=" and not (user_val <= comp_val):
                    all_conditions_met = False
                elif comparator == ">=" and not (user_val >= comp_val):
                    all_conditions_met = False

            # B) Check for boolean conditions (True/False)
            elif isinstance(condition_value, bool):
                # user_val must also be a bool, and must match exactly
                if not isinstance(user_val, bool) or (user_val != condition_value):
                    all_conditions_met = False

            else:
                # If none of the above conditions matched,
                # we consider the rule not met.
                all_conditions_met = False

            if not all_conditions_met:
                break  # No need to check further conditions in this rule

        # If all conditions are met, fire the rule's action
        if all_conditions_met:
            action_key = rule["then"]
            do_action(action_key, answers)

###############################################################################
# 2. Main Expert System Flow
###############################################################################

def run_expert_system(kb):

    '''
    User Input and Initial Fact Matching
    Prompts the user to describe how they feel.
    Extracts symptoms from the input using extract_keywords.
    Marks matched symptoms as True in the facts dictionary.
    b) Identify Relevant Disorders
    Finds disorders explicitly referencing the matched symptoms using find_relevant_disorders.
    If no specific disorders match, switches to a broader check of all disorders.
    c) Ask Missing Questions
    Uses gather_missing_symptoms_for_disorders to query the user about required symptoms for relevant or all disorders.
    d) Evaluate Disorders with Threshold
    Evaluates disorders based on the match ratio using check_disorders_with_threshold.
    Disorders with a match ratio ≥ 60% are considered potential diagnoses.
    e) Finalize or Narrow Down Diagnoses
    If one disorder meets the threshold:
    Asks the user whether to finalize the diagnosis or query more symptoms.
    If multiple disorders remain:
    Offers the user an option to further narrow them down.
    If no disorders meet the threshold, informs the user that more data may be needed.
    f) End of System
    Finalizes the diagnosis if only one disorder remains and the user chooses to confirm it.
    Otherwise, lists the potential disorders and their match details.
    '''
    facts = kb["facts"]

    print("Hello! Please describe how you feel.")
    user_input = input("> ")

    # NEW CHECK: If user mentions 'suicide' or 'suicidal'
    if any(word in user_input.lower() for word in ["suicide", "suicidal"]):
        print("\nIf you're having suicidal thoughts, please reach out to a crisis helpline immediately.\n"
              "In the UK, dial 111 or visit https://111.nhs.uk/guided-entry/mental-health-help to find one in your region.")
        print("\n(Ending the system here for safety.)")
        return  # Stop the expert system

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