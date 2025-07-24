# 🎵 MoodTunes – AI Music Mood Recommender

**Turn Your Feelings Into Playlists**  
MoodTunes is a Flask-based web app that uses AI to detect a user's mood from text input and recommends music playlists that match the emotion.

---

## 🌟 Features

- 🧠 AI-powered sentiment/emotion analysis using scikit-learn & joblib
- 🎧 Spotify API integration to fetch relevant mood playlists
- 🔁 Fallback playlist recommender using CSV if Spotify fails
- 🌀 Similar Songs Clustering using KMeans
- 📱 Simple, responsive Flask + Bootstrap frontend

---

## 🛠 Tech Stack

- Python (Flask, pandas, scikit-learn, joblib)
- HTML/CSS + Bootstrap (Frontend)
- Spotipy (Spotify API integration)
- FAISS or KMeans for “Songs Like This”
- Deployed using **Render** or **Replit** (for Flask apps)

---

## 🚀 Deployment Link
https://moodtunes-yuq6.onrender.com
## 📂 Project Structure

```
├── app.py
├── mood_classifier.py
├── similar_songs.py
├── playlist_fallback.csv
├── emotion_model.pkl
├── vector.pkl
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── result.html
│   └── similar.html
└── static/
    └── style.css (optional)
```

---

## 👤 Author

Oyibo Praise-God (Praiztech)  
AI & Software Engineering – PLP 2025  
Project guided by Skye (ChatGPT)

---

## ✅ SDG Alignment

- **SDG 3**: Good Health and Well-being (emotional support via music)
- **SDG 9**: Industry, Innovation, and Infrastructure

---

## 📸 Screenshots
<img width="1889" height="652" alt="{DD47E719-2FB8-44F7-B7D8-053FCC69CF92}" src="https://github.com/user-attachments/assets/4937aa95-d762-490c-bb20-76e3e0bb0577" />


---

## 💡 License

MIT License – Free to use and modify
