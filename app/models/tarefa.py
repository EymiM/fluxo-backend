from pydantic import BaseModel

class Tarefa(BaseModel):
    nome: str

class MoverTarefa(BaseModel):
    nome: str
    nova_coluna: str
