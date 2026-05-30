from sqlalchemy.orm import Session
from app.infrastructure.repositories import PostgresMedicationRepository, PostgresHistoryRepository, PostgresVitalRepository
from app.domain.models import MedicationCreate, MedicationUpdate, HistoryEventCreate, HistoryEventUpdate, VitalCreate, VitalUpdate

class MedicationService:
    def __init__(self, db: Session):
        self.repository = PostgresMedicationRepository(db)

    def get_all_medications(self):
        return self.repository.get_all()

    def create_medication(self, medication: MedicationCreate):
        return self.repository.create(medication)

    def update_medication(self, id: int, medication: MedicationUpdate):
        return self.repository.update(id, medication)

class HistoryService:
    def __init__(self, db: Session):
        self.repository = PostgresHistoryRepository(db)

    def get_history(self):
        return self.repository.get_all()

    def create_history_event(self, history_event: HistoryEventCreate):
        return self.repository.create(history_event)

    def update_history_event(self, id: int, history_event: HistoryEventUpdate):
        return self.repository.update(id, history_event)

class VitalService:
    def __init__(self, db: Session):
        self.repository = PostgresVitalRepository(db)

    def get_vitals(self):
        return self.repository.get_all()

    def create_vital(self, vital: VitalCreate):
        return self.repository.create(vital)

    def update_vital(self, id: int, vital: VitalUpdate):
        return self.repository.update(id, vital)
