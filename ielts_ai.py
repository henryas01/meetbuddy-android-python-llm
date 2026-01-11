from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil

from ai.whisper_stt import transcribe
from ai.scoring import evaluate
from db.database import cursor, conn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/speaking")
async def speaking(
    audio: UploadFile,
    mode: str = "IELTS",
    style: str = "coach"
):
    audio_path = f"temp/{audio.filename}"
    with open(audio_path, "wb") as f:
        shutil.copyfileobj(audio.file, f)

    transcript = transcribe(audio_path)
    feedback = evaluate(transcript, mode, style)

    cursor.execute(
        "INSERT INTO sessions (mode, transcript, feedback) VALUES (?, ?, ?)",
        (mode, transcript, feedback)
    )
    conn.commit()

    return {
        "transcript": transcript,
        "feedback": feedback
    }
