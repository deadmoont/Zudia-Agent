from google import genai
import os

# ✅ Initialize Gemini client once
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY", "AIzaSyDYyP_2j1VcgWbfUzsgSaM6rC7U-D9893k")
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def generate_from_gemini(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """
    Generate text output using Gemini 2.5 Flash.
    Returns plain text content.
    """
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )
        return response.text
    except Exception as e:
        print("Gemini API error:", e)
        return f"Error: {e}"
