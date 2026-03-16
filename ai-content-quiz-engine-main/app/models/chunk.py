from sqlalchemy import Column, Integer, String, Text
from app.database.db import Base

class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(Integer, primary_key=True, index=True)
    chunk_id = Column(String, unique=True)
    source_id = Column(String)
    text = Column(Text)
    topic = Column(String)