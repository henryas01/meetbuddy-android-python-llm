import uuid
import os
import edge_tts

TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

async def text_to_speech(text: str) -> str:
    filename = f"{uuid.uuid4()}.wav"
    path = os.path.join(TEMP_DIR, filename)

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-JennyNeural"
    )
    await communicate.save(path)

    return path
