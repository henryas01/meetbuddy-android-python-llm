# from fastapi import FastAPI
# from ai.speaking import speaking_coach

# app = FastAPI()

# @app.post("/speak")
# def speak(text: str):
#     reply = speaking_coach(text)
#     return {
#         "reply": reply
#     }


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from api.routes import router

# app = FastAPI(title="LLM Conversation Backend")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:3000",
#         "http://127.0.0.1:3000"
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(router)


#  pahse 2

# import os
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles

# from api.routes import router

# os.makedirs("static", exist_ok=True)

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.mount("/static", StaticFiles(directory="static"), name="static")

# # 🔥 INI WAJIB
# app.include_router(router)

# @app.get("/")
# def root():
#     return {"status": "ok"}


# from fastapi import FastAPI, WebSocket
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# from api.ws_conversation import conversation_ws
# from utils.paths import TEMP_DIR

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.websocket("/ws/conversation")
# async def ws_conv(ws: WebSocket):
#     await conversation_ws(ws)

# app.mount(
#     "/temp",
#     StaticFiles(directory=str(TEMP_DIR), html=False),
#     name="temp"
# )

# from fastapi import FastAPI, WebSocket
# from api.ws_test_audio import ws_test_audio

# app = FastAPI()
# @app.websocket("/ws/test-audio")
# async def ws_audio(ws: WebSocket):
#     await ws_test_audio(ws)

from fastapi import FastAPI
from api.ws_conversation import conversation_ws
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_websocket_route("/ws/conversation", conversation_ws)

app.mount("/temp", StaticFiles(directory="temp"), name="temp")
