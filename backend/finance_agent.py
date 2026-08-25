import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def finance_analysis(startup_idea):

    prompt = f"""
You are a Startup Finance Expert.

Analyze the following startup idea and provide:

1. Estimated Initial Investment
2. Monthly Expenses
3. Expected Revenue
4. Estimated Profit
5. Break-even Time
6. Funding Sources
7. Financial Risks
8. Cost Saving Suggestions

Startup Idea:
{startup_idea}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )

    return response.text