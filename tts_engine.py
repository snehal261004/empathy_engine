import pyttsx3
import os

OUTPUT_FILE = "static/output.wav"

def speak_with_emotion(text, emotion, intensity=0.5):
    engine = pyttsx3.init()

    # Default values
    rate = 170
    volume = 0.9

    # Emotion mapping
    if emotion == "happy":
        rate = int(170 + 60 * intensity)
        volume = 1.0

    elif emotion == "sad":
        rate = int(170 - 60 * intensity)
        volume = 0.7

    elif emotion == "neutral":
        rate = 170
        volume = 0.9

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    # Ensure static folder exists
    os.makedirs("static", exist_ok=True)

    engine.save_to_file(text, OUTPUT_FILE)
    engine.runAndWait()

    return OUTPUT_FILE