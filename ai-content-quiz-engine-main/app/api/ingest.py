import os
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.source import Source
from app.models.chunk import Chunk

from app.services.pdf_service import extract_text_from_pdf
from app.services.chunk_service import chunk_text
from app.utils.text_cleaner import clean_text

router = APIRouter()


@router.post("/ingest")
def ingest_pdf(filename: str, subject: str, grade: int, db: Session = Depends(get_db)):

    file_path = f"pdfs/{filename}"

    text = extract_text_from_pdf(file_path)

    clean = clean_text(text)

    chunks = chunk_text(clean)

    source_id = f"SRC_{filename}"

    existing_source = db.query(Source).filter(
        Source.source_id == source_id
    ).first()

    if existing_source:
        return {
            "message": "Source already ingested",
            "source_id": source_id
        }

    source = Source(
        source_id=source_id,
        filename=filename,
        subject=subject,
        grade=grade
    )

    db.add(source)
    db.commit()

    for i, chunk in enumerate(chunks):

        chunk_id = f"{source_id}_CH_{i}"

        new_chunk = Chunk(
            chunk_id=chunk_id,
            source_id=source_id,
            text=chunk,
            topic="general"
        )

        db.add(new_chunk)

    db.commit()

    return {
        "message": "PDF ingested successfully",
        "chunks_created": len(chunks)
    }