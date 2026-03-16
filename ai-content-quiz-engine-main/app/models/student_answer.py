from sqlalchemy import Column, Integer, String, Boolean
from app.database.db import Base

class StudentAnswer(Base):
    __tablename__ = "student_answers"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String)
    question_id = Column(String)
    selected_answer = Column(String)
    is_correct = Column(Boolean)