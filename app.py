import streamlit as st
import random

# -----------------------------
# Tijdloze 100 – Minimal Dataset
# (You can expand this list)
# -----------------------------
songs = [
    {
        "title": "Black",
        "artist": "Pearl Jam",
        "album": "Ten",
        "cover_url": "https://upload.wikimedia.org/wikipedia/en/2/2d/PearlJam-Ten2.jpg"
    },
    {
        "title": "Stairway to Heaven",
        "artist": "Led Zeppelin",
        "album": "Led Zeppelin IV",
        "cover_url": "https://upload.wikimedia.org/wikipedia/en/8/87/Led_Zeppelin_-_Led_Zeppelin_IV.jpg"
    },
    {
        "title": "Smells Like Teen Spirit",
        "artist": "Nirvana",
        "album": "Nevermind",
        "cover_url": "https://upload.wikimedia.org/wikipedia/en/b/b7/NirvanaNevermindalbumcover.jpg"
    },
    {
        "title": "Heroes",
        "artist": "David Bowie",
        "album": "Heroes",
        "cover_url": "https://upload.wikimedia.org/wikipedia/en/9/9d/David_Bowie_-_Heroes.png"
    },
    {
        "title": "One",
        "artist": "Metallica",
        "album": "...And Justice for All",
        "cover_url": "https://upload.wikimedia.org/wikipedia/en/2/2c/Metallica_-_...And_Justice_for_All_cover.jpg"
    },
    {
        "title": "Wish You Were Here",
        "artist": "Pink Floyd",
        "album": "Wish You Were Here",
        "cover_url": "https://upload.wikimedia.org/wikipedia/en/3/3b/Wish_You_Were_Here_%28Pink_Floyd_album%29.png"
    },
]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Tijdloze Rock Suggestor", page_icon="🎸")

st.title("🎸 Tijdloze 100 Rock Song Suggestor")
st.write("Klik op de knop voor een heerlijke rockklassieker uit de Tijdloze 100.")

if st.button("🎵 Geef mij een nummer!"):
    song = random.choice(songs)
    st.subheader(f"{song['title']} – {song['artist']}")
    st.caption(f"Album: *{song['album']}*")
    st.image(song["cover_url"], width=300)
