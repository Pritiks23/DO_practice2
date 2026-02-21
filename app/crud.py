"""
Database interaction layer.
Encapsulates all DB logic.
"""

from sqlalchemy.orm import Session
from .models import IngestedData

def create_record(db: Session, payload: str):
    record = IngestedData(payload=payload)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def update_status(db: Session, record_id: int, status: str):
    record = db.query(IngestedData).filter(IngestedData.id == record_id).first()
    if record:
        record.status = status
        db.commit()
        db.refresh(record)
    return record

def get_record(db: Session, record_id: int):
    return db.query(IngestedData).filter(IngestedData.id == record_id).first()
