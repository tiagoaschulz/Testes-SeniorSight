from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.domain.models import Vital, VitalCreate, VitalUpdate
from app.application.services import VitalService
from app.infrastructure.database import get_db

router = APIRouter()

@router.get("/", response_model=List[Vital])
def get_vitals(db: Session = Depends(get_db)):
    service = VitalService(db)
    return service.get_vitals()

@router.post("/", response_model=Vital, status_code=status.HTTP_201_CREATED)
def create_vital(vital: VitalCreate, db: Session = Depends(get_db)):
    service = VitalService(db)
    return service.create_vital(vital)

@router.patch("/{id}", response_model=Vital)
def update_vital(id: int, vital: VitalUpdate, db: Session = Depends(get_db)):
    service = VitalService(db)
    updated_vital = service.update_vital(id, vital)
    if not updated_vital:
        raise HTTPException(status_code=404, detail="Vital not found")
    return updated_vital
