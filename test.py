# test_gemini.py
from google import genai
import os

# ✅ Set API key here or export it as an environment variable
os.environ["GEMINI_API_KEY"] = "AIzaSyBcVWSDI0LrmBMPeCVqrCKNnOrOJjwjKBU"

# ✅ Initialize Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# ✅ Define prompt
prompt = "What is the capital of India?"

# ✅ Generate content using Gemini 2.5 Flash
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# ✅ Print result
print("Prompt:", prompt)
print("Gemini says:\n", response.text)
