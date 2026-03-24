# 🎙️ Empathy Engine – Giving AI a Human Voice

## 📌 Project Overview
The Empathy Engine is a system that converts plain text into emotionally expressive speech. Traditional Text-to-Speech (TTS) systems often sound robotic and lack emotional depth. This project aims to bridge that gap by dynamically modifying vocal parameters such as rate, volume, and pitch based on the detected emotion of the input text.

The goal is to make AI-generated voice sound more natural, engaging, and human-like, improving user experience in applications like customer support, virtual assistants, and AI-driven sales.

---

## 🎯 Problem Statement
Design and build a service that:
1. Accepts text input  
2. Detects emotion from the text  
3. Modifies speech characteristics accordingly  
4. Produces an audio output with emotional expression  

---

## ⚙️ Tech Stack
- Language: Python  
- Emotion Detection: TextBlob  
- Text-to-Speech: pyttsx3  
- Web Framework: Flask  

---

## 🧠 Approach

### Step 1: Text Input
The system accepts input through:
- CLI (Command Line Interface)  
- Web UI (Flask)  
- API endpoint  

---

### Step 2: Emotion Detection
We use TextBlob to compute sentiment polarity:

- Polarity > 0.3 → Happy  
- Polarity < -0.3 → Sad  
- Otherwise → Neutral  

We also use the polarity value as intensity.

---

### Step 3: Emotion-to-Voice Mapping

| Emotion  | Rate (Speed) | Volume | Pitch |
|----------|-------------|--------|-------|
| Happy    | Faster      | High   | Higher |
| Sad      | Slower      | Low    | Lower |
| Neutral  | Normal      | Medium | Default |

Additionally:
- Stronger sentiment → higher intensity → more variation  
- Example:  
  - "Good" → slight increase  
  - "This is the best news ever!" → large increase  

---

### Step 4: Voice Generation
We use pyttsx3 to:
- Convert text to speech  
- Modify rate, volume, and pitch  
- Save output as `.wav` file  

---

### Step 5: Output
The system generates:
- output.wav file  
- Playable audio in browser  

---

## ✅ Core Requirements Coverage

| Requirement | Status |
|------------|--------|
| Text Input | ✅ CLI + API + Web |
| Emotion Detection | ✅ 3 categories |
| Vocal Modulation | ✅ Rate, Volume, Pitch |
| Emotion Mapping | ✅ Implemented |
| Audio Output | ✅ WAV file |

---

## 🌟 Bonus Features Implemented

✔ Web Interface with audio player  
✔ Intensity-based modulation  
✔ User-controlled sliders (rate, volume, pitch)  
✔ API support  

---

## 🚀 How to Run

### 1. Clone Repository

git clone <your-repo-link>
cd empathy-engine


---

### 2. Install Dependencies

pip install -r requirements.txt


---

### 3. Download TextBlob Data

python -m textblob.download_corpora


---

### 4. Run the Application

python app.py


Choose mode:
- 1 → CLI  
- 2 → Web UI  
- 3 → API  

---

### 🌐 Web Interface
Open:

http://127.0.0.1:5000


---

### 🔗 API Example

POST /api/speak
{
"text": "I am very happy today!"
}


---

## 📂 Project Structure

empathy-engine/
│── app.py
│── emotion.py
│── tts_engine.py
│── requirements.txt
│── templates/
│ └── index.html
│── static/
│ └── output.wav


---

## ⚠️ Limitations
- Pitch control depends on system voice engine  
- pyttsx3 voices are less natural compared to cloud APIs  
- Emotion detection is basic (rule-based sentiment)  

---

## 🚧 Future Improvements
- Use HuggingFace models for better emotion detection  
- Integrate ElevenLabs / Google TTS for realistic voice  
- Add SSML support for pauses and emphasis  
- Improve UI with modern design  

---

## 🧪 Example Inputs & Behavior

| Input Text | Emotion | Behavior |
|-----------|--------|---------|
| "This is amazing!" | Happy | Faster, louder |
| "I am very disappointed" | Sad | Slower, softer |
| "This is a product" | Neutral | Normal |

---

## 🧠 Interview Explanation

### 🔹 Short Version
"I built an Empathy Engine that converts text into emotionally expressive speech by detecting sentiment and dynamically adjusting voice parameters like rate, volume, and pitch."

---

### 🔹 Detailed Version
"In this project, I designed a system that takes text input and analyzes its sentiment using TextBlob. Based on the detected emotion and its intensity, I map it to specific speech parameters such as rate, volume, and pitch. I then use pyttsx3 to generate speech output that reflects the emotional tone of the input. The system supports CLI, API, and a web interface, making it flexible and easy to use."

---

## 👨‍💻 Author
Snehal chowdary – Empathy Engine
