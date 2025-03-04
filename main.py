from fastapi import FastAPI
from fastapi.responses import FileResponse, Response, HTMLResponse, JSONResponse
from utils.gtts_api import start_generate_audio
from pydantic import BaseModel
from pathlib import Path

class AudioRequest(BaseModel):
    request_id: str
    text: str
    language: str


def read_file(fileName):
    path = Path("htmls") / fileName
    return path.read_text()

app = FastAPI()

@app.exception_handler(404)
async def not_found(request, exc):
    return HTMLResponse(content=read_file("404.html"), status_code=404)

@app.exception_handler(500)
async def internal_error(request, exc):
    return HTMLResponse(content=read_file("500.html"), status_code=500)

@app.exception_handler(405)
async def method_not_allowed(request, exc):
    return HTMLResponse(content=read_file("405.html"), status_code=405)

@app.get("/")
async def home():
    return JSONResponse(content={"message": "Hello world!, this code is written by Shindou Aris",
                                    "version": "0.0.1 pre-release beta pro max",
                                    "source_code": "https://github.com/ShindouAris/the_most_stupid_rest_api_that_i_ever_made.git"})


@app.post("/generate_audio")
async def generate_audio(audio_request: AudioRequest):

    if not any([audio_request.request_id, audio_request.text, audio_request.language]):
        return Response(status_code=400, content="Invaild request")

    file = await start_generate_audio(audio_request.request_id, audio_request.text, audio_request.language)
    return FileResponse(file, media_type="audio/mpeg")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)