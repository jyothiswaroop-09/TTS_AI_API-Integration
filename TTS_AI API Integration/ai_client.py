import os
import requests

class MistralClient:
    def __init__(self):
        self.api_key = os.getenv("MISTRAL_API_KEY")
        self.base_url = os.getenv("MISTRAL_BASE_URL", "https://api.mistral.ai/v1")

        if not self.api_key:
            raise ValueError("MISTRAL_API_KEY not set in environment")

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def chat(self, model, messages):
        url = f"{self.base_url}/chat/completions"
        body = {
            "model": model,
            "messages": messages
        }

        response = requests.post(url, json=body, headers=self.headers)
        response.raise_for_status()
        return response.json()

def format_response(text, fmt=None):
    if fmt == "bullet":
        lines = text.split(". ")
        return "\n".join([f"- {l}" for l in lines if l.strip()])

    if fmt == "number":
        lines = text.split(". ")
        return "\n".join([f"{i+1}. {l}" for i, l in enumerate(lines) if l.strip()])

    return text
