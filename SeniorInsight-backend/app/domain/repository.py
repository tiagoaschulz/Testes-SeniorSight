from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Medication, MedicationCreate, MedicationUpdate, HistoryEvent, HistoryEventCreate, HistoryEventUpdate, Vital, VitalCreate, VitalUpdate

class MedicationRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Medication]:
        pass

    @abstractmethod
    def create(self, medication: MedicationCreate) -> Medication:
        pass

    @abstractmethod
    def update(self, id: int, medication: MedicationUpdate) -> Optional[Medication]:
        pass

class HistoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[HistoryEvent]:
        pass

    @abstractmethod
    def create(self, history_event: HistoryEventCreate) -> HistoryEvent:
        pass

    @abstractmethod
    def update(self, id: int, history_event: HistoryEventUpdate) -> Optional[HistoryEvent]:
        pass

class VitalRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Vital]:
        pass

    @abstractmethod
    def create(self, vital: VitalCreate) -> Vital:
        pass

    @abstractmethod
    def update(self, id: int, vital: VitalUpdate) -> Optional[Vital]:
        pass
