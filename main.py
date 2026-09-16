from src.analyzer.question_handler import collect_questions
from src.analyzer.json_storage import load_questions, save_questions
from src.analyzer.api_client import send_question
print("AI Question Analyzer")

questions = load_questions()
new_questions = collect_questions()
for question in new_questions:
    result = send_question(question)
    if result is not None:
        print(result["title"])
    else:
        print("Error")
questions.extend(new_questions)
save_questions(questions)

print("Stored questions: ")
for index, question in enumerate(questions, 1):
    print(index, question)