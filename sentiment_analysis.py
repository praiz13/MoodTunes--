
from textblob import TextBlob

def get_emotion(text: str) -> str:
    """Return a simple emotion label based on TextBlob polarity."""
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.4:
        return "happy"
    elif polarity > 0.1:
        return "calm"
    elif polarity < -0.4:
        return "sad"
    elif polarity < -0.1:
        return "fearful"
    else:
        return "neutral"

if __name__ == "__main__":
    example = "I feel amazing today!"
    print(get_emotion(example))
