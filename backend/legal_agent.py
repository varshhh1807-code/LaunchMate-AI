from agent import ask_gemini

def legal_guide(startup_idea):
    prompt = f"""
    Provide legal guidance for this startup:

    {startup_idea}

    Include:
    1. Business Registration
    2. Licenses Required
    3. Tax Compliance
    4. Data Privacy Rules
    5. Legal Risks
    """

    return ask_gemini(prompt)