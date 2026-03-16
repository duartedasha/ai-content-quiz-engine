from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.question import Question
from app.models.student_answer import StudentAnswer

router = APIRouter()


@router.post("/submit-answer")
def submit_answer(student_id: str, question_id: str, selected_answer: str, db: Session = Depends(get_db)):

    question = db.query(Question).filter(Question.question_id == question_id).first()

    if not question:
        return {"error": "Question not found"}

    correct = (
        selected_answer.strip().lower()
        ==
        question.answer.strip().lower()
    )

    student_answer = StudentAnswer(
        student_id=student_id,
        question_id=question_id,
        selected_answer=selected_answer,
        is_correct=correct
    )

    db.add(student_answer)
    db.commit()

    return {
        "correct": correct
    }