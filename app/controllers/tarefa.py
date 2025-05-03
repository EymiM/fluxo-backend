from fastapi import APIRouter, Depends
from app.schemas.tarefa import Tarefa, MoverTarefa
from app.services.tarefa import listar_tarefas, adicionar_tarefa, mover_tarefa
from app.controllers.auth import get_current_user
from app.controllers.websocket import active_connections

router = APIRouter()

@router.get("/tarefas/ver-tarefas")
def get_tarefas(user=Depends(get_current_user)):
    return listar_tarefas()

@router.post("/tarefas/create-tarefas")
async def post_tarefa(tarefa: Tarefa, user=Depends(get_current_user)):
    results = adicionar_tarefa(tarefa)
    await enviar_alerta(f"Tarefa '{tarefa.nome}' foi criada!")

    return results

@router.put("/tarefas/move-tarefas")
async def put_tarefa(mover: MoverTarefa, user=Depends(get_current_user)):
    tarefa = mover_tarefa(mover=mover)
    await enviar_alerta(f"Tarefa '{tarefa.nome}' foi modificada para '{mover.novo_status}'!")

async def enviar_alerta(mensagem: str):
    for connection in active_connections:
        try:
            await connection.send_text(mensagem)
        except:
            pass
