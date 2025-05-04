from enum import Enum

class StatusTarefa(str, Enum):
    a_fazer = "todo"
    em_progresso = "doing"
    concluida = "done"
    bloqueada = "bloqueada"