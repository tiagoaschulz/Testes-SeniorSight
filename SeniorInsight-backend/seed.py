import logging
from datetime import datetime
from app.infrastructure.database import SessionLocal, engine
from app.infrastructure.orm_models import Base, Medication, HistoryEvent, Vital

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cria uma sessão com o banco de dados
db = SessionLocal()

def seed_data():
    """
    Popula o banco de dados com dados iniciais se as tabelas estiverem vazias.
    """
    try:
        # Apaga e recria as tabelas. CUIDADO: Isso deleta todos os dados existentes.
        logger.info("Recriando todas as tabelas...")
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        logger.info("Tabelas recriadas com sucesso.")

        # Dados iniciais para Medications
        medications_to_add = [
            Medication(name='Losartana', dosage='50mg', frequency='1x ao dia', last_dose_time=datetime(2026, 5, 30, 8, 30), status='ok'),
            Medication(name='Metformina', dosage='850mg', frequency='2x ao dia', last_dose_time=None, status='warning')
        ]
        db.add_all(medications_to_add)
        logger.info(f"{len(medications_to_add)} registros de medicamentos adicionados.")

        # Dados iniciais para History Events
        history_to_add = [
            HistoryEvent(event_type='medication', title='Lisinopril tomado', event_time=datetime(2026, 5, 30, 8, 30), description='Dose administrada corretamente.'),
            HistoryEvent(event_type='alert', title='Arritmia detectada', event_time=datetime(2026, 5, 30, 10, 15), description='Padrão cardíaco irregular detectado.')
        ]
        db.add_all(history_to_add)
        logger.info(f"{len(history_to_add)} registros de histórico adicionados.")

        # Dados iniciais para Vitals
        vitals_to_add = [
            Vital(title='Heart Rate', value='72', unit='BPM', status='stable', recorded_at=datetime.now()),
            Vital(title='Blood Pressure', value='120/80', unit='MMHG', status='stable', recorded_at=datetime.now()),
            Vital(title='Oxygen Level', value='92%', unit='SPO2', status='alert', recorded_at=datetime.now()),
            Vital(title='Temperature', value='36.8°', unit='CELSIUS', status='stable', recorded_at=datetime.now())
        ]
        db.add_all(vitals_to_add)
        logger.info(f"{len(vitals_to_add)} registros de sinais vitais adicionados.")

        # Confirma a transação
        db.commit()
        logger.info("Dados iniciais inseridos com sucesso no banco de dados!")

    except Exception as e:
        logger.error(f"Ocorreu um erro ao popular o banco de dados: {e}")
        db.rollback()
    finally:
        db.close()
        logger.info("Sessão com o banco de dados fechada.")

if __name__ == "__main__":
    logger.info("Iniciando o script para popular o banco de dados...")
    seed_data()
