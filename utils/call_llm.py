# utils/call_llm.py

import google.generativeai as genai
import os

# Set your API key (this should ideally come from env var for safety)
api_key = os.getenv("API Key")  # Set this in your terminal or .env
if not api_key:
    # fallback to hardcoded (less safe)
    api_key = "API Key"

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

def call_llm(prompt):
    print(f"📦 Prompt received by Gemini: '{prompt}'")
    response = model.generate_content(prompt)
    return response.text
