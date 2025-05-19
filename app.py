from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from chat_model import query_llm
from tts import text_to_speech

app = FastAPI()

# Allow requests from all origins (helpful for frontend testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(input_text: str = Form(...)):
    """
    Handles chat input from the user.
    Returns the LLM response and audio file path.
    """
    response = query_llm(input_text)
    audio_file = text_to_speech(response)
    return {
        "response": response,
        "audio_path": "/audio"
    }

@app.get("/audio")
def get_audio():
    """
    Serves the latest generated MP3 audio file.
    """
    return FileResponse("output.mp3", media_type="audio/mpeg")
