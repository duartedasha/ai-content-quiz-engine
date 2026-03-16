from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json
import uuid
import ast
import traceback

from app.database.db import get_db
from app.models.chunk import Chunk
from app.models.question import Question


from app.utils.prompt import quiz_prompt
from app.services.quiz_service import generate_questions
from app.models.student_answer import StudentAnswer

from fastapi import Query

router = APIRouter()


@router.post("/generate-quiz")
def generate_quiz(db: Session = Depends(get_db)):

    chunks = db.query(Chunk).all()

    all_questions = []

    for chunk in chunks:

        prompt = quiz_prompt(chunk.text)

        result = generate_questions(prompt)
        print("LLM RAW OUTPUT:", result)

        try:
            questions = json.loads(result)

            for q in questions:

                if not q.get("question"):
                    continue

                if q.get("type") == "MCQ" and not q.get("options"):
                    continue

                # check duplicate question
                existing = db.query(Question).filter(
                    Question.question == q["question"]
                ).first()

                if existing:
                    continue

                question = Question(
                    question_id=str(uuid.uuid4()),
                    question=q["question"],
                    type=q["type"],
                    options=str(q.get("options", [])),
                    answer=q["answer"],
                    difficulty=str(q.get("difficulty", "easy")),
                    source_chunk_id=chunk.chunk_id
                )

                db.add(question)
                all_questions.append(q)

        except Exception as e:
            traceback.print_exc()
            continue

    db.commit()

    return {
        "questions_generated": len(all_questions)
    }


@router.get("/quiz")
def get_quiz(student_id: str = None, db: Session = Depends(get_db)):

    difficulty = "easy"

    if student_id:

        last_answer = db.query(StudentAnswer)\
            .filter(StudentAnswer.student_id == student_id)\
            .order_by(StudentAnswer.id.desc())\
            .first()

        if last_answer:

            if last_answer.is_correct:
                difficulty = "medium"
            else:
                difficulty = "easy"

    questions = db.query(Question)\
        .filter(Question.difficulty == difficulty)\
        .limit(5)\
        .all()

    result = []

    for q in questions:

        options = []

        if q.options:
            try:
                options = ast.literal_eval(q.options)
            except:
                options = []

        result.append({
            "question_id": q.question_id,
            "question": q.question,
            "type": q.type,
            "options": options,
            "difficulty": q.difficulty
        })

    return result