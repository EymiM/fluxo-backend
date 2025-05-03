from fastapi import APIRouter, Depends
from app.schemas.tarefa import Filtro, PatchTarefa, Tarefa, MoverTarefa
from app.services.tarefa import listar_tarefas, adicionar_tarefa, mover_tarefa, editar_tarefa
from app.controllers.auth import get_current_user
from app.controllers.websocket import active_connections

router = APIRouter()

@router.post("/tarefas/ver-tarefas")
def get_tarefas(filtro: Filtro, user=Depends(get_current_user)):
    return listar_tarefas(filtro)

@router.post("/tarefas/create-tarefas")
async def post_tarefa(tarefa: Tarefa, user=Depends(get_current_user)):
    results = adicionar_tarefa(tarefa)
    await enviar_alerta(f"Tarefa '{tarefa.nome}' foi criada!")

    return results

@router.put("/tarefas/move-tarefas")
async def move_tarefa(mover: MoverTarefa, user=Depends(get_current_user)):
    tarefa = mover_tarefa(mover=mover)
    await enviar_alerta(f"Tarefa '{tarefa.nome}' foi modificada para '{mover.novo_status}'!")

@router.put("/tarefas/edita-tarefas")
async def patch_tarefa(tarefa: str, patch: PatchTarefa, user=Depends(get_current_user)):
    nova_tarefa = editar_tarefa(tarefa=tarefa, patch=patch)

    if patch.nome:
        await enviar_alerta(f"Tarefa '{tarefa}' foi alterada para '{patch.nome}'!")
    else:
        await enviar_alerta(f"Tarefa '{tarefa}' foi editada!")
    if patch.status:
        await enviar_alerta(f"Tarefa '{tarefa}' foi modificada para '{patch.status}'!")
    
    return nova_tarefa

async def enviar_alerta(mensagem: str):
    for connection in active_connections:
        try:
            await connection.send_text(mensagem)
        except:
            pass
