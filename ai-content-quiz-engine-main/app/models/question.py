from sqlalchemy import Column, Integer, String, Text
from app.database.db import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(String, unique=True)
    question = Column(Text)
    type = Column(String)
    options = Column(Text)
    answer = Column(String)
    difficulty = Column(String)
    source_chunk_id = Column(String)