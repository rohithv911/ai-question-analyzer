from ai_question_analyzer.question_handler import collect_questions
from ai_question_analyzer.json_storage import load_questions, save_questions
from ai_question_analyzer.api_client import send_question
print("AI Question Analyzer")

questions = load_questions()
new_questions = collect_questions()
for question in new_questions:
    result = send_question(question["question"])
    if result is not None:
        question.update(result)
    else:
        print("Error")
questions.extend(new_questions)
save_questions(questions)

print("Stored questions:")

for index, question in enumerate(questions, 1):
    print(index, question["question"])

    if "answer" in question:
        print("Topic:", question["topic"])
        print("Category:", question["category"])
        print("Difficulty:", question["difficulty"])
        print("Answer:", question["answer"])
        print("Keywords:", question["keywords"])
        print()