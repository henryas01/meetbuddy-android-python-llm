from fastapi import (
    APIRouter,
    UploadFile,
    File,
    WebSocket,
    WebSocketDisconnect
)

from ai.speaking import speaking_coach
from ai.whisper_stt import transcribe_audio
from ai.tts import text_to_speech
from db.repository import create_session

import base64
import tempfile
import os


from fastapi import WebSocket, WebSocketDisconnect
from ai.whisper_realtime import transcribe_chunk
import base64

router = APIRouter()

# =========================
# SESSION
# =========================
@router.post("/session")
def create_new_session():
    return {"session_id": create_session()}

# =========================
# TEXT SPEAK (HTTP)
# =========================
@router.post("/speak")
def speak(session_id: str, text: str):
    return speaking_coach(session_id, text)

# =========================
# AUDIO SPEAK (HTTP)
# =========================
@router.post("/speak/audio")
async def speak_audio(
    session_id: str,
    audio: UploadFile = File(...)
):
    text = await transcribe_audio(audio)
    result = speaking_coach(session_id, text)
    audio_path = text_to_speech(result["reply"])

    return {
        "transcription": text,
        "reply": result["reply"],
        "audio": audio_path,
        "processing_time": result["processing_time_seconds"]
    }

# =========================
# REALTIME WEBSOCKET
# =========================
@router.websocket("/ws/speak")
async def ws_speak(ws: WebSocket):
    await ws.accept()

    try:
        while True:
            data = await ws.receive_json()

            session_id = data.get("session_id")
            msg_type = data.get("type")

            # ---------- TEXT ----------
            if msg_type == "text":
                result = speaking_coach(session_id, data["text"])
                audio_path = text_to_speech(result["reply"])

                await ws.send_json({
                    "type": "reply",
                    "text": result["reply"],
                    "audio": audio_path,
                    "time": result["processing_time_seconds"]
                })

            # ---------- AUDIO ----------
            elif msg_type == "audio":
                audio_bytes = base64.b64decode(data["audio"])

                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
                    f.write(audio_bytes)
                    temp_path = f.name

                # whisper → text
                text = transcribe_audio_sync(temp_path)
                os.unlink(temp_path)

                result = speaking_coach(session_id, text)
                audio_path = text_to_speech(result["reply"])

                await ws.send_json({
                    "type": "reply",
                    "transcription": text,
                    "text": result["reply"],
                    "audio": audio_path,
                    "time": result["processing_time_seconds"]
                })

    except WebSocketDisconnect:
        print("WebSocket disconnected")



@router.websocket("/ws/whisper")
async def ws_whisper(ws: WebSocket):
    await ws.accept()

    try:
        while True:
            data = await ws.receive_json()

            if data["type"] == "audio_chunk":
                audio_bytes = base64.b64decode(data["audio"])
                text = transcribe_chunk(audio_bytes)

                await ws.send_json({
                    "type": "partial",
                    "text": text
                })

    except WebSocketDisconnect:
        print("Whisper WS disconnected")
