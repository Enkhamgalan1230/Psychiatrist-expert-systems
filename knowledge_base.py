# knowledge base.py

knowledge_base = {
    "facts": {
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
        "feeling nervous": False,
        "worrying": False,
        "irritated": False,
        "trouble concentrating": False,
        "feeling overwhelmed": False,
        "uncontrollable worry": False,
        "flashbacks": False,
        "nightmares": False,
        "guilty": False,
        "obsessions": False,
        "fear harming others": False,
        "fear accidental harm": False,
        "fear contamination": False,
        "need symmetry order": False,
        "disturbing thoughts": False,
        "compulsive cleaning": False,
        "compulsive checking": False,
        "compulsive counting": False,
        "arranging items": False,
        "seeking reassurance": False,
        "repetitive actions": False,
        "avoidance behavior": False,
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
        "hallucinations": False,
        "delusions": False,
        "paranoia": False,
        "hearing voices": False,
        "seeing things": False,
        "smelling things": False,
        "feeling controlled": False,
        "avoiding people": False,
        "lack of self care": False,
        "mood swings": False,
        "sudden mood change": False,
        "increased energy": False,
        "easily annoyed": False,
        "excessive spending": False,
        "decreased need for sleep or food": False,
        "body dysmorphia": False,
        "worrying about body": False,
        "worrying about weight": False,
        "eating less": False,
        "restricting food": False,
        "exercising excessively": False,
        "numbness in arms and legs": False,
        "digestive issue diarhhea": False,
        "diarhhea": False,
        "higher weight": False,
        "lower weight": False,
        "delayed period": False,
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
        "easily offended": False,
        "defensive": False,
        "aggression": False,
        "inability to compromise": False,
        "struggling with criticism": False,
        "feeling false touches": False,
        "rapid or constantspeech": False,
        "switching topics mid sentence": False,
        "persecutory delusions": False,
        "grandiose delusions": False,
        "emotional instability": False,
        "intense negative emotions": False,
        "rage": False,
        "sorrow": False,
        "cognitive distortions": False,
        "perceptual distortions": False,
        "impulsive actions": False,
        "reckless behavior": False,
        "fear of abandonment": False,
        "idealization devaluation": False,
        "perceived threats": False,
        "delusion": False
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
                "trouble sleeping": True
            },
            "then": "depression"
        },
        {
            "if": {
                "anxious": True,
                "feeling nervous": True,
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
        {
            "if": {
                "obsessions": True,
                "fear harming others": True,
                "fear accidental harm": True,
                "fear contamination": True,
                "need symmetry order": True,
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
                "shaky limbs": True,
                "dizziness": True,
                "shortness of breath": True,
                "pins and needles": True,
                "lasts up to 20 minutes": True
            },
            "then": "panic disorder"
        },
        {
            "if": {
                "hallucinations": True,
                "delusions": True,
                "delusion": True,
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
                "diarhhea": True,
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
                "poor organizational skills": True,
                "difficulty focusing": True,
                "losing items": True,
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
                "emotional instability": True,
                "intense negative emotions": True,
                "rage": True,
                "sorrow": True,
                "mood swings": True,
                "cognitive distortions": True,
                "perceptual distortions": True,
                "impulsive actions": True,
                "reckless behavior": True,
                "fear of abandonment": True,
                "idealization devaluation": True
            },
            "then": "borderline personality disorder"
        },
        {
            "if": {
                "emotional instability": True,
                "delusions": True,
                "hallucinations": True,
                "feeling controlled": True,
                "perceived threats": True,
                "easily offended": True,
                "defensive": True,
                "aggression": True,
                "inability to compromise": True,
                "struggling with criticism": True
            },
            "then": "paranoia"
        },
        {
            "if": {
                "hallucinations": True,
                "seeing things": True,
                "feeling false touches": True,
                "hearing voices": True,
                "delusions": True,
                "rapid or constant speech": True,
                "switching topics mid sentence": True,
                "persecutory delusions": True,
                "grandiose delusions": True
            },
            "then": "psychosis"
        }
    ],

    "follow_up": {
        "depression": {
            "questions": [
                {
                    "id": "duration",
                    "text": "How many weeks have you been experiencing these symptoms of depression? (0-99)",
                    "type": "int",  
                    "threshold": 2,
                },
                {
                    "id": "taking_meds",
                    "text": "Are you currently taking any medication for this? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "suicidal_thoughts",
                    "text": "Have you ever had thoughts of harming yourself or ending your life? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    "if": {
                        "duration": "<2"
                    },
                    "then": "ADVISE_LIFESTYLE"
                },
                {
                    "if": {
                        "duration": ">=2"
                    },
                    "then": "ASK_MEDICATION"
                },
                {
                    "if": {
                        "taking_meds": True
                    },
                    "then": "MEDICATION_OK"
                },
                {
                    "if": {
                        "taking_meds": False
                    },
                    "then": "ADVISE_PROFESSIONAL"
                },
                {
                    "if": {
                        "suicidal_thoughts": True
                    },
                    "then": "SHOW_HELPLINE"
                }
            ]
        },
        "general anxiety": {
            "questions": [
                {
                    "id": "duration",
                    "text": "For how many months have you been experiencing these anxiety symptoms? (0-99)",
                    "type": "int",
                    "threshold": 6 
                },
                {
                    "id": "taking_meds",
                    "text": "Are you currently taking medication for anxiety? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "therapy",
                    "text": "Have you tried therapy or counseling? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    "if": {
                        "duration": "<6"
                    },
                    "then": "ADVISE_SHORT_TERM_STRATEGIES"
                },
                {
                    "if": {
                        "duration": ">=6"
                    },
                    "then": "ADVISE_LONG_TERM_STRATEGIES"
                },
                {
                    "if": {
                        "taking_meds": True
                    },
                    "then": "MEDICATION_ADVICE"
                },
                {
                    "if": {
                        "therapy": False
                    },
                    "then": "THERAPY_RECOMMENDATION"
                }
            ]
        },
        "ptsd": {
            "questions": [
                {
                    "id": "trauma_duration",
                    "text": "How many months has it been since the traumatic event(s)? (0-99)",
                    "type": "int",
                    "threshold": 1  # e.g., PTSD typically considered if >= 1 month
                },
                {
                    "id": "avoidance_behavior",
                    "text": "Do you actively avoid reminders of the trauma? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "therapy",
                    "text": "Have you tried therapy or counseling for your PTSD symptoms? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "nightmares_flashbacks",
                    "text": "Are you still experiencing frequent nightmares or flashbacks? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    "if": {
                        # If the trauma duration is under 1 month, 
                        # it might be considered Acute Stress Disorder rather than PTSD.
                        "trauma_duration": "<1"
                    },
                    "then": "ACUTE_STRESS_ADVICE"
                },
                {
                    "if": {
                        # If the trauma duration is 1 month or more,
                        # it suggests persistent or diagnosable PTSD.
                        "trauma_duration": ">=1"
                    },
                    "then": "PTSD_PERSISTENT"
                },
                {
                    "if": {
                        "nightmares_flashbacks": True
                    },
                    "then": "PTSD_INTENSE"
                },
                {
                    "if": {
                        "avoidance_behavior": True
                    },
                    "then": "PTSD_AVOIDANCE"
                },
                {
                    "if": {
                        "therapy": False
                    },
                    "then": "RECOMMEND_TRAUMA_FOCUSED_THERAPY"
                }
            ]
        },
        "ocd": {
            "questions": [
                {
                    "id": "ocd_duration",
                    "text": "How many months have you been experiencing these obsessive or compulsive symptoms? (0-99)",
                    "type": "int",
                    "threshold": 1  # for instance, 1 month is a typical benchmark to consider clinical significance
                },
                {
                    "id": "daily_hours",
                    "text": "Do these obsessions or compulsions take up more than 1 hour a day? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "daily_life_interference",
                    "text": "Do these symptoms significantly interfere with your daily activities or responsibilities? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "therapy_used",
                    "text": "Have you tried any therapy or counseling specifically for OCD? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "medication_used",
                    "text": "Have you been prescribed or are you currently taking any medication for OCD? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    # If the duration is under 1 month, it might still be emerging.
                    "if": {
                        "ocd_duration": "<1"
                    },
                    "then": "OCD_EMERGING_ADVICE"
                },
                {
                    # If the duration is 1 month or more, it suggests a persistent pattern.
                    "if": {
                        "ocd_duration": ">=1"
                    },
                    "then": "OCD_PERSISTENT_ADVICE"
                },
                {
                    # If obsessions/compulsions consume more than 1 hour/day, highlight severity.
                    "if": {
                        "daily_hours": True
                    },
                    "then": "OCD_HOURS_ADVICE"
                },
                {
                    # If it significantly interferes with daily life, emphasize professional intervention.
                    "if": {
                        "daily_life_interference": True
                    },
                    "then": "OCD_INTERFERENCE_ADVICE"
                },
                {
                    # If no therapy has been tried, recommend exploring therapy options.
                    "if": {
                        "therapy_used": False
                    },
                    "then": "OCD_THERAPY_RECOMMENDATION"
                },
                {
                    # If on medication, suggest follow-up with a doctor for medication management.
                    "if": {
                        "medication_used": True
                    },
                    "then": "OCD_MEDICATION_FOLLOWUP"
                }
            ]
        },
        "panic disorder": {
            "questions": [
                {
                    "id": "frequency_of_attacks",
                    "text": "How many panic attacks do you typically experience in a week? (0-10+)",
                    "type": "int",
                    "threshold": 1  # We'll interpret threshold in the logic below
                },
                {
                    "id": "avoidance_of_situations",
                    "text": "Do you avoid certain places or situations for fear of having a panic attack? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "concern_of_next_attack",
                    "text": "Are you constantly worried about having another panic attack or its consequences? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "substance_use",
                    "text": "Have you ever used alcohol or medication to cope with or prevent panic attacks? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "day_to_day_impact",
                    "text": "Do these panic attacks significantly impact your daily life or routines? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    "if": {
                        # If they have at least 1 attack per week
                        "frequency_of_attacks": ">=1"
                    },
                    "then": "PANIC_ATTACKS_FREQUENT"
                },
                {
                    "if": {
                        "avoidance_of_situations": True
                    },
                    "then": "PANIC_AVOIDANCE_ADVICE"
                },
                {
                    "if": {
                        "concern_of_next_attack": True
                    },
                    "then": "PANIC_WORRY_ADVICE"
                },
                {
                    "if": {
                        "substance_use": True
                    },
                    "then": "PANIC_SUBSTANCE_ADVICE"
                },
                {
                    "if": {
                        "day_to_day_impact": True
                    },
                    "then": "PANIC_INTERFERENCE_ADVICE"
                }
            ]
        },
        "schizophrenia": {
            "questions": [
                {
                    "id": "symptom_duration",
                    "text": "How many months have you been experiencing these symptoms (hallucinations, delusions, etc.)? (0-99)",
                    "type": "int",
                    "threshold": 6  # Typically, 6+ months are needed for a schizophrenia diagnosis
                },
                {
                    "id": "treatment_history",
                    "text": "Have you ever received treatment (medication/therapy) for these symptoms? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "hospitalization",
                    "text": "Have you ever been hospitalized for these symptoms or related issues? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "daily_life_impact",
                    "text": "Do these symptoms significantly affect your daily functioning, such as work, school, or social life? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "support_system",
                    "text": "Do you have a support system (friends/family) you can rely on regularly? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    "if": {
                        "symptom_duration": "<6"
                    },
                    "then": "SCHIZOPHRENIA_DURATION_WARNING"
                },
                {
                    "if": {
                        "symptom_duration": ">=6"
                    },
                    "then": "SCHIZOPHRENIA_PERSISTENT"
                },
                {
                    "if": {
                        "treatment_history": False
                    },
                    "then": "SCHIZOPHRENIA_NO_TREATMENT_ADVICE"
                },
                {
                    "if": {
                        "hospitalization": True
                    },
                    "then": "SCHIZOPHRENIA_HOSPITALIZATION_ADVICE"
                },
                {
                    "if": {
                        "daily_life_impact": True
                    },
                    "then": "SCHIZOPHRENIA_FUNCTIONAL_IMPAIRMENT"
                },
                {
                    "if": {
                        "support_system": False
                    },
                    "then": "SCHIZOPHRENIA_NO_SUPPORT_ADVICE"
                }
            ]
        },
        "bipolar disorder": {
            "questions": [
                {
                    "id": "manic_episode_duration",
                    "text": "How many days, on average, do your manic/hypomanic episodes last? (0-99)",
                    "type": "int",
                    "threshold": 7  # Typically, mania is considered at least 7 days; hypomania ~4 days.
                },
                {
                    "id": "number_of_episodes",
                    "text": "How many manic or hypomanic episodes have you had in the past year? (0-10+)",
                    "type": "int"
                },
                {
                    "id": "depressive_episodes",
                    "text": "Do you also experience depressive episodes? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "risky_behavior",
                    "text": "Have you engaged in potentially risky or impulsive behavior during these episodes? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "hospitalization",
                    "text": "Have you ever been hospitalized or required emergency treatment during a manic episode? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    "if": {
                        # If manic/hypomanic episodes last 7 days or more, it meets the typical threshold for mania.
                        "manic_episode_duration": ">=7"
                    },
                    "then": "BIPOLAR_MANIA_DURATION"
                },
                {
                    "if": {
                        # If user experiences depressive episodes as well,
                        # it suggests a bipolar I or II pattern depending on mania severity.
                        "depressive_episodes": True
                    },
                    "then": "BIPOLAR_DEPRESSIVE_EPISODES"
                },
                {
                    "if": {
                        "number_of_episodes": ">=3"
                    },
                    "then": "BIPOLAR_FREQUENT_EPISODES"
                },
                {
                    "if": {
                        "risky_behavior": True
                    },
                    "then": "BIPOLAR_RISKY_BEHAVIOR"
                },
                {
                    "if": {
                        "hospitalization": True
                    },
                    "then": "BIPOLAR_HOSPITALIZATION_ADVICE"
                }
            ]
        },
        "eating disorder": {
            "questions": [
                {
                    "id": "behavior_duration",
                    "text": "How many months have you been experiencing these eating-related behaviors or concerns? (0-99)",
                    "type": "int",
                    "threshold": 3  # Typically, disordered eating patterns lasting 3+ months raise clinical concern
                },
                {
                    "id": "weight_change",
                    "text": "Have you experienced significant weight changes (gain or loss) in the past few months? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "purging_behavior",
                    "text": "Do you engage in purging behaviors (e.g., self-induced vomiting, misuse of laxatives)? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "binge_eating",
                    "text": "Do you often eat large quantities of food in a short period (binge eating)? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "body_image_concerns",
                    "text": "Do you have persistent worries or distortions about your body shape or weight? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "medical_issues",
                    "text": "Have you experienced any medical issues (e.g., dizziness, fainting, menstrual irregularities) related to your eating habits? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    "if": {
                        "behavior_duration": "<3"
                    },
                    "then": "ED_EMERGING"
                },
                {
                    "if": {
                        "behavior_duration": ">=3"
                    },
                    "then": "ED_PERSISTENT"
                },
                {
                    "if": {
                        "weight_change": True
                    },
                    "then": "ED_WEIGHT_ADVICE"
                },
                {
                    "if": {
                        "purging_behavior": True
                    },
                    "then": "ED_PURGING_ADVICE"
                },
                {
                    "if": {
                        "binge_eating": True
                    },
                    "then": "ED_BINGE_ADVICE"
                },
                {
                    "if": {
                        "body_image_concerns": True
                    },
                    "then": "ED_BODY_IMAGE_ADVICE"
                },
                {
                    "if": {
                        "medical_issues": True
                    },
                    "then": "ED_MEDICAL_ISSUES_ADVICE"
                }
            ]
        },
        "adhd": {
            "questions": [
                {
                    "id": "symptom_duration",
                    "text": "How many months have you consistently noticed attention difficulties or hyperactivity? (0-99)",
                    "type": "int",
                    "threshold": 6  # Typically, ADHD is considered when symptoms persist at least 6 months
                },
                {
                    "id": "onset_age",
                    "text": "Were these issues noticeable before age 12? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "hyperfocus",
                    "text": "Do you ever hyperfocus on certain interests while neglecting other important tasks? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "time_management_issues",
                    "text": "Do you struggle significantly with time management or meeting deadlines? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "restlessness",
                    "text": "Do you often feel restless or fidgety, even in settings where you should remain still? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "impact_on_life",
                    "text": "Have these symptoms significantly impacted your daily life, such as work, school, or relationships? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    "if": {
                        "symptom_duration": "<6"
                    },
                    "then": "ADHD_DURATION_WARNING"
                },
                {
                    "if": {
                        "symptom_duration": ">=6"
                    },
                    "then": "ADHD_PERSISTENT"
                },
                {
                    "if": {
                        "onset_age": True
                    },
                    "then": "ADHD_CHILDHOOD_ONSET"
                },
                {
                    "if": {
                        "hyperfocus": True
                    },
                    "then": "ADHD_HYPERFOCUS_ADVICE"
                },
                {
                    "if": {
                        "time_management_issues": True
                    },
                    "then": "ADHD_TIME_MANAGEMENT_ADVICE"
                },
                {
                    "if": {
                        "restlessness": True
                    },
                    "then": "ADHD_RESTLESSNESS_ADVICE"
                },
                {
                    "if": {
                        "impact_on_life": True
                    },
                    "then": "ADHD_FUNCTIONAL_IMPAIRMENT"
                }
            ]
        },
        "borderline personality disorder": {
            "questions": [
                {
                    "id": "duration_of_instability",
                    "text": "How many months have you felt ongoing emotional instability or intense mood swings? (0-99)",
                    "type": "int",
                    "threshold": 6  # BPD patterns usually persist over time (6+ months).
                },
                {
                    "id": "fear_of_abandonment",
                    "text": "Do you fear being left alone or abandoned by people close to you? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "impulsive_behaviors",
                    "text": "Do you often engage in impulsive or risky behaviors (spending, substance use, etc.)? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "self_harm_urges",
                    "text": "Have you had urges to self-harm or suicidal thoughts? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "relationship_issues",
                    "text": "Do your relationships swing between intense closeness and extreme conflict? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "chronic_emptiness",
                    "text": "Do you frequently feel empty, bored, or numb inside? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    "if": {
                        "duration_of_instability": "<6"
                    },
                    "then": "BPD_DURATION_WARNING"
                },
                {
                    "if": {
                        "duration_of_instability": ">=6"
                    },
                    "then": "BPD_PERSISTENT"
                },
                {
                    "if": {
                        "fear_of_abandonment": True
                    },
                    "then": "BPD_FEAR_OF_ABANDONMENT_ADVICE"
                },
                {
                    "if": {
                        "impulsive_behaviors": True
                    },
                    "then": "BPD_IMPULSIVE_BEHAVIOR_ADVICE"
                },
                {
                    "if": {
                        "self_harm_urges": True
                    },
                    "then": "BPD_SELF_HARM_ADVICE"
                },
                {
                    "if": {
                        "relationship_issues": True
                    },
                    "then": "BPD_RELATIONSHIP_ADVICE"
                },
                {
                    "if": {
                        "chronic_emptiness": True
                    },
                    "then": "BPD_CHRONIC_EMPTINESS_ADVICE"
                }
            ]
        },
        "paranoia": {
            "questions": [
                {
                    "id": "trust_issues_duration",
                    "text": "How many months have you been feeling distrust or suspicion toward others? (0-99)",
                    "type": "int",
                    "threshold": 6  # Paranoid patterns persisting for several months may indicate personality traits.
                },
                {
                    "id": "doubting_loyalty",
                    "text": "Do you frequently doubt the loyalty or trustworthiness of friends/family without clear evidence? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "bearing_grudges",
                    "text": "Do you find yourself holding onto grudges or resentments for long periods? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "perceiving_attacks",
                    "text": "Do you often perceive comments or actions as personal attacks? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "confide_hesitation",
                    "text": "Are you hesitant to confide in others out of fear they might use the info against you? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "paranoid_thoughts_impact",
                    "text": "Are these paranoid or suspicious thoughts affecting your daily activities or relationships? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    "if": {
                        "trust_issues_duration": "<6"
                    },
                    "then": "PARANOIA_DURATION_WARNING"
                },
                {
                    "if": {
                        "trust_issues_duration": ">=6"
                    },
                    "then": "PARANOIA_PERSISTENT"
                },
                {
                    "if": {
                        "doubting_loyalty": True
                    },
                    "then": "PARANOIA_LOYALTY_ADVICE"
                },
                {
                    "if": {
                        "bearing_grudges": True
                    },
                    "then": "PARANOIA_GRUDGES_ADVICE"
                },
                {
                    "if": {
                        "perceiving_attacks": True
                    },
                    "then": "PARANOIA_PERCEIVED_ATTACKS_ADVICE"
                },
                {
                    "if": {
                        "confide_hesitation": True
                    },
                    "then": "PARANOIA_CONFIDE_HESITATION_ADVICE"
                },
                {
                    "if": {
                        "paranoid_thoughts_impact": True
                    },
                    "then": "PARANOIA_FUNCTIONAL_IMPAIRMENT"
                }
            ]
        },
        "psychosis": {
            "questions": [
                {
                    "id": "psychosis_duration",
                    "text": "How many months have you been experiencing these psychotic symptoms (e.g., hallucinations, delusions)? (0-99)",
                    "type": "int",
                    "threshold": 1  # Often if symptoms last longer than 1 month, we consider persistent psychosis.
                },
                {
                    "id": "trigger_known",
                    "text": "Do you suspect a known trigger for these symptoms, such as substance use or a major stressor? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "reality_testing",
                    "text": "Do you find it difficult to distinguish your experiences (voices, visions) from reality? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "insight_level",
                    "text": "Are you aware that these experiences might be part of a mental health condition? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "daily_life_impact",
                    "text": "Are these symptoms severely impacting your daily life, such as work, school, or relationships? (yes/no)",
                    "type": "bool"
                },
                {
                    "id": "safety_concerns",
                    "text": "Have you felt unsafe or feared harming yourself or others during these episodes? (yes/no)",
                    "type": "bool"
                }
            ],
            "logic": [
                {
                    "if": {
                        "psychosis_duration": "<1"
                    },
                    "then": "PSYCHOSIS_ACUTE_WARNING"
                },
                {
                    "if": {
                        "psychosis_duration": ">=1"
                    },
                    "then": "PSYCHOSIS_PERSISTENT"
                },
                {
                    "if": {
                        "trigger_known": True
                    },
                    "then": "PSYCHOSIS_TRIGGER_ADVICE"
                },
                {
                    "if": {
                        "reality_testing": True
                    },
                    "then": "PSYCHOSIS_REALITY_TESTING_ADVICE"
                },
                {
                    "if": {
                        "insight_level": False
                    },
                    "then": "PSYCHOSIS_LOW_INSIGHT_ADVICE"
                },
                {
                    "if": {
                        "daily_life_impact": True
                    },
                    "then": "PSYCHOSIS_FUNCTIONAL_IMPAIRMENT"
                },
                {
                    "if": {
                        "safety_concerns": True
                    },
                    "then": "PSYCHOSIS_SAFETY_WARNING"
                }
            ]
        },

    }
}

