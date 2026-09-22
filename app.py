import streamlit as st
st.set_page_config(
    page_title="AI Question Analyzer",
    page_icon="🤖",
    layout="wide"
)
from ai_question_analyzer.api_client import send_question
from ai_question_analyzer.database import (create_table, insert_question, get_questions)
from ai_question_analyzer.question_handler import (filter_questions, get_question_count, count_by_difficulty, count_by_category)

create_table()

st.title("🤖 AI Question Analyzer")
st.caption("Analyze, organize, and explore your questions using AI.")

question = st.text_area(
    "Enter your question:",
    placeholder="Example: What is machine learning?"
)

if st.button("Analyze Question"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing your question..."):
            result = send_question(question)

        if result is not None:
            st.success("Question analyzed successfully!")
            st.write("### Analysis")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Topic", result["topic"])
            with col2:
                st.metric("Category", result["category"])
            with col3:
                st.metric("Difficulty", result["difficulty"])
            st.write("**Answer:**", result["answer"])
            st.write("**Keywords:**", ", ".join(result["keywords"]))
            question_data = {
                "question": question,
                "topic": result["topic"],
                "category": result["category"],
                "difficulty": result["difficulty"],
                "answer": result["answer"],
                "keywords": result["keywords"]
            }
            existing_questions = get_questions()
            already_exists = any(
                item["question"].strip().lower() == question.strip().lower()
                for item in existing_questions
            )
            if already_exists:
                st.info("This question is already saved in your database.")
            else:
                insert_question(question_data)
                st.info("Question saved to your database.")
        else:
            st.error("Unable to analyze the question.")

st.divider()
st.header("📚 Previous Questions")
questions = get_questions()
if not questions:
    st.info("No questions have been analyzed yet.")
else:
    for item in questions:
        with st.expander(item["question"]):
            st.write("**Topic:**", item["topic"])
            st.write("**Category:**", item["category"])
            st.write("**Difficulty:**", item["difficulty"])
            st.write("**Answer:**", item["answer"])
            st.write("**Keywords:**", ", ".join(item["keywords"]))

st.divider()
st.header("🔎 Search Questions")
search_field = st.selectbox(
    "Search by:",
    ["topic", "category", "difficulty"]
)
search_value = st.text_input(
    "Enter search value:"
)
if st.button("Search"):
    if not search_value.strip():
        st.warning("Please enter a search value.")
    else:
        results = filter_questions(
            questions,
            search_field,
            search_value
        )
        if results:
            st.write(f"Found {len(results)} question(s).")
            for item in results:
                with st.expander(item["question"]):
                    st.write("**Topic:**", item["topic"])
                    st.write("**Category:**", item["category"])
                    st.write("**Difficulty:**", item["difficulty"])
                    st.write("**Answer:**", item["answer"])
                    st.write("**Keywords:**", ", ".join(item["keywords"]))
        else:
            st.info("No matching questions found.")

st.divider()
st.header("📊 Question Statistics")

total_questions = get_question_count(questions)
difficulty_counts = count_by_difficulty(questions)
category_counts = count_by_category(questions)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Questions", total_questions)

with col2:
    st.metric("Easy Questions", difficulty_counts.get("Easy", 0))

with col3:
    st.metric("Medium Questions", difficulty_counts.get("Medium", 0))

st.subheader("Difficulty Distribution")

if difficulty_counts:
    st.write(difficulty_counts)
else:
    st.info("No difficulty data available.")

st.subheader("Category Distribution")

if category_counts:
    st.write(category_counts)
else:
    st.info("No category data available.")