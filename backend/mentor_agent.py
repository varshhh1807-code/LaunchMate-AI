import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def mentor_advice(startup_idea):
    prompt = f"""
You are an experienced Startup Mentor.

Analyze the following startup idea and provide:

1. Startup Score (out of 10)
2. Strengths
3. Weaknesses
4. Potential Risks
5. Suggestions for Improvement
6. Next Steps
7. Final Advice

Startup Idea:
{startup_idea}
"""

    response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
)

    return response.text

