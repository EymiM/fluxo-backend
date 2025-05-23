from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.enums.prioridade import PrioridadeTarefa
from app.enums.status import StatusTarefa

class MoverTarefa(BaseModel):
    tarefa: str
    novo_status: StatusTarefa

class ChecklistItem(BaseModel):
    topico: str
    feito: bool = False

class TarefaPK(BaseModel):
    id: int

class TarefaBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    status: StatusTarefa
    prioridade: PrioridadeTarefa
    responsavel: Optional[str] = None
    data_criacao: Optional[datetime] = datetime.now()
    data_vencimento: Optional[datetime] = None
    tempo_realizado: Optional[int] = None
    tags: Optional[List[str]] = []
    dependencias: Optional[List[str]] = []
    checklist: Optional[List[ChecklistItem]] = []
    em_alarme: Optional[bool] = False

class Tarefa(TarefaBase, TarefaPK):
    pass

class PostTarefa(TarefaBase):
    pass

class PatchTarefa(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    status: Optional[StatusTarefa] = None
    prioridade: Optional[PrioridadeTarefa] = None
    responsavel: Optional[str] = None
    data_vencimento: Optional[datetime] = None
    tags: Optional[List[str]] = None
    dependencias: Optional[List[str]] = None
    checklist: Optional[List[ChecklistItem]] = None

class Filtro(BaseModel):
    ls_nome: Optional[List[str]] = []
    ls_status: Optional[List[StatusTarefa]] = []
    ls_prioridade: Optional[List[PrioridadeTarefa]] = []
    ls_responsavel: Optional[List[str]] = []
    ls_tags: Optional[List[str]] = []
    ls_dependendecias: Optional[List[str]] = []
    em_alarme: Optional[bool] = None