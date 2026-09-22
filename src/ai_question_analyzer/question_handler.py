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
                questions.append({"question": question})

    return questions

def filter_questions(questions, field, value):
    matches = []
    for question in questions:
        if field in question and value.lower() in question[field].lower():
            matches.append(question)
    return matches

def get_question_count(questions):
    return len(questions)

def count_by_difficulty(questions):
    difficulties = []
    for question in questions:
        if "difficulty" in question:
            difficulty = question["difficulty"]
            difficulties.append(difficulty)
    return count_values(difficulties)

def count_by_category(questions):
    categories = []
    for question in questions:
        if "category" in question:
            category = question["category"]
            categories.append(category)
    return count_values(categories)

def count_keywords(questions):
    keywords = []
    for question in questions:
        if "keywords" in question:
            for keyword in question["keywords"]:
                keywords.append(keyword)
    return count_values(keywords)

def count_values(values):
    counts = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts

def validate_question(question):
    required_fields = [
        "question",
        "topic",
        "category",
        "difficulty",
        "answer",
        "keywords"
    ]
    for field in required_fields:
        if field not in question:
            return False
    return True

def get_valid_questions(questions):
    valid_questions = []
    for question in questions:
        if validate_question(question):
            valid_questions.append(question)
    return valid_questions