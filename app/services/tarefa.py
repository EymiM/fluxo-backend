from datetime import datetime
from fastapi import HTTPException
from app.storage import fluxo
from app.models.tarefa import Tarefa, MoverTarefa

def listar_tarefas():
    return fluxo

def obter_tarefa(nome: str):
    for t in fluxo:
        if t.nome == nome:
            return t
        
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

def adicionar_tarefa(tarefa: Tarefa):
    for t in fluxo:
        if t.nome == tarefa.nome:
            raise HTTPException(status_code=400, detail="Uma tarefa com esse nome já existe.")
    tarefa.data_criacao = tarefa.data_criacao or datetime.now()
    fluxo.append(tarefa)

    return {"mensagem": "Tarefa adicionada com sucesso"}

def mover_tarefa(mover: MoverTarefa):
    for t in fluxo:
        if t.nome == mover.nome:
            t.status = mover.novo_status
            return t
        
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")