## 🚀 TTS + Mistral AI Chat Application

A simple and interactive Text-to-Speech (TTS) + Mistral AI Chat application built using Streamlit.

This project uses pyttsx3 (offline TTS) for speech generation and Mistral AI API for AI chat responses.

## 📌 Features

# 🎤 Text-to-Speech (TTS):
```
Converts text into speech
Works offline using pyttsx3
Voice selection
Adjustable speech rate and volume
Downloadable audio file
```
# 🤖 Mistral AI Chat
```
Sends user prompts to Mistral AI API
Receives intelligent AI responses
Option to choose response format
```
## 📂 Project Structure
```
📁 TTS_AI API Integration
│── app.py
│── ai_client.py
│── tts_utils.py
│── logger_config.py
└── 📁tests
        │──test_validation.py

📄 requirements.txt      # outside folder  
📄 .env                  # outside folder
```
## 🔧 Installation & Setup

### ✅ 1. Create/Activate Virtual Environment
python -m venv venv
venv\Scripts\activate     # windows

### ✅ 2. Install Dependencies
Your requirements.txt is outside the folder, so install like this:
pip install -r requirements.txt

### ✅ 3. Add Your API Key
Create a .env file next to requirements.txt:

MISTRAL_API_KEY=your_api_key
MISTRAL_BASE_URL=https://api.mistral.ai/v1

*Make sure your code loads env path like this:
```
from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")  # since env is one level above
```
## ▶️ Running the App
streamlit run app.py

## 🛠️ requirements.txt
```
streamlit
python-dotenv
requests
pyttsx3
pydub
```
## 🧠 How the App Works

#### *TTS Module
```
.Accepts text
.Uses pyttsx3 engine
.Saves audio as .mp3
.Allows playback/download
```
#### *Mistral Chat Module
```
.Sends user text to Mistral API
.Returns formatted AI response
```
## 🖼️ Streamlit UI Sections

#### 🎤 TTS Section
```
.Enter text
.Choose voice
.Adjust speech rate/volume
.Generate & play speech
```
#### 🤖 AI Chat Section
```
.Enter prompt
.Choose response mode
.Receive AI answer instantly
```
## Example Output
### Login Page
![Login Page](output/code(1).png)

### Home Page
![Home Page](output/Home(2).png)

### Audio Page
![Audio Page](output/Audio(3).png)

### Mistral Prompt Page
![Values Page](output/mistral_prompt(4).png)

### Mistral Output Page
![Mistral Output Page](output/mistral_output(5).png)

### Mistral B/w Output Page
![Mistral B/w Output Page](output/output(6).png)

### Mistral end Output Page
![Mistral end Output Page](output/end_output(7).png)

### TTS - AI Output video
![TTS - AI Output video](output/output_video.mp4)

## 🙌 Author

Motupalli Jyothi Swaroop
AI & ML Developer
