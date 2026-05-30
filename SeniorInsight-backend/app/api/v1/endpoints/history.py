from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.domain.models import HistoryEvent, HistoryEventCreate, HistoryEventUpdate
from app.application.services import HistoryService
from app.infrastructure.database import get_db

router = APIRouter()

@router.get("/", response_model=List[HistoryEvent])
def get_history(db: Session = Depends(get_db)):
    service = HistoryService(db)
    return service.get_history()

@router.post("/", response_model=HistoryEvent, status_code=status.HTTP_201_CREATED)
def create_history_event(history_event: HistoryEventCreate, db: Session = Depends(get_db)):
    service = HistoryService(db)
    return service.create_history_event(history_event)

@router.patch("/{id}", response_model=HistoryEvent)
def update_history_event(id: int, history_event: HistoryEventUpdate, db: Session = Depends(get_db)):
    service = HistoryService(db)
    updated_event = service.update_history_event(id, history_event)
    if not updated_event:
        raise HTTPException(status_code=404, detail="History event not found")
    return updated_event
