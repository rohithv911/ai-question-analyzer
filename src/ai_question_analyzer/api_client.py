import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

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
    url = "https://generativelanguage.googleapis.com/v1beta/interactions"

    headers = {
    "x-goog-api-key": api_key,
    "Content-Type": "application/json"
    }
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
    data = {
        "model": "gemini-3.6-flash",
        "input": prompt
    }
    try:
        response = requests.post(url, headers = headers, json=data, timeout = 60)
        if response.status_code == 200:
            data = response.json()
            for step in data["steps"]:
                if step["type"] == "model_output":
                    text = step["content"][0]["text"]
                    text = text.replace("```json", "").replace("```", "").strip()
                    try:
                        result = json.loads(text)
                        return result
                    except json.JSONDecodeError:
                        print("Invalid JSON response from AI")
                        return None
        else:
            print("API Error:", response.status_code)
            print(response.text)
            return None
    except requests.exceptions.RequestException as error:
        print('Request Error:', error)
        return None
    
