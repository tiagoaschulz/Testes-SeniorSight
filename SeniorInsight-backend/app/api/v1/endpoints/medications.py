from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.domain.models import Medication, MedicationCreate, MedicationUpdate
from app.application.services import MedicationService
from app.infrastructure.database import get_db

router = APIRouter()

@router.get("/", response_model=List[Medication])
def get_all_medications(db: Session = Depends(get_db)):
    service = MedicationService(db)
    return service.get_all_medications()

@router.post("/", response_model=Medication, status_code=status.HTTP_201_CREATED)
def create_medication(medication: MedicationCreate, db: Session = Depends(get_db)):
    service = MedicationService(db)
    return service.create_medication(medication)

@router.patch("/{id}", response_model=Medication)
def update_medication(id: int, medication: MedicationUpdate, db: Session = Depends(get_db)):
    service = MedicationService(db)
    updated_medication = service.update_medication(id, medication)
    if not updated_medication:
        raise HTTPException(status_code=404, detail="Medication not found")
    return updated_medication
