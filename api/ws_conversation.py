from fastapi import WebSocket, WebSocketDisconnect
from ai.whisper_rt import transcribe
from ai.ollama import chat
from ai.tts import text_to_speech
import traceback

async def conversation_ws(ws: WebSocket):
    await ws.accept()
    print("CONVERSATION WS CONNECTED")

    try:
        while True:
            data = await ws.receive_bytes()
            print("AUDIO BYTES:", len(data))

            user_text = transcribe(data)
            print("USER:", user_text)

            await ws.send_json({
                "type": "user_text",
                "text": user_text
            })

            reply_text, processing_time = chat(user_text)

            await ws.send_json({
                "type": "assistant_text",
                "text": reply_text,
                "time": processing_time
            })

            audio_path = await text_to_speech(reply_text)

            await ws.send_json({
                "type": "assistant_audio",
                "audio": audio_path
            })


    except WebSocketDisconnect:
        print("CONVERSATION WS DISCONNECTED")
    except Exception:
        traceback.print_exc()
