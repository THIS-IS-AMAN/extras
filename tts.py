

from gtts import gTTS

def text_to_speech(text: str, filename="output.mp3") -> str:
    """
    Converts text to speech and saves it as an MP3 file.
    Returns the filename.
    """
    try:
        tts = gTTS(text)
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"❌ TTS Error: {e}")
        return ""
