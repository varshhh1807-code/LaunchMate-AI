import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=key)

def ask_gemini(question):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=question,
        )

        return response.text

    except Exception as e:
        print("ERROR:", e)
        return str(e)