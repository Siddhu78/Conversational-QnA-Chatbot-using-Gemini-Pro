from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

from google.generativeai import list_models
print("Available Gemini models:")
for m in list_models():
    print("•", m.name)
 