from flask import Flask, render_template, request, jsonify, send_file
from emotions import detect_emotion
from tts_engine import speak_with_emotion

app = Flask(__name__)

# ---------------- CLI MODE ----------------
def run_cli():
    text = input("Enter text: ")

    emotion, intensity = detect_emotion(text)

    print(f"Detected Emotion: {emotion}")
    print(f"Intensity: {intensity}")

    file = speak_with_emotion(text, emotion, abs(intensity))

    print(f"Audio saved at: {file}")


# ---------------- WEB UI ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]

        emotion, intensity = detect_emotion(text)
        file = speak_with_emotion(text, emotion, abs(intensity))

        return render_template(
            "index.html",
            audio_file=file,
            emotion=emotion
        )

    return render_template("index.html")


# ---------------- API ----------------
@app.route("/api/speak", methods=["POST"])
def api_speak():
    data = request.json
    text = data.get("text", "")

    emotion, intensity = detect_emotion(text)
    file = speak_with_emotion(text, emotion, abs(intensity))

    return jsonify({
        "emotion": emotion,
        "audio_file": file
    })


@app.route("/api/audio")
def get_audio():
    return send_file("static/output.wav", as_attachment=False)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    choice = input("Choose mode:\n1 = CLI\n2 = Web UI\n3 = API\nEnter: ")

    if choice == "1":
        run_cli()
    elif choice == "2":
        app.run(debug=True)
    elif choice == "3":
        app.run(debug=True)