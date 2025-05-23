from datetime import datetime
from fastapi import HTTPException
from app.storage import fluxo
from app.schemas.tarefa import Filtro, PatchTarefa, Tarefa, MoverTarefa, PostTarefa

variavel_id = 0

def listar_tarefas(filtro: Filtro):
    fluxo_f = fluxo

    if filtro.ls_nome:
        fluxo_f = [t for t in fluxo_f if t.nome in filtro.ls_nome]

    if filtro.ls_status:
        fluxo_f = [t for t in fluxo_f if t.status in filtro.ls_status]

    if filtro.ls_prioridade:
        fluxo_f = [t for t in fluxo_f if t.prioridade in filtro.ls_prioridade]

    if filtro.ls_responsavel:
        fluxo_f = [t for t in fluxo_f if t.responsavel in filtro.ls_responsavel]

    if filtro.ls_tags:
        fluxo_f = [t for t in fluxo_f if any(tag in t.tags for tag in filtro.ls_tags)]

    if filtro.ls_dependendecias:
        fluxo_f = [t for t in fluxo_f if any(dep in t.dependencias for dep in filtro.ls_dependendecias)]

    if filtro.em_alarme is not None:
        fluxo_f = [t for t in fluxo_f if t.em_alarme == filtro.em_alarme]

    return fluxo_f

def obter_tarefa(nome: str):
    for t in fluxo:
        if t.nome == nome:
            return t
        
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

def adicionar_tarefa(tarefa: PostTarefa):
    global variavel_id
    for t in fluxo:
        if t.nome == tarefa.nome:
            raise HTTPException(status_code=400, detail="Uma tarefa com esse nome já existe.")
    tarefa.data_criacao = tarefa.data_criacao or datetime.now()
    variavel_id+=1
    nova_tarefa = Tarefa(**tarefa.dict(), id=variavel_id)
    fluxo.append(nova_tarefa)

    return nova_tarefa

def mover_tarefa(mover: MoverTarefa):
    for t in fluxo:
        if t.nome == mover.tarefa:
            t.status = mover.novo_status
            return t
        
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

def editar_tarefa(tarefa: str, patch: PatchTarefa):
    for t in fluxo:
        if t.nome == tarefa:
            update_data = patch.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(t, key, value)
            return t
        
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")