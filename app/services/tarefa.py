from app.storage import fluxo

def listar_tarefas():
    return fluxo

def adicionar_tarefa(nome: str):
    fluxo["To Do"].append(nome)
    return {"mensagem": "Tarefa adicionada com sucesso"}

def mover_tarefa(nome: str, nova_coluna: str):
    for coluna in fluxo:
        if nome in fluxo[coluna]:
            fluxo[coluna].remove(nome)
            break
    if nova_coluna in fluxo:
        fluxo[nova_coluna].append(nome)
        return {"mensagem": f"Tarefa movida para '{nova_coluna}'"}
    return {"erro": "Coluna inválida"}
