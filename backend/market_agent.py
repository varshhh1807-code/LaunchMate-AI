import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def market_research(startup_idea):

    prompt = f"""
You are an expert Startup Marketing Consultant.

Analyze the startup idea and provide:

1. Target Audience
2. Marketing Channels
3. Social Media Strategy
4. Branding Ideas
5. Pricing Strategy
6. Promotional Activities
7. Customer Acquisition Plan
8. Marketing Tips

Startup Idea:
{startup_idea}
"""

    response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
)
    return response.text