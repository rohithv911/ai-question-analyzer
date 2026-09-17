import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

url = "https://generativelanguage.googleapis.com/v1beta/interactions"

headers = {
    "x-goog-api-key": api_key,
    "Content-Type": "application/json"
}

data = {
    "model": "gemini-3.6-flash",
    "input": "What is Python?"
}

response = requests.post(
    url,
    headers=headers,
    json=data,
    timeout=60
)

result = response.json()
print(response.status_code)
for step in result["steps"]:
    if step["type"] == "model_output":
        print(step["content"][0]["text"])
