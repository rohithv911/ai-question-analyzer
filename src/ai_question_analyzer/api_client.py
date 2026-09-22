import os
import requests
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def fetch_todo():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout = 5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

def send_question(question):
    prompt = f"""
Analyze the following question.

Return valid JSON only with these fields:
- topic
- category
- difficulty
- answer
- keywords

The keywords field must be a list.

Question:
{question}
"""

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": "You analyze questions and return structured JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={"type": "json_object"}
        )

        text = response.choices[0].message.content

        try:
            result = json.loads(text)
            return result
        except json.JSONDecodeError:
            print("Invalid JSON response from AI")
            return None

    except Exception as error:
        print("API Error:", error)
        return None
