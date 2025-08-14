import streamlit as st
import random

st.set_page_config(page_title="🎧 MBTI 음악 추천기", page_icon="🎵", layout="centered")

# 🎵 MBTI별 음악 데이터 (제목, 아티스트, URL, 앨범커버)
music_data = {
    "INTJ": [
        ("Numb", "Linkin Park", "https://youtu.be/kXYiU_JCYtU", "https://img.youtube.com/vi/kXYiU_JCYtU/0.jpg"),
        ("Somewhere I Belong", "Linkin Park", "https://youtu.be/zsCD5XCu6CM", "https://img.youtube.com/vi/zsCD5XCu6CM/0.jpg")
    ],
    "INTP": [
        ("Clocks", "Coldplay", "https://youtu.be/d020hcWA_Wg", "https://img.youtube.com/vi/d020hcWA_Wg/0.jpg"),
        ("Viva La Vida", "Coldplay", "https://youtu.be/dvgZkm1xWPE", "https://img.youtube.com/vi/dvgZkm1xWPE/0.jpg")
    ],
    "ENTJ": [
        ("Stronger", "Kanye West", "https://youtu.be/PsO6ZnUZI0g", "https://img.youtube.com/vi/PsO6ZnUZI0g/0.jpg"),
        ("Can't Hold Us", "Macklemore & Ryan Lewis", "https://youtu.be/2zNSgSzhBfM", "https://img.youtube.com/vi/2zNSgSzhBfM/0.jpg")
    ],
    "ENTP": [
        ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "https://youtu.be/OPf0YbXqDm0", "https://img.youtube.com/vi/OPf0YbXqDm0/0.jpg"),
        ("Sugar", "Maroon 5", "https://youtu.be/09R8_2nJtjg", "https://img.youtube.com/vi/09R8_2nJtjg/0.jpg")
    ],
    "INFJ": [
        ("Yellow", "Coldplay", "https://youtu.be/yKNxeF4KMsY", "https://img.youtube.com/vi/yKNxeF4KMsY/0.jpg"),
        ("Fix You", "Coldplay", "https://youtu.be/k4V3Mo61fJM", "https://img.youtube.com/vi/k4V3Mo61fJM/0.jpg")
    ],
    "INFP": [
        ("Lost Stars", "Adam Levine", "https://youtu.be/cL4uhaQ58Rk", "https://img.youtube.com/vi/cL4uhaQ58Rk/0.jpg"),
        ("Let Her Go", "Passenger", "https://youtu.be/RBumgq5yVrA", "https://img.youtube.com/vi/RBumgq5yVrA/0.jpg")
    ],
    "ENFJ": [
        ("Hall of Fame", "The Script ft. will.i.am", "https://youtu.be/mk48xRzuNvA", "https://img.youtube.com/vi/mk48xRzuNvA/0.jpg"),
        ("Counting Stars", "OneRepubl
