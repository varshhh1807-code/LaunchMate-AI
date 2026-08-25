import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
for model in client.models.list():
    print(model.name)

# Available models print avuthayi
print("\n=====AVAILABLE MODELS =====")
for model in client.models.list():
    print(model.name)
print("============================\n")


def generate_startup_idea(topic):
    prompt = f"""
You are a startup consultant.

Generate:
1. Startup Name
2. Problem Statement
3. Solution
4. Target Customers

Topic: {topic}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )

    return response.text
