from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.enums.prioridade import PrioridadeTarefa
from app.enums.status import StatusTarefa

class MoverTarefa(BaseModel):
    nome: str
    novo_status: str

class ChecklistItem(BaseModel):
    topico: str
    feito: bool = False

class Tarefa(BaseModel):
    nome: str
    descricao: Optional[str]
    status: StatusTarefa
    prioridade: Optional[PrioridadeTarefa]
    responsavel: Optional[str]
    data_criacao: Optional[datetime] = datetime.now()
    data_vencimento: Optional[datetime]
    tempo_realizado: Optional[int]
    tags: Optional[List[str]] = []
    dependencias: Optional[List[str]] = []
    checklist: Optional[List[ChecklistItem]] = []
    em_alarme: Optional[bool] = False

class Filtro(BaseModel):
    ls_nome: Optional[List[str]] = []
    ls_status: Optional[List[StatusTarefa]] = []
    ls_prioridade: Optional[List[PrioridadeTarefa]] = []
    ls_responsavel: Optional[List[str]] = []
    ls_tags: Optional[List[str]] = []
    ls_dependendecias: Optional[List[str]] = []
    em_alarme: Optional[bool] = None