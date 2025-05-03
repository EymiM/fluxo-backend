from fastapi import FastAPI
from app.controllers.tarefa import router as tarefa_router
from app.controllers.auth import router as auth_router

app = FastAPI(title="Fluxo")

app.include_router(tarefa_router)
app.include_router(auth_router)
