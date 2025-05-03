# Fluxo - Backend

Este repositório é dedicado ao desenvolvimento da API de 'Fluxo', como projeto de Sistemas Distribuídos. O Fluxo é uma aplicação construída para gerenciamento de tarefas.

Para iniciar o ambiente, instale as dependências:

## Configuração e Inicialização

```bash
pip install -r requirements.txt
```

Para iniciar o Uvicorn, com permissão para conexões externas:

```bash
uvicorn app.main:app --reload --host 0.0.0.0
```

## Websocket
Os endpoints de criação e modificação de tarefas emitem um alerta aos clientes conectados na rede, avisando-os da criação/modificação da tarefa.

## Exemplos de Operações com a API
1. **Listar todas as tarefas**
    - Método: `POST`
    - Endpoint: `/tarefas/ver-tarefas`
    - Descrição: Retorna uma lista com as tarefas cadastradas, conforme filtro desejado.

2. **Criar nova tarefa**
    - Método: `POST`
    - Endpoint: `/tarefas/create-tarefas`
    - Descrição: Cria nova tarefa com base no modelo de Tarefa.

3. **Mover tarefa para outro Status**
    - Método: `PUT`
    - Endpoint: `/tarefas/move-tarefas`
    - Descrição: Recebe o nome da tarefa e a atualiza conforme novo status dado.


4. **Editar tarefa**
    - Método: `PUT`
    - Endpoint: `/tarefas/edita-tarefas`
    - Descrição: Recebe o nome da tarefa e os dados que o cliente deseja editar.