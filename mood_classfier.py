"""
mood_classifier.py
Train a simple Naive‑Bayes classifier that predicts an emotion
label (happy, sad, calm, fearful, neutral) from user text.
Saves the model to emotion_model.pkl and the vectorizer to vector.pkl
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# -------- Training data (tiny example; extend it for accuracy) -------
data = {
    "text": [
        "I feel great", "This is awesome",        # happy
        "I am joyful", "I'm very excited",
        "I feel sad", "I'm down",                 # sad
        "feeling depressed", "so unhappy",
        "I am calm", "Feeling relaxed",           # calm
        "peaceful vibes", "quite serene",
        "I'm scared", "I feel anxious",           # fearful
        "so nervous", "I am afraid",
        "Just normal", "I'm okay",                # neutral
        "nothing special", "fine, I guess"
    ],
    "label": [
        "happy","happy","happy","happy",
        "sad","sad","sad","sad",
        "calm","calm","calm","calm",
        "fearful","fearful","fearful","fearful",
        "neutral","neutral","neutral","neutral"
    ]
}
df = pd.DataFrame(data)

# -------- Vectorize & train -------
vec = CountVectorizer()
X = vec.fit_transform(df["text"])
y = df["label"]

model = MultinomialNB()
model.fit(X, y)

# -------- Persist assets -------
joblib.dump(model, "emotion_model.pkl")
joblib.dump(vec, "vector.pkl")

print("✅ Model and vectorizer saved.")
