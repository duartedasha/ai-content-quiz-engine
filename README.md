# Mini Content Ingestion + Adaptive Quiz Engine
AI-powered backend system that ingests educational PDFs and generates adaptive quizzes using LLMs.
## Overview

This project is a prototype backend system that ingests educational PDF content and automatically generates quiz questions using a Large Language Model (LLM).

The system demonstrates how raw learning materials can be transformed into interactive assessments using an AI-driven backend pipeline.

The backend performs the following pipeline:

PDF → Text Extraction → Content Chunking → LLM Question Generation → Database Storage → Quiz APIs → Adaptive Difficulty

---

## Features

### 1. Content Ingestion

* Accepts educational PDFs
* Extracts and cleans text
* Splits text into manageable chunks
* Stores structured chunks in the database

---

### 2. AI Quiz Generation

* Uses **Google Gemini LLM**
* Generates multiple types of questions:

  * MCQ
  * True / False
  * Fill in the Blank
* Each generated question keeps **traceability to the source chunk**

---

### 3. Structured Storage

The system stores the following data:

* Source documents
* Content chunks
* Generated quiz questions
* Student answers

This allows traceability between **learning content → generated questions → student responses**.

---

### 4. Quiz Retrieval API

Provides endpoints to retrieve quiz questions based on difficulty and student performance.

---

### 5. Student Answer Submission

Students can submit answers through an API.

The backend:

* Validates answers
* Stores attempts
* Tracks correctness

---

### 6. Adaptive Difficulty

The system adjusts difficulty based on student performance.

Example logic:

* Correct answer → increase difficulty
* Incorrect answer → decrease difficulty

This simulates a **basic adaptive learning engine**.

---

## System Architecture Diagram

```
                +----------------------+
                |   Educational PDFs   |
                | (Math / Science /    |
                |  English Content)    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   PDF Ingestion API  |
                |      POST /ingest    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Text Extraction     |
                |   (PyMuPDF)          |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Text Cleaning       |
                |  Remove noise        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Content Chunking   |
                |  Split text blocks   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   SQLite Database    |
                |                      |
                |  sources             |
                |  chunks              |
                |  questions           |
                |  student_answers     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  LLM Quiz Generator  |
                |  Google Gemini API   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Quiz API           |
                |   GET /quiz          |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Student Answer API   |
                | POST /submit-answer  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Adaptive Difficulty  |
                | correct → harder     |
                | wrong   → easier     |
                +----------------------+
```

# Tech Stack

### Backend

* Python
* FastAPI

### Database

* SQLite

### AI Model

* Google Gemini LLM

### Libraries

* SQLAlchemy
* PyMuPDF
* python-dotenv
* google-generativeai

---

# Project Structure

```
peblo-ai-quiz-engine
│
├── app
│   ├── api
│   │   ├── ingest.py
│   │   ├── quiz.py
│   │   └── answers.py
│   │
│   ├── services
│   │   ├── pdf_service.py
│   │   ├── chunk_service.py
│   │   └── quiz_service.py
│   │
│   ├── models
│   │   ├── source.py
│   │   ├── chunk.py
│   │   ├── question.py
│   │   └── student_answer.py
│   │
│   ├── database
│   │   └── db.py
│   │
│   └── utils
│       ├── prompt.py
│       └── text_cleaner.py
│
├── pdfs
│   ├── peblo_pdf_grade1_math_numbers.pdf
│   ├── peblo_pdf_grade3_science_plants_animals.pdf
│   └── peblo_pdf_grade4_english_grammar.pdf
│
├── requirements.txt
├── .env.example
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```
git clone https://github.com/Vallen328/ai-content-quiz-engines.git
cd ai-content-quiz-engines
```

---

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file using `.env.example`.

Example:

```
GEMINI_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///./quiz.db
```

---

## 5. Run Backend Server

```
uvicorn app.main:app --reload
```

API documentation will be available at:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Ingest Content

```
POST /ingest
```

Example parameters:

```
filename: peblo_pdf_grade3_science_plants_animals.pdf
subject: Science
grade: 3
```

This extracts and stores content chunks.

---

## Generate Quiz

```
POST /generate-quiz
```

Generates quiz questions from stored content using the LLM.

---

## Retrieve Quiz

```
GET /quiz
```

Returns generated quiz questions.

Optional parameter:

```
student_id
```

Used for adaptive difficulty.

---

## Submit Student Answer

```
POST /submit-answer
```

Example request:

```
student_id: S001
question_id: <question_id>
selected_answer: 3
```

Response example:

```
{
  "correct": true
}
```

---

# Example Generated Question

```json
{
  "question": "Which part of a plant makes food?",
  "type": "MCQ",
  "options": ["Root","Leaf","Stem","Flower"],
  "answer": "Leaf",
  "difficulty": "easy"
}
```

---

# Example Workflow

1. Upload PDF using `/ingest`
2. Generate quiz questions using `/generate-quiz`
3. Retrieve questions using `/quiz`
4. Submit answers using `/submit-answer`
5. Difficulty adapts based on performance

---

# Future Improvements

* Embedding based duplicate question detection
* Better adaptive difficulty algorithm
* Topic extraction using NLP
* Question quality evaluation
* Multi-student learning analytics

---

# Author

**Dasha Duarte**
