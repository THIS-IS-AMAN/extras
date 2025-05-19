

import os
import requests
from dotenv import load_dotenv

# Load the .env file to get the API key
load_dotenv()

# Mistral API setup
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

def query_llm(prompt: str) -> str:
    
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "mistral-small",  # options: mistral-small, mistral-medium
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Mistral API Error: {e}"
