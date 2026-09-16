import json

def save_questions(questions):
    with open("data/questions.json", "w", encoding="utf-8") as file:
        json.dump(questions, file, indent=4)

def load_questions():
    try:
        with open("data/questions.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            clean_questions = []
            for item in data:
                if isinstance(item, str):
                    clean_questions.append({"question": item})
                else:
                    clean_questions.append(item)
            return clean_questions
    except (FileNotFoundError, json.JSONDecodeError):
        return []