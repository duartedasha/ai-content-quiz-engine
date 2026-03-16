from fastapi import FastAPI
from app.database.db import engine, Base

from app.models import source, chunk, question, student_answer

from app.api.ingest import router as ingest_router

from app.api.quiz import router as quiz_router

from app.api.answers import router as answer_router

app = FastAPI(title="Peblo AI Quiz Engine")

Base.metadata.create_all(bind=engine)

app.include_router(ingest_router)
app.include_router(quiz_router)
app.include_router(answer_router)


@app.get("/")
def root():
    return {"message": "Peblo AI Quiz Engine Running"}