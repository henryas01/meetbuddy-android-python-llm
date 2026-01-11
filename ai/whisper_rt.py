import subprocess
import tempfile
import whisper
import os

model = whisper.load_model("base")

def transcribe(audio_webm_bytes: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as webm:
        webm.write(audio_webm_bytes)
        webm_path = webm.name

    wav_path = webm_path.replace(".webm", ".wav")

    # 🔥 convert webm → wav
    subprocess.run([
        "ffmpeg", "-y",
        "-i", webm_path,
        "-ar", "16000",
        "-ac", "1",
        wav_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    result = model.transcribe(wav_path, language="en", fp16=False)

    os.remove(webm_path)
    os.remove(wav_path)

    return result["text"].strip()
