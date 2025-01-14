def do_action(action_key, answers):
    """
    Perform an action or display a message based on the rule's 'then' value.
    """
    #Depression
    if action_key == "ADVISE_LIFESTYLE":
        print("\nAdvice: Since it's been under 2 weeks, try improving sleep, exercise, "
              "and talking to a counselor if possible.")
    elif action_key == "ASK_MEDICATION":
        print("\nADVICE:\nIt has been more than 2 weeks; consider seeking professional help or medication.")
    elif action_key == "MEDICATION_OK":
        print("\nADVICE:\nGreat. Continue following your doctor's prescription and schedule follow-ups.")
    elif action_key == "ADVISE_PROFESSIONAL":
        print("\nADVICE:\nWe recommend consulting a healthcare provider to discuss treatment options.")
    elif action_key == "SHOW_HELPLINE":
        print("\nADVICE:\nIf you're having suicidal thoughts, please reach out to a crisis helpline immediately.\n"
              "In the UK, dial 111 or visit https://111.nhs.uk/guided-entry/mental-health-help to find one in your region.")

    #PTSD
    elif action_key == "ACUTE_STRESS_ADVICE":
        print("\nADVICE:\nYour traumatic symptoms have been present for less than 1 month. "
              "This may be more in line with acute stress disorder. "
              "Still, it's important to seek help early to prevent worsening.")
    elif action_key == "PTSD_PERSISTENT":
        print("\nADVICE:\nYour symptoms have lasted 1 month or more, suggesting persistent or diagnosable PTSD. "
              "We strongly recommend seeking professional support, such as therapy or counseling.")
    elif action_key == "PTSD_INTENSE":
        print("\nADVICE:\nYou indicated experiencing frequent nightmares or flashbacks, which can be very distressing. "
              "Professional therapy, including trauma-focused approaches, may greatly help you cope.")
    elif action_key == "PTSD_AVOIDANCE":
        print("\nADVICE:\nAvoidance of reminders of the trauma is common in PTSD, but it can prolong or worsen symptoms. "
              "Consider talking to a therapist about safe, gradual exposure or coping strategies.")
    elif action_key == "RECOMMEND_TRAUMA_FOCUSED_THERAPY":
        print("\nADVICE:\nYou haven't tried therapy yet, and trauma-focused therapy (like CBT or EMDR) "
              "is often very effective in treating PTSD. Please consider reaching out to a qualified specialist.")

    #Anxiety
    elif action_key == "ADVISE_SHORT_TERM_STRATEGIES":
        print("\nAdvice: Since you've had these symptoms for less than 6 months, "
              "it might be acute or situational. Consider relaxation techniques, "
              "mindfulness exercises, or talking to a therapist if it persists.")
    elif action_key == "ADVISE_LONG_TERM_STRATEGIES":
        print("\nADVICE:\nYou've had these symptoms for 6 months or longer. This suggests "
              "a more persistent form of anxiety. We strongly recommend seeking "
              "professional help, such as a psychologist or psychiatrist.")
    elif action_key == "MEDICATION_ADVICE":
        print("\nADVICE:\nIt's great that you're taking medication for your anxiety. "
              "Ensure you're following up regularly with your doctor to monitor effectiveness "
              "and manage side effects.")
    elif action_key == "THERAPY_RECOMMENDATION":
        print("\nADVICE:\nTherapy can be very effective for managing anxiety long-term. "
              "You might consider cognitive behavioral therapy (CBT), "
              "counseling, or support groups.")
    
    # OCD
    elif action_key == "OCD_EMERGING_ADVICE":
        print("\nADVICE:\nSince it's under 1 month, these behaviors may be emerging. Still, "
              "it's good to track them and consider early professional advice if they worsen.")
    elif action_key == "OCD_PERSISTENT_ADVICE":
        print("\nADVICE:\nYou’ve had these symptoms for at least a month. Persistent OCD "
              "often benefits from cognitive-behavioral therapy or medication.")
    elif action_key == "OCD_HOURS_ADVICE":
        print("\nADVICE:\nSpending more than 1 hour a day on obsessions or compulsions indicates "
              "a significant impact. A mental health professional can help you manage this.")
    elif action_key == "OCD_INTERFERENCE_ADVICE":
        print("\nADVICE:\nBecause it significantly interferes with daily life, seeking help "
              "from a therapist or psychiatrist is strongly recommended.")
    elif action_key == "OCD_THERAPY_RECOMMENDATION":
        print("\nADVICE:\nIf you haven’t tried therapy, look into specialized treatments like ERP (Exposure and Response Prevention).")
    elif action_key == "OCD_MEDICATION_FOLLOWUP":
        print("\nADVICE:\nMedication can be effective for OCD. Continue working with your doctor for proper management and check-ups.")
    
    #Panic attack
    elif action_key == "PANIC_ATTACKS_FREQUENT":
        print("\nADVICE:\nYou report at least 1 panic attack weekly. This frequency can be disruptive; "
              "consider seeking professional help (therapy, medication).")
    elif action_key == "PANIC_AVOIDANCE_ADVICE":
        print("\nADVICE:\nAvoiding places or situations due to fear of attacks can worsen anxiety over time. "
              "Therapeutic approaches like CBT or exposure therapy may help.")
    elif action_key == "PANIC_WORRY_ADVICE":
        print("\nADVICE:\nConstantly worrying about the next attack can lead to heightened stress. "
              "Relaxation techniques, mindfulness, or counseling might help break the cycle.")
    elif action_key == "PANIC_SUBSTANCE_ADVICE":
        print("\nADVICE:\nUsing alcohol or unprescribed medication for panic can be risky. "
              "Please consider talking to a healthcare professional about safer coping strategies.")
    elif action_key == "PANIC_INTERFERENCE_ADVICE":
        print("\nADVICE:\nBecause panic attacks are significantly impacting your daily life, "
              "professional intervention (therapy/psychiatry) is highly recommended.")

    #Schizo
    elif action_key == "SCHIZOPHRENIA_DURATION_WARNING":
        print("\nADVICE:\nIf your symptoms have lasted under 6 months, it may be an acute or "
              "short-term psychotic disorder. Please consult with a mental health professional "
              "to clarify diagnosis and treatment.")
    elif action_key == "SCHIZOPHRENIA_PERSISTENT":
        print("\nADVICE:\nSince your symptoms have persisted for 6 months or more, it may indicate "
              "a chronic condition. Ongoing psychiatric care is crucial.")
    elif action_key == "SCHIZOPHRENIA_NO_TREATMENT_ADVICE":
        print("\nADVICE:\nIt seems you've not pursued treatment yet. Schizophrenia is often best managed "
              "with a combination of medication and therapy—please reach out to a doctor or therapist.")
    elif action_key == "SCHIZOPHRENIA_HOSPITALIZATION_ADVICE":
        print("\nADVICE:\nYou've indicated a past hospitalization, which suggests more severe episodes. "
              "Continuity of care and follow-up with a mental health professional is vital.")
    elif action_key == "SCHIZOPHRENIA_FUNCTIONAL_IMPAIRMENT":
        print("\nADVICE:\nIf these symptoms significantly impact daily functioning, "
              "please consider support services, therapy, and potentially medication.")
    elif action_key == "SCHIZOPHRENIA_NO_SUPPORT_ADVICE":
        print("\nADVICE:\nHaving no reliable support system can make coping difficult. "
              "Consider local support groups, community resources, or online forums "
              "where you can find help and connection.")

    #Bipolar
    elif action_key == "BIPOLAR_MANIA_DURATION":
        print("\nADVICE:\nYour episodes last about a week or longer, which meets criteria for mania. "
              "This usually warrants professional intervention, like medication or therapy.")
    elif action_key == "BIPOLAR_DEPRESSIVE_EPISODES":
        print("\nADVICE:\nYou also experience depressive episodes, which aligns with bipolar I or II disorder. "
              "Talk to a mental health professional about treatment strategies for both phases.")
    elif action_key == "BIPOLAR_FREQUENT_EPISODES":
        print("\nADVICE:\nHaving three or more episodes in a year can be significant. Consider seeing "
              "a psychiatrist for possible mood stabilizers or therapy to manage episode frequency.")
    elif action_key == "BIPOLAR_RISKY_BEHAVIOR":
        print("\nADVICE:\nEngaging in risky or impulsive behavior can have serious consequences. "
              "Professional help can offer strategies to recognize and manage these impulses.")
    elif action_key == "BIPOLAR_HOSPITALIZATION_ADVICE":
        print("\nADVICE:\nPrior hospitalization indicates severe episodes. Ongoing medication management "
              "and support from mental health services are highly recommended.")

    #Eating Disorder
    elif action_key == "ED_EMERGING":
        print("\nADVICE:\nThese issues have lasted less than 3 months, but early help can prevent worsening. "
              "Consider talking to a mental health professional or nutritionist.")
    elif action_key == "ED_PERSISTENT":
        print("\nADVICE:\nYour disordered eating patterns have lasted 3 months or more. This is significant; "
              "consult a healthcare provider for a thorough assessment and support plan.")
    elif action_key == "ED_WEIGHT_ADVICE":
        print("\nADVICE:\nSignificant weight changes—up or down—can be dangerous without monitoring. "
              "Please see a doctor to rule out serious complications.")
    elif action_key == "ED_PURGING_ADVICE":
        print("\nADVICE:\nPurging behaviors can harm your body, including risking electrolyte imbalances. "
              "Professional help (medical, nutritional, and therapeutic) is strongly advised.")
    elif action_key == "ED_BINGE_ADVICE":
        print("\nADVICE:\nFrequent binge eating can be part of Binge Eating Disorder or Bulimia. "
              "Therapy (like CBT) and support groups might help you manage triggers and behaviors.")
    elif action_key == "ED_BODY_IMAGE_ADVICE":
        print("\nADVICE:\nPersistent worries about body image can worsen eating habits. "
              "A psychologist or counselor experienced with body image issues may help.")
    elif action_key == "ED_MEDICAL_ISSUES_ADVICE":
        print("\nADVICE:\nExperiencing medical issues (fainting, irregular periods, etc.) is a red flag. "
              "Seek medical attention to address potential complications as soon as possible.")
        
    #ADHD
    elif action_key == "ADHD_DURATION_WARNING":
        print("\nADVICE:\nYour symptoms have lasted under 6 months. It's possible this is a short-term issue, "
              "but keep an eye on it. If it persists or worsens, consider professional evaluation.")
    elif action_key == "ADHD_PERSISTENT":
        print("\nADVICE:\nYour symptoms have persisted for at least 6 months, "
              "which suggests a chronic pattern typical of ADHD.")
    elif action_key == "ADHD_CHILDHOOD_ONSET":
        print("\nADVICE:\nNoticing these issues before age 12 aligns with core ADHD diagnostic criteria. "
              "Early onset is key in many formal diagnoses.")
    elif action_key == "ADHD_HYPERFOCUS_ADVICE":
        print("\nADVICE:\nHyperfocus can be a double-edged sword—use strategies (timers, reminders) "
              "to ensure other tasks aren’t neglected.")
    elif action_key == "ADHD_TIME_MANAGEMENT_ADVICE":
        print("\nADVICE:\nStruggling with time management can be common in ADHD. "
              "Consider using planning apps, calendar reminders, or structured routines.")
    elif action_key == "ADHD_RESTLESSNESS_ADVICE":
        print("\nADVICE:\nPersistent restlessness or fidgetiness can disrupt daily life. "
              "Certain therapies, mindfulness practices, or mild physical outlets may help.")
    elif action_key == "ADHD_FUNCTIONAL_IMPAIRMENT":
        print("\nADVICE:\nBecause these symptoms significantly affect your daily life, "
              "we recommend talking to a healthcare professional about an ADHD assessment.")
    
    #BPD
    elif action_key == "BPD_DURATION_WARNING":
        print("\nADVICE:\nYour emotional instability is under 6 months. It may be situational. "
              "If it persists, consider seeking help from a mental health professional.")
    elif action_key == "BPD_PERSISTENT":
        print("\nADVICE:\nYou’ve experienced emotional instability for 6 months or more, "
              "which could align with a persistent pattern often seen in personality disorders.")
    elif action_key == "BPD_FEAR_OF_ABANDONMENT_ADVICE":
        print("\nADVICE:\nFear of abandonment can be overwhelming. Therapy (like DBT) may help build healthier attachments.")
    elif action_key == "BPD_IMPULSIVE_BEHAVIOR_ADVICE":
        print("\nADVICE:\nFrequent impulsive behaviors can be risky. Consider professional help to develop coping strategies "
              "and impulse control techniques.")
    elif action_key == "BPD_SELF_HARM_ADVICE":
        print("\nADVICE:\nUrges to self-harm or suicidal thoughts are serious. Please reach out to a mental health professional. "
              "If you feel unsafe, contact an emergency helpline immediately.")
    elif action_key == "BPD_RELATIONSHIP_ADVICE":
        print("\nADVICE:\nIntense relationship patterns can be stressful. A therapist can help with communication and "
              "emotional regulation techniques.")
    elif action_key == "BPD_CHRONIC_EMPTINESS_ADVICE":
        print("\nADVICE:\nPersistent emptiness can be debilitating. DBT or CBT techniques may help you find meaning "
              "and reduce these feelings.")
        
    #Paranoia

    elif action_key == "PARANOIA_DURATION_WARNING":
        print("\nADVICE:\nYour feelings of distrust have been under 6 months. They could be related to a recent event or stress. "
              "If they persist, consider professional evaluation.")
    elif action_key == "PARANOIA_PERSISTENT":
        print("\nADVICE:\nYour distrust or suspicion has lasted 6+ months, suggesting a more ingrained pattern. "
              "Therapy or counseling could help you develop healthier coping strategies.")
    elif action_key == "PARANOIA_LOYALTY_ADVICE":
        print("\nADVICE:\nDoubting the loyalty of those close to you might stem from anxiety or past experiences. "
              "A mental health professional can help clarify these perceptions.")
    elif action_key == "PARANOIA_GRUDGES_ADVICE":
        print("\nADVICE:\nHolding onto grudges for long periods can affect your well-being. "
              "Therapy may help you process unresolved feelings and find healthier ways to cope.")
    elif action_key == "PARANOIA_PERCEIVED_ATTACKS_ADVICE":
        print("\nADVICE:\nFrequently perceiving others’ comments as attacks can heighten stress. "
              "Learning to challenge these assumptions in therapy could improve your relationships.")
    elif action_key == "PARANOIA_CONFIDE_HESITATION_ADVICE":
        print("\nADVICE:\nHesitating to share personal details due to fear of betrayal can isolate you from supportive relationships. "
              "Consider discussing trust-building strategies with a counselor.")
    elif action_key == "PARANOIA_FUNCTIONAL_IMPAIRMENT":
        print("\nADVICE:\nYour paranoid or suspicious thoughts appear to be significantly impacting daily life. "
              "Seek professional help—cognitive-behavioral therapy or other interventions might help reduce this impact.")
    
    #Psychosis
    elif action_key == "PSYCHOSIS_ACUTE_WARNING":
        print("\nADVICE:\nEven if symptoms have been present for less than 1 month, acute psychosis "
              "still requires prompt professional attention.")
    elif action_key == "PSYCHOSIS_PERSISTENT":
        print("\nADVICE:\nSymptoms for over a month indicate persistent psychosis. "
              "Seek specialized psychiatric evaluation, as early intervention is critical.")
    elif action_key == "PSYCHOSIS_TRIGGER_ADVICE":
        print("\nADVICE:\nYou mentioned a possible trigger (substance or stress). Consider discussing "
              "this with a professional to address underlying factors.")
    elif action_key == "PSYCHOSIS_REALITY_TESTING_ADVICE":
        print("\nADVICE:\nDifficulty distinguishing hallucinations/delusions from reality can be extremely distressing. "
              "Immediate professional support is advisable.")
    elif action_key == "PSYCHOSIS_LOW_INSIGHT_ADVICE":
        print("\nADVICE:\nLow insight can lead to delayed help-seeking. A mental health professional might help "
              "you understand these experiences.")
    elif action_key == "PSYCHOSIS_FUNCTIONAL_IMPAIRMENT":
        print("\nADVICE:\nYour daily life is significantly affected by these symptoms. A comprehensive evaluation "
              "and treatment plan (medication and/or therapy) can be very helpful.")
    elif action_key == "PSYCHOSIS_SAFETY_WARNING":
        print("\nADVICE:\nIf you feel unsafe or fear harming yourself or others, please reach out to a crisis line or "
              "seek emergency medical help immediately.")
    
    else:
        print(f"\n[No explicit action defined for '{action_key}'.]")