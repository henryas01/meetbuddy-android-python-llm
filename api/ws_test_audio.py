from fastapi import WebSocket, WebSocketDisconnect
from ai.tts import text_to_speech
import traceback

async def ws_test_audio(ws: WebSocket):
    await ws.accept()
    print("WS CONNECTED")

    try:
        while True:
            data = await ws.receive_text()
            print("RECEIVED:", data)

            await ws.send_json({
                "type": "assistant_text",
                "text": "Hello, this is a test reply"
            })

            try:
                audio_path = await text_to_speech("Hello, this is a test reply")
                print("AUDIO GENERATED:", audio_path)

                await ws.send_json({
                    "type": "assistant_audio",
                    "audio": audio_path
                })

            except Exception:
                traceback.print_exc()
                await ws.send_json({
                    "type": "error",
                    "message": "TTS failed"
                })

    except WebSocketDisconnect:
        print("WS DISCONNECTED")
