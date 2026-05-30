from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

# --- Base Models (for GET responses) ---

class MedicationBase(BaseModel):
    name: str
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    last_dose_time: Optional[datetime] = None
    status: Optional[str] = None

class HistoryEventBase(BaseModel):
    event_type: str
    title: str
    event_time: Optional[datetime] = None
    description: Optional[str] = None

class VitalBase(BaseModel):
    title: str
    value: str
    unit: Optional[str] = None
    status: Optional[str] = None
    recorded_at: Optional[datetime] = None

# --- Create Models (for POST requests) ---

class MedicationCreate(MedicationBase):
    pass

class HistoryEventCreate(HistoryEventBase):
    pass

class VitalCreate(VitalBase):
    pass

# --- Update Models (for PATCH requests) ---

class MedicationUpdate(BaseModel):
    name: Optional[str] = None
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    last_dose_time: Optional[datetime] = None
    status: Optional[str] = None

class HistoryEventUpdate(BaseModel):
    event_type: Optional[str] = None
    title: Optional[str] = None
    event_time: Optional[datetime] = None
    description: Optional[str] = None

class VitalUpdate(BaseModel):
    title: Optional[str] = None
    value: Optional[str] = None
    unit: Optional[str] = None
    status: Optional[str] = None
    recorded_at: Optional[datetime] = None

# --- Full Models with ID (for database and GET responses) ---

class Medication(MedicationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class HistoryEvent(HistoryEventBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class Vital(VitalBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
