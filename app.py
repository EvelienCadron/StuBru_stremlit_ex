import streamlit as st
import random
import json

# -----------------------------
# Tijdloze 100 – Minimal Dataset
# (You can expand this list)
# -----------------------------


@st.cache_data
def load_songs():
    with open("tijdloze100.json", "r", encoding="utf-8") as f:
        return json.load(f)

songs = load_songs()

st.title("🎸 Tijdloze Rock Suggestor")

if st.button("Geef mij een nummer!"):
    song = random.choice(songs)
    st.subheader(f"{song['title']} – {song['artist']}")
    st.caption(f"Album: {song.get('album', 'Onbekend')}")
    if song.get("cover_url"):
        st.image(song["cover_url"], width=300)



