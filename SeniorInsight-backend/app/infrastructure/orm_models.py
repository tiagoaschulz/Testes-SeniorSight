from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from .database import Base

class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    dosage = Column(String(100))
    frequency = Column(String(100))
    last_dose_time = Column(TIMESTAMP(timezone=True))
    status = Column(String(50))

class HistoryEvent(Base):
    __tablename__ = "history_events"

    id = Column(Integer, primary_key=True)
    event_type = Column(String(100), nullable=False)
    title = Column(String(255), nullable=False)
    event_time = Column(TIMESTAMP(timezone=True))
    description = Column(Text)

class Vital(Base):
    __tablename__ = "vitals"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    value = Column(String(100), nullable=False)
    unit = Column(String(50))
    status = Column(String(50))
    recorded_at = Column(TIMESTAMP(timezone=True))
