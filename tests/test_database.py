import pytest
from ai_question_analyzer.database import (
    get_connection,
    create_table,
    insert_question,
    get_question_by_id,
    update_question_difficulty,
    delete_question,
    get_questions,
)
from ai_question_analyzer.question_handler import (validate_question, filter_questions)

@pytest.fixture
def test_database(tmp_path):
    database_path = tmp_path / "test.db"
    create_table(str(database_path))
    return str(database_path)

def test_get_question_by_id(test_database):
    question = {
        "question": "Test question",
        "topic": "Testing",
        "category": "Test",
        "difficulty": "Easy",
        "answer": "Test answer",
        "keywords": ["test"]
    }

    question_id = insert_question(question, test_database)
    result = get_question_by_id(question_id, test_database)
    assert result is not None
    assert result["question"] == "Test question"
    assert result["topic"] == "Testing"

def test_get_question_by_id_not_found(test_database):
    result = get_question_by_id(999999, test_database)
    assert result is None

def test_update_question_difficulty(test_database):
    question = {
    "question": "Test question",
    "topic": "Testing",
    "category": "Test",
    "difficulty": "Easy",
    "answer": "Test answer",
    "keywords": ["test"]
    }
    question_id = insert_question(question, test_database)
    update_question_difficulty(question_id, "Hard", test_database)
    result = get_question_by_id(question_id, test_database)
    assert result["difficulty"] == "Hard"

def test_delete_question(test_database):
    question = {
        "question": "Test question",
        "topic": "Testing",
        "category": "Test",
        "difficulty": "Easy",
        "answer": "Test answer",
        "keywords": ["test"]
    }
    question_id = insert_question(question, test_database)

    delete_question(question_id, test_database)

    result = get_question_by_id(question_id, test_database)

    assert result is None

def test_get_questions(test_database):
    question1 = {
        "question": "What is Python?",
        "topic": "Python",
        "category": "Programming",
        "difficulty": "Easy",
        "answer": "Python is a programming language.",
        "keywords": ["python"]
    }

    question2 = {
        "question": "What is SQL?",
        "topic": "SQL",
        "category": "Database",
        "difficulty": "Medium",
        "answer": "SQL is used to work with relational databases.",
        "keywords": ["sql", "database"]
    }

    insert_question(question1, test_database)
    insert_question(question2, test_database)

    results = get_questions(test_database)

    assert len(results) == 2
    assert results[0]["question"] == "What is Python?"
    assert results[1]["question"] == "What is SQL?"

def test_validate_question():
    question = {
        "question": "What is Python?",
        "topic": "Python",
        "category": "Programming",
        "difficulty": "Easy",
        "answer": "Python is a programming language.",
        "keywords": ["python"]
    }

    assert validate_question(question) is True


def test_validate_question_missing_field():
    question = {
        "question": "What is Python?",
        "topic": "Python",
        "category": "Programming",
        "difficulty": "Easy",
        "answer": "Python is a programming language."
    }

    assert validate_question(question) is False

def test_filter_questions():
    questions = [
        {
            "question": "What is Python?",
            "topic": "Python",
            "category": "Programming",
            "difficulty": "Easy"
        },
        {
            "question": "What is SQL?",
            "topic": "SQL",
            "category": "Database",
            "difficulty": "Medium"
        },
        {
            "question": "What are Python lists?",
            "topic": "Python",
            "category": "Programming",
            "difficulty": "Medium"
        }
    ]

    results = filter_questions(questions, "topic", "Python")

    assert len(results) == 2
    assert results[0]["question"] == "What is Python?"
    assert results[1]["question"] == "What are Python lists?"