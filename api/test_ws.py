from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws/speak")
async def ws(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_text()
        await ws.send_text("pong")
