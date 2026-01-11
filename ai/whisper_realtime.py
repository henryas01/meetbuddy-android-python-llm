import whisper
import numpy as np
import soundfile as sf
import tempfile
import os

model = whisper.load_model("base")

def transcribe_chunk(audio_bytes: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        path = f.name

    result = model.transcribe(path, language="en", fp16=False)
    os.unlink(path)

    return result["text"].strip()
