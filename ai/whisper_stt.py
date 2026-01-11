# import whisper

# model = whisper.load_model("small")

# def transcribe(audio_path):
#     result = model.transcribe(audio_path)
#     return result["text"]


import tempfile
import subprocess
from fastapi import UploadFile

import subprocess

async def transcribe_audio(audio: UploadFile) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await audio.read())
        tmp_path = tmp.name

    result = subprocess.run(
        ["whisper", tmp_path, "--model", "base", "--language", "en", "--fp16", "False"],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()


def transcribe_audio_sync(path: str) -> str:
    result = subprocess.run(
        ["whisper", path, "--model", "base", "--language", "en", "--fp16", "False"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()