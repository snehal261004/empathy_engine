from textblob import TextBlob

def detect_emotion(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.3:
        return "happy", polarity
    elif polarity < -0.3:
        return "sad", polarity
    else:
        return "neutral", polarity