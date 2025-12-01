import pyttsx3
from gtts import gTTS
import re
from pathlib import Path

def validate_text(text: str, max_len: int = 5000) -> str:
    if not isinstance(text, str):
        raise ValueError("Text must be a string.")
    txt = text.strip()
    if len(txt) == 0:
        raise ValueError("Text is empty after trimming.")
    if len(txt) > max_len:
        raise ValueError(f"Text too long (> {max_len} chars).")
    txt = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', txt)
    return txt

def save_pyttsx3(text: str, filename: str, voice_id: str = None, rate: int = 150, volume: float = 1.0):
    text = validate_text(text)
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', max(0.0, min(1.0, volume)))
    if voice_id:
        engine.setProperty('voice', voice_id)
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    engine.save_to_file(text, filename)
    engine.runAndWait()

def list_pyttsx3_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    out = []
    for v in voices:
        lang = getattr(v, 'languages', None)
        if isinstance(lang, (list, tuple)) and len(lang) > 0:
            try:
                lang = [l.decode() if isinstance(l, bytes) else l for l in lang]
            except Exception:
                pass
        out.append({"id": v.id, "name": v.name, "lang": lang})
    return out

def save_gtts(text: str, filename: str, lang: str='en', slow: bool=False):
    text = validate_text(text)
    tts = gTTS(text=text, lang=lang, slow=slow)
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    tts.save(filename)
