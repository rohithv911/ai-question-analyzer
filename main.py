from src.analyzer.question_handler import collect_questions
from src.analyzer.json_storage import load_questions, save_questions

print("AI Question Analyzer")

questions = load_questions()
new_questions = collect_questions()
questions.extend(new_questions)
save_questions(questions)

print("Stored questions: ")
for index, question in enumerate(questions, 1):
    print(index, question)