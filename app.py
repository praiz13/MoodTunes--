from flask import Flask, request, render_template
import joblib, pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from similar_songs import recommend_similar

app = Flask(__name__)

# ---------- Spotify credentials ----------
client_id = "a1fc2401783d46b0954e235ceb446f8d"
client_secret = "f73fb06bb65b4796be795029a0c4c0fa"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret))

# ---------- Load ML model & vectorizer ----------
model   = joblib.load("emotion_model.pkl")
vector  = joblib.load("vector.pkl")

# ---------- Load fallback CSV via pandas ----------
fallback_df = pd.read_csv("playlist_fallback.csv")

def predict_emotion(text: str) -> str:
    X = vector.transform([text])
    return model.predict(X)[0]

def get_spotify_playlists(mood, genre, limit=3):
    try:
        query = f"{mood} {genre}"
        results = sp.search(q=query, type='playlist', limit=limit)
        playlists = [
            {
                "name": item.get('name', 'No title'),
                "url": item.get('external_urls', {}).get('spotify', '#')
            }
            for item in results.get('playlists', {}).get('items', [])
            if item
        ]
        if playlists:
            return playlists
        raise Exception("Empty response")          # trigger fallback
    except Exception as e:
        print("⚠️  Spotify error:", e)
        # Fallback to CSV
        rows = fallback_df.query("mood == @mood and genre == @genre").head(3)
        return [{"name": row.track, "url": "#"} for _, row in rows.iterrows()]

# ---------- Routes ----------
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/similar/<song>')
def similar(song):
    recs = recommend_similar(song)
    return render_template("similar.html", base_song=song, recs=recs)




@app.route('/recommend', methods=['POST'])
def recommend():
    mood_text = request.form['mood']
    genre     = request.form['genre']
    emotion   = predict_emotion(mood_text)
    playlists = get_spotify_playlists(emotion, genre)
    return render_template("result.html",
                           emotion=emotion,
                           genre=genre,
                           playlists=playlists)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))  # default to 5000 for local dev
    app.run(debug=True, host='0.0.0.0', port=port)
