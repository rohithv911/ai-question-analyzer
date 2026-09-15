from src.analyzer.question_handler import get_question, is_valid_question, collect_questions

print("AI Question Analyzer")
questions = collect_questions()
print("Stored questions: ")
for index, question in enumerate(questions, 1):
    print(index, question)