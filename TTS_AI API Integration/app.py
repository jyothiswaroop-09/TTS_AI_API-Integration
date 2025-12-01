import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path
from tts_utils import save_pyttsx3, save_gtts, list_pyttsx3_voices, validate_text
from ai_client import MistralClient, format_response

load_dotenv()

# Initialize Mistral Client
mistral_client = MistralClient()

st.title("TTS + Mistral AI Chat App 🚀")

# -------------------------
# TTS SECTION
# -------------------------
st.header("🗣️ Text-to-Speech (TTS)")

text = st.text_area("Enter text:", "Hello, welcome to the TTS demo!")

engine = st.selectbox("Choose TTS Engine:", ["pyttsx3 (offline)", "gTTS (online)"])

voices = list_pyttsx3_voices()
voice_names = [v["name"] for v in voices]
voice_selected = st.selectbox("Choose Voice (pyttsx3 only):", ["default"] + voice_names)

rate = st.slider("Speech Rate", 80, 300, 150)
volume = st.slider("Volume", 0.0, 1.0, 1.0)

if st.button("Generate Speech"):
    try:
        valid = validate_text(text)
        file_path = Path("generated_audio") / "output.mp3"
        file_path.parent.mkdir(exist_ok=True)

        # pyttsx3 TTS
        if engine.startswith("pyttsx3"):
            voice_id = None
            if voice_selected != "default":
                voice_id = next(v["id"] for v in voices if v["name"] == voice_selected)

            save_pyttsx3(valid, str(file_path), voice_id, rate, volume)
        else:
            save_gtts(valid, str(file_path))

        st.audio(str(file_path))
        st.success("Audio generated!")

    except Exception as e:
        st.error(f"Error: {e}")


# -------------------------
# AI CHAT SECTION (Mistral)
# -------------------------
st.header("🤖 Mistral AI Chat")

chat_input = st.text_input("Type your question")

format_choice = st.selectbox(
    "Response Format",
    ["normal", "bullet", "number"]
)

if st.button("Ask Mistral"):
    try:
        messages = [{"role": "user", "content": chat_input}]
        response = mistral_client.chat("mistral-small-latest", messages)

        output = response["choices"][0]["message"]["content"]
        formatted = format_response(output, format_choice)

        st.write("### AI Response:")
        st.write(formatted)

    except Exception as e:
        st.error(f"Chat Error: {e}")
