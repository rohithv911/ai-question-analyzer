import json

def save_questions(questions):
    with open("data/questions.json", "w", encoding="utf-8") as file:
        json.dump(questions, file, indent=4)

def load_questions():
    try:
        with open("data/questions.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []