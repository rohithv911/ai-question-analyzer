# 🤖 AI Question Analyzer

An AI-powered web application that analyzes user questions using the **Groq API**, generates structured insights, and stores analyzed questions using **SQLite**.

The project was built to practice and demonstrate practical Python development, API integration, database management, testing, and deployment.

## 🚀 Live Demo

[AI Question Analyzer](https://ai-question-analyzer-cs5pltcczkt5zzwcllsfku.streamlit.app/)

---

## 📌 Overview

AI Question Analyzer allows users to enter a question and receive an AI-generated analysis containing:

- Topic
- Category
- Difficulty
- Answer
- Keywords

Analyzed questions are stored in a SQLite database and displayed in the application's **Previous Questions** section.

### Application Flow

```text
User enters a question
        ↓
Streamlit Web Interface
        ↓
Question Validation
        ↓
Groq API
        ↓
Structured AI Response
        ↓
SQLite Database
        ↓
Display Stored Questions
