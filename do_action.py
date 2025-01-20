def do_action(action_key, answers):
    """
    Performs an action (i.e., prints advice) based on the 'then' value in the rules.
    This version uses a dictionary lookup instead of a large if-elif chain.
    """
    # Lookup the message from ACTION_MESSAGES
    msg = ACTION_MESSAGES.get(action_key)
    
    if msg:
        print(msg)
    else:
        # No message found for this action key
        print(f"\n[No explicit action defined for '{action_key}'].")

ACTION_MESSAGES = {
    # -------------- Depression --------------
    "ADVISE_LIFESTYLE": "\nADVICE:\nSince it's been under 2 weeks, try improving sleep, exercise, "
                        "and talking to a counselor if possible.",
    "ASK_MEDICATION": "\nADVICE:\nIt has been more than 2 weeks; consider seeking professional help or medication.",
    "MEDICATION_OK": "\nADVICE:\nGreat. Continue following your doctor's prescription and schedule follow-ups.",
    "ADVISE_PROFESSIONAL": "\nADVICE:\nWe recommend consulting a healthcare provider to discuss treatment options.",
    "SHOW_HELPLINE": "\nADVICE:\nIf you're having suicidal thoughts, please reach out to a crisis helpline immediately.\n"
                     "In the UK, dial 111 or visit https://111.nhs.uk/guided-entry/mental-health-help.",

    # -------------- PTSD --------------
    "ACUTE_STRESS_ADVICE": "\nADVICE:\nYour traumatic symptoms have been present for less than 1 month. "
                           "This may be acute stress disorder. Seek help early to prevent worsening.",
    "PTSD_PERSISTENT": "\nADVICE:\nYour symptoms have lasted 1 month or more, suggesting persistent PTSD. "
                       "We strongly recommend seeking professional support, such as therapy.",
    "PTSD_INTENSE": "\nADVICE:\nYou're experiencing frequent nightmares or flashbacks, which can be distressing. "
                    "Trauma-focused therapy may help you cope.",
    "PTSD_AVOIDANCE": "\nADVICE:\nAvoidance of trauma reminders is common but can worsen PTSD. "
                      "Consider gradual exposure with a therapist.",
    "RECOMMEND_TRAUMA_FOCUSED_THERAPY": "\nADVICE:\nTrauma-focused therapy (CBT or EMDR) is often very effective. "
                                        "Please reach out to a qualified specialist.",

    # -------------- Anxiety --------------
    "ADVISE_SHORT_TERM_STRATEGIES": "\nADVICE:\nSince you've had these symptoms for less than 6 months, "
                                    "try relaxation techniques or mindfulness. Consider therapy if it persists.",
    "ADVISE_LONG_TERM_STRATEGIES": "\nADVICE:\n6+ months of anxiety may require professional help, such as a psychologist.",
    "MEDICATION_ADVICE": "\nADVICE:\nIt's great you're taking medication. Follow up with your doctor to monitor effectiveness.",
    "THERAPY_RECOMMENDATION": "\nADVICE:\nTherapy can be effective long-term. Consider CBT, counselling, or support groups.",

    # -------------- OCD --------------
    "OCD_EMERGING_ADVICE": "\nADVICE:\nUnder 1 month, so these OCD symptoms may be emerging. Early advice can help.",
    "OCD_PERSISTENT_ADVICE": "\nADVICE:\nAt least 1 month of OCD symptoms often requires CBT or medication.",
    "OCD_HOURS_ADVICE": "\nADVICE:\nSpending 1+ hour a day on obsessions is significant. Seek a mental health professional.",
    "OCD_INTERFERENCE_ADVICE": "\nADVICE:\nOCD is interfering with daily life. A therapist or psychiatrist is strongly recommended.",
    "OCD_THERAPY_RECOMMENDATION": "\nADVICE:\nConsider specialized ERP therapy. Early intervention is key.",
    "OCD_MEDICATION_FOLLOWUP": "\nADVICE:\nMedication can be effective for OCD. Continue with regular doctor check-ups.",

    # -------------- Panic Disorder --------------
    "PANIC_ATTACKS_FREQUENT": "\nADVICE:\nAt least 1 panic attack weekly can be disruptive. "
                              "Therapy or medication might be necessary.",
    "PANIC_AVOIDANCE_ADVICE": "\nADVICE:\nAvoiding places due to fear of panic can worsen anxiety. "
                              "Exposure therapy may help.",
    "PANIC_WORRY_ADVICE": "\nADVICE:\nWorrying constantly about attacks raises stress. Relaxation or counselling could help.",
    "PANIC_SUBSTANCE_ADVICE": "\nADVICE:\nUsing alcohol or unprescribed meds is risky. Talk to a professional.",
    "PANIC_INTERFERENCE_ADVICE": "\nADVICE:\nPanic attacks impact daily life; professional intervention is highly recommended.",

    # -------------- Schizophrenia --------------
    "SCHIZOPHRENIA_DURATION_WARNING": "\nADVICE:\nUnder 6 months could be a short-term psychotic disorder. "
                                      "Consult a mental health professional.",
    "SCHIZOPHRENIA_PERSISTENT": "\nADVICE:\n6+ months suggests a chronic condition. Ongoing psychiatric care is vital.",
    "SCHIZOPHRENIA_NO_TREATMENT_ADVICE": "\nADVICE:\nYou've not pursued treatment yet. Schizophrenia often requires meds + therapy.",
    "SCHIZOPHRENIA_HOSPITALIZATION_ADVICE": "\nADVICE:\nPast hospitalization indicates severe episodes. Consistent follow-up is vital.",
    "SCHIZOPHRENIA_FUNCTIONAL_IMPAIRMENT": "\nADVICE:\nIf daily functioning is impaired, seek therapy or medication.",
    "SCHIZOPHRENIA_NO_SUPPORT_ADVICE": "\nADVICE:\nWithout a support system, coping is harder. Look for local groups or online forums.",

    # -------------- Bipolar --------------
    "BIPOLAR_MANIA_DURATION": "\nADVICE:\nEpisodes lasting a week or more meet mania criteria. "
                              "Professional intervention is usually required.",
    "BIPOLAR_DEPRESSIVE_EPISODES": "\nADVICE:\nYou also experience depressive phases, indicating bipolar I/II. "
                                   "Discuss both in therapy.",
    "BIPOLAR_FREQUENT_EPISODES": "\nADVICE:\nThree+ episodes yearly is significant. Mood stabilisers or therapy may help.",
    "BIPOLAR_RISKY_BEHAVIOR": "\nADVICE:\nRisky impulses can be serious. Seek professional help to manage them.",
    "BIPOLAR_HOSPITALIZATION_ADVICE": "\nADVICE:\nPast hospitalization indicates severe episodes. Consistent medication is key.",

    # -------------- Eating Disorder --------------
    "ED_EMERGING": "\nADVICE:\nUnder 3 months, but early help can prevent worsening. "
                   "Consider a mental health professional or nutritionist.",
    "ED_PERSISTENT": "\nADVICE:\n3+ months of disordered eating is serious; get a thorough assessment and support plan.",
    "ED_WEIGHT_ADVICE": "\nADVICE:\nSignificant weight changes can be dangerous. See a doctor for monitoring.",
    "ED_PURGING_ADVICE": "\nADVICE:\nPurging harms the body. Medical, nutritional, and therapeutic aid is strongly advised.",
    "ED_BINGE_ADVICE": "\nADVICE:\nFrequent bingeing may indicate Bulimia or BED. Therapy and support groups can help.",
    "ED_BODY_IMAGE_ADVICE": "\nADVICE:\nBody image worries often worsen disordered eating. A specialized counselor can assist.",
    "ED_MEDICAL_ISSUES_ADVICE": "\nADVICE:\nFainting, irregular periods, etc. are red flags. Seek prompt medical attention.",

    # -------------- ADHD --------------
    "ADHD_DURATION_WARNING": "\nADVICE:\nUnder 6 months may be short-term issues, but monitor. "
                             "If persistent, consider professional evaluation.",
    "ADHD_PERSISTENT": "\nADVICE:\n6+ months suggests a chronic pattern typical of ADHD.",
    "ADHD_CHILDHOOD_ONSET": "\nADVICE:\nOnset before age 12 aligns with ADHD diagnostic criteria.",
    "ADHD_HYPERFOCUS_ADVICE": "\nADVICE:\nHyperfocus can be double-edged. Use reminders so other tasks aren't neglected.",
    "ADHD_TIME_MANAGEMENT_ADVICE": "\nADVICE:\nTime management struggles are common. Planning apps and routines help.",
    "ADHD_RESTLESSNESS_ADVICE": "\nADVICE:\nRestlessness can disrupt daily life. Therapies and mindfulness might help.",
    "ADHD_FUNCTIONAL_IMPAIRMENT": "\nADVICE:\nSignificant impact indicates a need for professional ADHD assessment.",

    # -------------- Borderline Personality Disorder --------------
    "BPD_DURATION_WARNING": "\nADVICE:\nUnder 6 months of instability may be situational. "
                            "If persistent, seek professional help.",
    "BPD_PERSISTENT": "\nADVICE:\nOver 6 months suggests a long-standing pattern often seen in personality disorders.",
    "BPD_FEAR_OF_ABANDONMENT_ADVICE": "\nADVICE:\nFear of abandonment can be overwhelming. DBT or therapy may help.",
    "BPD_IMPULSIVE_BEHAVIOR_ADVICE": "\nADVICE:\nImpulsive behaviors are risky. Professional support can improve coping.",
    "BPD_SELF_HARM_ADVICE": "\nADVICE:\nSelf-harm urges or suicidal thoughts are serious. Contact a mental health professional.",
    "BPD_RELATIONSHIP_ADVICE": "\nADVICE:\nIntense relationship swings can be stressful. Therapy aids communication.",
    "BPD_CHRONIC_EMPTINESS_ADVICE": "\nADVICE:\nChronic emptiness can be debilitating. DBT or CBT may help find meaning.",

    # -------------- Paranoia --------------
    "PARANOIA_DURATION_WARNING": "\nADVICE:\nDistrust under 6 months could be event-related. "
                                 "If persistent, consider professional help.",
    "PARANOIA_PERSISTENT": "\nADVICE:\nDistrust 6+ months suggests ingrained patterns. Therapy can build healthier perspectives.",
    "PARANOIA_LOYALTY_ADVICE": "\nADVICE:\nFrequent loyalty doubts could stem from anxiety. Talk to a mental health professional.",
    "PARANOIA_GRUDGES_ADVICE": "\nADVICE:\nHolding grudges can harm well-being. Therapy helps process unresolved feelings.",
    "PARANOIA_PERCEIVED_ATTACKS_ADVICE": "\nADVICE:\nInterpreting comments as personal attacks can raise stress. "
                                         "Challenging assumptions in therapy helps.",
    "PARANOIA_CONFIDE_HESITATION_ADVICE": "\nADVICE:\nFearing betrayal can isolate you. Trust-building strategies may help.",
    "PARANOIA_FUNCTIONAL_IMPAIRMENT": "\nADVICE:\nParanoid thoughts affecting daily life require professional intervention.",

    # -------------- Psychosis --------------
    "PSYCHOSIS_ACUTE_WARNING": "\nADVICE:\nEven under 1 month, acute psychosis needs prompt professional attention.",
    "PSYCHOSIS_PERSISTENT": "\nADVICE:\nOver 1 month indicates persistent psychosis. Early psychiatric evaluation is crucial.",
    "PSYCHOSIS_TRIGGER_ADVICE": "\nADVICE:\nSubstance or stress triggers may be involved. A professional can address them.",
    "PSYCHOSIS_REALITY_TESTING_ADVICE": "\nADVICE:\nDifficulty distinguishing hallucinations/delusions from reality is distressing. "
                                        "Seek immediate support.",
    "PSYCHOSIS_LOW_INSIGHT_ADVICE": "\nADVICE:\nLow insight can delay help. A mental health professional might improve understanding.",
    "PSYCHOSIS_FUNCTIONAL_IMPAIRMENT": "\nADVICE:\nSignificant daily impairment suggests medication and/or therapy.",
    "PSYCHOSIS_SAFETY_WARNING": "\nADVICE:\nIf you fear harm to self or others, call a crisis line or emergency services immediately."
}
