from fastapi import FastAPI
from app.api.v1.endpoints import medications, history, vitals

app = FastAPI(
    title="SeniorInsight API",
    description="API para o sistema de monitoramento de saúde SeniorInsight.",
    version="1.0.0"
)

# Roteadores da API v1
app.include_router(medications.router, prefix="/v1/medications", tags=["Medications"])
app.include_router(history.router, prefix="/v1/history", tags=["History"])
app.include_router(vitals.router, prefix="/v1/vitals", tags=["Vitals"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API do SeniorInsight"}
