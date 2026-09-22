import sqlite3
import json
import os

def get_connection(database = "data/questions.db"):
    os.makedirs(os.path.dirname(database), exist_ok=True)
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    return connection

def create_table(database = "data/questions.db"):
    connection = get_connection(database)
    connection.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            topic TEXT NOT NULL,
            category TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            answer TEXT NOT NULL,
            keywords TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def insert_question(question, database = "data/questions.db"):
    connection = get_connection(database)
    cursor = connection.execute(
        '''
        INSERT INTO questions
        (question, topic, category, difficulty, answer, keywords)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (
            question["question"],
            question["topic"],
            question["category"],
            question["difficulty"],
            question["answer"],
            json.dumps(question["keywords"])
        )
    )
    connection.commit()
    question_id = cursor.lastrowid
    connection.close()
    return question_id 

def get_questions(database = "data/questions.db"):
    connection = get_connection(database)
    cursor = connection.execute(
        "SELECT * FROM questions"
    )
    rows = cursor.fetchall()
    questions = []
    for row in rows:
        question = dict(row)
        question["keywords"] = json.loads(question["keywords"])
        questions.append(question)
    connection.close()
    return questions

def load_questions(database = "data/questions.db"):
    return get_questions(database)

def get_question_by_id(question_id, database = "data/questions.db"):
    connection = get_connection(database)
    cursor = connection.execute(
        "SELECT * FROM questions WHERE id = ?",
        (question_id,)
    )
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    question = dict(row)
    question["keywords"] = json.loads(question["keywords"])
    return question

def update_question_difficulty(question_id, difficulty, database = "data/questions.db"):
    connection = get_connection(database)
    cursor = connection.execute(
        '''
        UPDATE questions 
        SET difficulty = ?
        WHERE id = ?
        ''',
        (
            difficulty,
            question_id
        )
    )
    if cursor.rowcount == 0:
        print("Question not found")
    else:
        print("Question updated")

    connection.commit()
    connection.close()

def delete_question(question_id, database = "data/questions.db"):
    connection = get_connection(database)

    cursor = connection.execute(
        """
        DELETE FROM questions
        WHERE id = ?
        """,
        (question_id,)
    )
    if cursor.rowcount == 0:
        print("Question not found")
    else:
        print("Question deleted")

    connection.commit()
    connection.close()

def delete_all_questions(database = "data/questions.db"):
    connection = get_connection(database)

    connection.execute("DELETE FROM questions")

    connection.commit()
    connection.close()