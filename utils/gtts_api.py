from gtts import gTTS
from asgiref.sync import sync_to_async as s2a
import os.path

def __generate_audio__(request_id: str, text: str, language: str):
    tts_module = gTTS(text=text, lang=language)
    audio_dir = "./audio"
    if not os.path.isdir(audio_dir):
        os.makedirs(audio_dir, exist_ok=True)
    tts_module.save(f"{audio_dir}/{request_id}.mp3")

    return f"./audio/{request_id}.mp3"

async def start_generate_audio(request_id: str, text: str, language: str):
    file = await s2a(__generate_audio__)(request_id, text, language)
    return file