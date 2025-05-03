from enum import Enum

class StatusTarefa(str, Enum):
    a_fazer = "a_fazer"
    em_progresso = "em_progresso"
    concluida = "concluida"
    bloqueada = "bloqueada"