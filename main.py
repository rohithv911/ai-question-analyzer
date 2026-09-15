print("AI Question Analyzer")

questions = []
while True:
    question = input("Enter your question: ").strip()
    if not question:
        print("Error: Question cannot be empty.")
    elif question.lower() == "done":
        break
    else:
        print(f"Question received: {question}")
        questions.append(question)

print("Stored questions: ")
for index, question in enumerate(questions, 1):
    print(index, question)