from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(String, unique=True)
    filename = Column(String)
    subject = Column(String)
    grade = Column(Integer)