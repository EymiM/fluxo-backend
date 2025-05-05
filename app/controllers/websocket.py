from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(prefix="/api")

active_connections: list[WebSocket] = []

async def broadcast_message(message: str):
    for connection in active_connections:
        try:
            await connection.send_text(message)
        except:
            # Se falhar ao enviar para um cliente, remove a conexão
            active_connections.remove(connection)

@router.websocket("/ws/alerta")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Faz broadcast da mensagem para todos os clientes
            await broadcast_message(data)
    except WebSocketDisconnect:
        active_connections.remove(websocket)
    except Exception as e:
        print(f"Error: {e}")
        active_connections.remove(websocket)
