def get_question():
    question = input("Enter your question: ").strip()
    return question

def is_valid_question(question):
    if not question:
        return False
    else:
        return True

def collect_questions():
    questions = []
    while True:
        question = get_question()
        if question.lower() == "done":
            break
        else:
            if not is_valid_question(question):
                print("Error: Question cannot be empty.")
            else:
                questions.append(question)

    return questions
