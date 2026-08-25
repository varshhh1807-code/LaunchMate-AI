import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def marketing_strategy(startup_idea):

    prompt = f"""
You are a Startup Marketing Expert.

Provide:
1. Marketing Strategy
2. Branding Ideas
3. Social Media Plan
4. Customer Acquisition
5. Promotion Methods
6. Growth Plan

Startup Idea:
{startup_idea}
"""
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )

    return response.text

   