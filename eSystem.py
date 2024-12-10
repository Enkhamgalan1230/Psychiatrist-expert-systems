import tkinter as tk
from tkinter import messagebox

# Define the knowledge base
knowledge_base = {
    "facts": {
            #Depression
        "sad": False,
        "low": False,
        "hopeless": False,
        "helpless": False,
        "tearful": False,
        "lack of interest": False,
        "anxious": False,
        "fatigue": False,
        "difficulties in life": False,
        "trouble sleeping": False,

            #General anxiety
        "anxious": False,
        "feeling nervous": False,
        "worrying": False,
        "irritated": False,
        #trouble sleeping
        #fatigue
        "trouble concentrating": False,
        "feeling overwhelmed": False,
        "uncontrollable worry": False,

            #PTSD
        "flashbacks": False,
        "nightmares": False,
        #irritated
        "guilty": False,
        #trouble concentrating
        #trouble sleeping

            #OCD
        "obsessions": False,
        "fear harming others": False,
        "fear accidental harm": False,
        "fear contamination": False,
        "need symmetry order": False,
        "disturbing thoughts": False,
        #anxious
        "compulsive cleaning": False,
        "compulsive checking": False,
        "compulsive counting": False,
        "arranging items": False,
        "seeking reassurance": False,
        "repetitive actions": False,
        "avoidance behavior": False,
        
            #Panic disorder
        #anxious
        #worrying
        "panicing": False,
        "panic attack": False,
        "sweating": False,
        "racing heartbeat": False,
        "chills": False,
        "nausea": False,
        "shaky limbs": False,
        "dizziness": False,
        "shortness of breath": False,
        "pins and needles": False,
        "lasts up to 20 minutes": False,
        
            #Schizophrenia
        "hallucinations": False,
        "delusions": False,
        "paranoia": False,
        "hearing voices": False,
        "seeing things": False,
        "smelling things": False,
        #trouble concentrating
        "feeling controlled": False,
        "avoiding people": False,
        "lack of self care": False,
        
            #Bipolar disorder
        "mood_swings": False,
        "sudden mood change": False,
        #sad
        #low
        #trouble concentrating
        #lack of interest
        "increased energy": False,
        "easily annoyed": False,
        "excessive spending": False,
        "decreased need for sleep or food": False,
        #delusions
        #hallucinations
        #irritated

            #Eating disorder
        "body dysmorphia": False,
        "worrying about body": False,
        "worrying about weight": False,
        #avoiding people
        "eating less": False,
        "restricting food": False,
        #anxious
        "exercising excessively": False,
        #dizziness
        "numbness in arms and legs": False,
        "digestive issue, diarhhea": False,
        "higher weight": False,
        "lower weight": False,
        "delayed period": False,

            #ADHD
        #mood swings
        "carelessness": False,
        "difficulty finishing tasks": False,
        "poor organizational skills": False,
        "difficulty focusing": False,
        "losing items": False,
        "forgetfulness": False,
        "restlessness": False,
        "difficulty staying quiet": False,
        "speaking out of turn": False,
        "interrupting others": False,
        "quick temper": False,
        "inability to handle stress": False,
        "impatience": False,
        "taking risks": False,
            #Paranoia
        #delusions
        #hallucinations
        #feeling controlled
        #perceived threats
        "easily offended": False,
        "defensive": False,
        "aggresion": False,
        "inability to compromise": False,
        "struggling with criticism": False,

            #Psychosis
        #hallicinations
        #seeing things
        "feeling false touches": False,
        #hearing voices
        #delusions
        "rapid or constant speech": False,
        "switching topics mid sentence": False,
        "perscecutory delusions": False,
        "grandiose delusions": False,

            #Borderline personality disorder
        "emotional instability": False,
        "intense negative emotions": False,
        "rage": False,
        "sorrow": False,
        #mood swings
        "cognitive distortions": False,
        "perceptual distortions": False,
        "impulsive actions": False,
        "reckless behavior": False,
        "fear of abandonment": False,
        "idealization devaluation": False

    },
    "rules": [
        {
            "if": {
                "sad": True,
                "low": True,
                "hopeless": True,
                "helpless": True,
                "tearful": True,
                "lack of interest": True,
                "anxious": True,
                "fatigue": True,
                "difficulties in life": True,
                "trouble sleeping": True,
            },
            "then": "depression"
        },
        {
            "if": {
                "anxious": True,
                "feeling_nervous": True,
                "worrying": True,
                "irritated": True,
                "trouble concentrating": True,
                "feeling overwhelmed": True,
                "uncontrollable worry": True,
                "trouble sleeping": True,
                "fatigue": True
            },
            "then": "general anxiety"
        },
        {
            "if": {
                "flashbacks": True,
                "nightmares": True,
                "irritated": True,
                "guilty": True,
                "trouble concentrating": True,
                "trouble sleeping": True
            },
            "then": "ptsd"
        },
        # Rule for OCD
        {
            "if": {
                "obsessions": True,
                "fear harming_others": True,
                "fear accidental_harm": True,
                "fear contamination": True,
                "need symmetry_order": True,
                "disturbing thoughts": True,
                "compulsive cleaning": True,
                "compulsive checking": True,
                "compulsive counting": True,
                "arranging items": True,
                "seeking reassurance": True,
                "repetitive actions": True,
                "avoidance behavior": True,
                "anxious": True
            },
            "then": "ocd"
        },
        {
            "if": {
                "anxious": True,
                "worrying": True,
                "panicing": True,
                "panic attack": True,
                "sweating": True,
                "racing heartbeat": True,
                "chills": True,
                "nausea": True,
                "shaky_limbs": True,
                "dizziness": True,
                "shortness of breath": True,
                "pins and needles": True,
                "lasts up to 20 minutes": True
            },
            "then": "panic disorder"
        },
            # Rule for Schizophrenia
        {
            "if": {
                "hallucinations": True,
                "delusions": True,
                "paranoia": True,
                "hearing voices": True,
                "seeing things": True,
                "smelling things": True,
                "trouble concentrating": True,
                "feeling controlled": True,
                "avoiding people": True,
                "lack of self care": True
            },
            "then": "schizophrenia"
        },
        {
            "if": {
                "mood swings": True,
                "sudden mood change": True,
                "sad": True,
                "low": True,
                "trouble concentrating": True,
                "lack of interest": True,
                "increased energy": True,
                "easily annoyed": True,
                "excessive spending": True,
                "decreased need for sleep or food": True,
                "delusions": True,
                "hallucinations": True,
                "irritated": True
            },
            "then": "bipolar disorder"
        },
        {
            "if": {
                "body dysmorphia": True,
                "worrying about body": True,
                "worrying about weight": True,
                "avoiding people": True,
                "eating less": True,
                "restricting food": True,
                "anxious": True,
                "exercising excessively": True,
                "dizziness": True,
                "numbness in arms and legs": True,
                "digestive issue diarhhea": True,
                "higher weight": True,
                "lower weight": True,
                "delayed period": True
            },
            "then": "eating disorder"
        },
        {
            "if": {
                "mood swings": True,
                "carelessness": True,
                "difficulty finishing tasks": True,
                "poor_organizational skills": True,
                "difficulty focusing": True,
                "losing_items": True,
                "forgetfulness": True,
                "restlessness": True,
                "difficulty staying quiet": True,
                "speaking out of turn": True,
                "interrupting others": True,
                "quick temper": True,
                "inability to handle stress": True,
                "impatience": True,
                "taking risks": True
            },
            "then": "adhd"
        },
        {
            "if": {
                "emotional_instability": True,
                "intense_negative_emotions": True,
                "rage": True,
                "sorrow": True,
                "mood_swings": True,
                "cognitive_distortions": True,
                "perceptual_distortions": True,
                "impulsive_actions": True,
                "reckless_behavior": True,
                "fear_of_abandonment": True,
                "idealization_devaluation": True
            },
            "then": "borderline_personality_disorder"
        },
        {
            "if": {
                "delusions": True,
                "hallucinations": True,
                "feeling_controlled": True,
                "perceived_threats": True,
                "easily_offended": True,
                "defensive": True,
                "aggresion": True,
                "inability_to_compromise": True,
                "struggling_with_criticism": True
            },
            "then": "paranoia"
        },
        {
            "if": {
                "hallucinations": True,
                "seeing_things": True,
                "feeling_false_touches": True,
                "hearing_voices": True,
                "delusions": True,
                "rapid_or_constant_speech": True,
                "switching_topics_mid_sentence": True,
                "perscecutory_delusions": True,
                "grandiose_delusions": True
            },
            "then": "psychosis"
        }
    ]
}

