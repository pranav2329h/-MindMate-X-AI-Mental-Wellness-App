from textblob import TextBlob
import nltk
nltk.download('punkt')  # Only needs to run once

def analyze_mood(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity

    if score > 0.1:
        sentiment = 'positive'
    elif score < -0.1:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return sentiment, score
