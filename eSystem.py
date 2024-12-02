import tkinter as tk
from tkinter import messagebox

# Define the knowledge base
knowledge_base = {
    "facts": {
        "feeling_sad": False,
        "lack_of_interest": False,
        "trouble_sleeping": False,
        "feeling_nervous": False,
        "excessive_worrying": False,
        "trouble_concentrating": False,
        "feeling_overwhelmed": False,
        "uncontrollable_worry": False,
        "restlessness": False,
        "muscle_tension": False,
        "flashbacks": False,
        "nightmares": False,
        "obsessions": False,
        "compulsions": False,
        "racing_heartbeat": False,
        "sweating": False,
        "chest_pain": False,
        "hallucinations": False,
        "delusions": False,
        "impulsivity": False,
        "idealization_devaluation": False,
    },
    "rules": [
        {"if": {"feeling_sad": True, "lack_of_interest": True, "trouble_sleeping": True}, "then": "depression", "explanation": "Feeling sad, lack of interest, and trouble sleeping are common symptoms of depression."},
        {"if": {"uncontrollable_worry": True, "restlessness": True, "muscle_tension": True}, "then": "general_anxiety_disorder", "explanation": "Uncontrollable worry, restlessness, and muscle tension are key indicators of General Anxiety Disorder."},
        {"if": {"flashbacks": True, "nightmares": True}, "then": "post_traumatic_stress_disorder", "explanation": "Flashbacks and nightmares are significant symptoms of PTSD."},
        {"if": {"obsessions": True, "compulsions": True}, "then": "obsessive_compulsive_disorder", "explanation": "Obsessions and compulsions are characteristic of Obsessive-Compulsive Disorder."},
        {"if": {"racing_heartbeat": True, "sweating": True, "chest_pain": True}, "then": "panic_disorder", "explanation": "Racing heartbeat, sweating, and chest pain can point to Panic Disorder."},
        {"if": {"hallucinations": True, "delusions": True}, "then": "schizophrenia", "explanation": "Hallucinations and delusions are common symptoms of Schizophrenia."},
        {"if": {"feeling_sad": True, "lack_of_interest": True, "trouble_sleeping": True}, "then": "bipolar_depression", "explanation": "Depression with these symptoms could also indicate Bipolar Depression."},
        {"if": {"elevated_mood": True, "increased_activity": True, "impulsivity": True}, "then": "bipolar_mania", "explanation": "Elevated mood, increased activity, and impulsivity are indicators of Bipolar Mania."},
        {"if": {"intense_emotions": True, "impulsivity": True, "idealization_devaluation": True}, "then": "borderline_personality_disorder", "explanation": "Intense emotions and impulsivity with idealization/devaluation are typical of Borderline Personality Disorder."},
    ]
}

# Inference engine with Forward Chaining and explanation
def inference_engine(knowledge_base):
    facts = knowledge_base["facts"]
    rules = knowledge_base["rules"]
    conclusions = []
    explanation = []

    # Forward Chaining: Apply all rules and check facts
    for rule in rules:
        if all(facts.get(condition, False) == value for condition, value in rule["if"].items()):
            conclusions.append(rule["then"])
            explanation.append(rule["explanation"])

    return conclusions, explanation

# Expert System Application class with chaining option
class ExpertSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Health Diagnosis Expert System")
        
        # Define the questions and corresponding knowledge base keys
        self.questions = [
            ("Do you often feel sad or down?", "feeling_sad"),
            ("Do you lose interest in things you used to enjoy?", "lack_of_interest"),
            ("Do you have trouble sleeping or sleep too much?", "trouble_sleeping"),
            ("Do you feel nervous or on edge?", "feeling_nervous"),
            ("Do you worry excessively about different things?", "excessive_worrying"),
            ("Do you find it hard to concentrate?", "trouble_concentrating"),
            ("Do you feel overwhelmed by daily tasks?", "feeling_overwhelmed"),
            ("Do you experience uncontrollable worrying?", "uncontrollable_worry"),
            ("Do you feel restless or on edge?", "restlessness"),
            ("Do you have muscle tension?", "muscle_tension"),
            ("Do you experience flashbacks or nightmares?", "flashbacks"),
            ("Do you experience unwanted thoughts or compulsive actions?", "obsessions"),
            ("Do you have a racing heartbeat, sweating, or chest pain?", "racing_heartbeat"),
            ("Do you experience hallucinations or delusions?", "hallucinations"),
            ("Do you have impulsive behaviors or thoughts?", "impulsivity"),
            ("Do you experience mood swings, especially in relationships?", "idealization_devaluation"),
        ]
        self.current_question_index = 0
        self.answers = {}

        # Create UI elements
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), width=80, height=2)
        self.question_label.pack(pady=20)
        
        self.answer_var = tk.IntVar(value=0)
        self.yes_button = tk.Radiobutton(self.root, text="Yes", variable=self.answer_var, value=1, font=("Arial", 12))
        self.no_button = tk.Radiobutton(self.root, text="No", variable=self.answer_var, value=0, font=("Arial", 12))
        self.yes_button.pack()
        self.no_button.pack()

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=10)
        
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset, font=("Arial", 12))
        self.reset_button.pack(pady=10)

        # Display the first question
        self.display_question()

    def display_question(self):
        question, _ = self.questions[self.current_question_index]
        self.question_label.config(text=question)

    def next_question(self):
        # Save the current answer to the facts in the knowledge base
        _, key = self.questions[self.current_question_index]
        knowledge_base["facts"][key] = bool(self.answer_var.get())
        
        # Move to the next question
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            # End of questions; perform inference
            self.show_results()

    def show_results(self):
        # Perform forward chaining and get diagnosis and explanation
        conclusions, explanation = inference_engine(knowledge_base)

        if conclusions:
            result_text = "Possible mental health conditions:\n" + "\n".join(f"- {c}" for c in conclusions)
            result_text += "\n\nExplanation for the diagnosis:\n" + "\n".join(f"{ex}" for ex in explanation)
            messagebox.showinfo("Diagnosis", result_text)
        else:
            messagebox.showinfo("Diagnosis", "No mental health condition could be diagnosed based on the current symptoms.")
        self.root.quit()

    def reset(self):
        # Reset the application state for a new diagnosis session
        knowledge_base["facts"] = {key: False for key in knowledge_base["facts"]}
        self.current_question_index = 0
        self.answer_var.set(0)
        self.display_question()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystemApp(root)
    root.mainloop()