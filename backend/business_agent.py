from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def business_plan(startup_idea):
    prompt = f"""
Create a professional business plan for this startup:

Startup Idea:
{startup_idea}

Include:
1. Executive Summary
2. Business Model
3. Revenue Model
4. Target Customers
5. Growth Strategy
6. Risks
7. Future Scope
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text