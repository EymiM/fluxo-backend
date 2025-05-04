from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.tarefa import router as tarefa_router
from app.controllers.auth import router as auth_router
from app.controllers.websocket import router as websocket_router

app = FastAPI(title="Fluxo")

origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tarefa_router)
app.include_router(auth_router)
app.include_router(websocket_router)