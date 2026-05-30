from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.repository import MedicationRepository, HistoryRepository, VitalRepository
from app.domain.models import MedicationCreate, MedicationUpdate, HistoryEventCreate, HistoryEventUpdate, VitalCreate, VitalUpdate
from app.infrastructure import orm_models

class PostgresMedicationRepository(MedicationRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[orm_models.Medication]:
        return self.db.query(orm_models.Medication).all()

    def create(self, medication: MedicationCreate) -> orm_models.Medication:
        db_medication = orm_models.Medication(**medication.model_dump())
        self.db.add(db_medication)
        self.db.commit()
        self.db.refresh(db_medication)
        return db_medication

    def update(self, id: int, medication: MedicationUpdate) -> Optional[orm_models.Medication]:
        db_medication = self.db.query(orm_models.Medication).filter(orm_models.Medication.id == id).first()
        if db_medication:
            update_data = medication.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_medication, key, value)
            self.db.commit()
            self.db.refresh(db_medication)
        return db_medication

class PostgresHistoryRepository(HistoryRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[orm_models.HistoryEvent]:
        return self.db.query(orm_models.HistoryEvent).all()

    def create(self, history_event: HistoryEventCreate) -> orm_models.HistoryEvent:
        db_history_event = orm_models.HistoryEvent(**history_event.model_dump())
        self.db.add(db_history_event)
        self.db.commit()
        self.db.refresh(db_history_event)
        return db_history_event

    def update(self, id: int, history_event: HistoryEventUpdate) -> Optional[orm_models.HistoryEvent]:
        db_history_event = self.db.query(orm_models.HistoryEvent).filter(orm_models.HistoryEvent.id == id).first()
        if db_history_event:
            update_data = history_event.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_history_event, key, value)
            self.db.commit()
            self.db.refresh(db_history_event)
        return db_history_event

class PostgresVitalRepository(VitalRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[orm_models.Vital]:
        return self.db.query(orm_models.Vital).all()

    def create(self, vital: VitalCreate) -> orm_models.Vital:
        db_vital = orm_models.Vital(**vital.model_dump())
        self.db.add(db_vital)
        self.db.commit()
        self.db.refresh(db_vital)
        return db_vital

    def update(self, id: int, vital: VitalUpdate) -> Optional[orm_models.Vital]:
        db_vital = self.db.query(orm_models.Vital).filter(orm_models.Vital.id == id).first()
        if db_vital:
            update_data = vital.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_vital, key, value)
            self.db.commit()
            self.db.refresh(db_vital)
        return db_vital
