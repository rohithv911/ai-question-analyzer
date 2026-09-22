from ai_question_analyzer.question_handler import (collect_questions, filter_questions, get_question_count, count_by_difficulty, count_by_category, count_keywords, validate_question, get_valid_questions)
from ai_question_analyzer.api_client import send_question
from ai_question_analyzer.database import (create_table, load_questions, insert_question)

print("AI Question Analyzer")

create_table()
new_questions = collect_questions()
valid_questions = []
for question in new_questions:
    result = send_question(question["question"])
    if result is not None:
        question.update(result)
        if validate_question(question):
            valid_questions.append(question)
        else:
            print("Invalid question data")
    else:
        print("Error")
for question in valid_questions:
    insert_question(question)
questions = load_questions()

print("Stored questions:")

for index, question in enumerate(questions, 1):
    print(index, question["question"])

topic = input("\nEnter a topic to search: ").strip()
results = filter_questions(questions, "topic", topic)
print("\nTopic Search Results:")
for question in results:
    print(question)

difficulty = input("\nEnter a difficulty to search: ").strip()
results = filter_questions(questions, "difficulty", difficulty)
print("\nDifficulty Search Results:")
for question in results:
    print(question)

category = input("\nEnter a category to search: ").strip()
results = filter_questions(questions, "category", category)
print("\nCategory Search Results:")
for question in results:
    print(question)

print("\nQuestion Statistics")
print("Total questions:", get_question_count(questions))
print("By difficulty:", count_by_difficulty(questions))
print("By category:", count_by_category(questions))
print("Keywords:", count_keywords(questions))
