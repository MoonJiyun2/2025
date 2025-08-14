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
        ("Counting Stars", "OneRepublic", "https://youtu.be/hT_nvWreIhg", "https://img.youtube.com/vi/hT_nvWreIhg/0.jpg")
    ],
    "ENFP": [
        ("Happy", "Pharrell Williams", "https://youtu.be/ZbZSe6N_BXs", "https://img.youtube.com/vi/ZbZSe6N_BXs/0.jpg"),
        ("Shake It Off", "Taylor Swift", "https://youtu.be/nfWlot6h_JM", "https://img.youtube.com/vi/nfWlot6h_JM/0.jpg")
    ],
    "ISTJ": [
        ("Eye of the Tiger", "Survivor", "https://youtu.be/btPJPFnesV4", "https://img.youtube.com/vi/btPJPFnesV4/0.jpg"),
        ("In the End", "Linkin Park", "https://youtu.be/eVTXPUF4Oz4", "https://img.youtube.com/vi/eVTXPUF4Oz4/0.jpg")
    ],
    "ISFJ": [
        ("Perfect", "Ed Sheeran", "https://youtu.be/2Vv-BfVoq4g", "https://img.youtube.com/vi/2Vv-BfVoq4g/0.jpg"),
        ("Photograph", "Ed Sheeran", "https://youtu.be/nSDgHBxUbVQ", "https://img.youtube.com/vi/nSDgHBxUbVQ/0.jpg")
    ],
    "ESTJ": [
        ("We Will Rock You", "Queen", "https://youtu.be/-tJYN-eG1zk", "https://img.youtube.com/vi/-tJYN-eG1zk/0.jpg"),
        ("Thunderstruck", "AC/DC", "https://youtu.be/v2AC41dglnM", "https://img.youtube.com/vi/v2AC41dglnM/0.jpg")
    ],
    "ESFJ": [
        ("All of Me", "John Legend", "https://youtu.be/450p7goxZqg", "https://img.youtube.com/vi/450p7goxZqg/0.jpg"),
        ("Love Story", "Taylor Swift", "https://youtu.be/8xg3vE8Ie_E", "https://img.youtube.com/vi/8xg3vE8Ie_E/0.jpg")
    ],
    "ISTP": [
        ("Believer", "Imagine Dragons", "https://youtu.be/7wtfhZwyrcc", "https://img.youtube.com/vi/7wtfhZwyrcc/0.jpg"),
        ("Whatever It Takes", "Imagine Dragons", "https://youtu.be/gOsM-DYAEhY", "https://img.youtube.com/vi/gOsM-DYAEhY/0.jpg")
    ],
    "ISFP": [
        ("Stay With Me", "Sam Smith", "https://youtu.be/pB-5XG-DbAA", "https://img.youtube.com/vi/pB-5XG-DbAA/0.jpg"),
        ("When I Was Your Man", "Bruno Mars", "https://youtu.be/ekzHIouo8Q4", "https://img.youtube.com/vi/ekzHIouo8Q4/0.jpg")
    ],
    "ESTP": [
        ("Can't Stop the Feeling!", "Justin Timberlake", "https://youtu.be/ru0K8uYEZWw", "https://img.youtube.com/vi/ru0K8uYEZWw/0.jpg"),
        ("Don't Stop Me Now", "Queen", "https://youtu.be/HgzGwKwLmgM", "https://img.youtube.com/vi/HgzGwKwLmgM/0.jpg")
    ],
    "ESFP": [
        ("Levitating", "Dua Lipa", "https://youtu.be/TUVcZfQe-Kw", "https://img.youtube.com/vi/TUVcZfQe-Kw/0.jpg"),
        ("Dance Monkey", "Tones and I", "https://youtu.be/q0hyYWKXF0Q", "https://img.youtube.com/vi/q0hyYWKXF0Q/0.jpg")
    ],
}

# 🌟 제목
st.markdown("<h1 style='text-align:center;'>🎧 MBTI 음악 추천기 🎵</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>✨ 당신의 성격에 딱 맞는 노래를 찾아드릴게요! ✨</h3>", unsafe_allow_html=True)
st.write(" ")

# 📌 MBTI 선택
mbti = st.selectbox("💡 당신의 MBTI를 선택해주세요!", list(music_data.keys()))

# 🎁 추천 버튼
if st.button("🚀 음악 추천받기 🎶"):
    song = random.choice(music_data[mbti])
    title, artist, url, cover = song

    # 결과 출력
    st.success(f"🌟 {mbti} 타입의 당신에게 추천하는 노래는... 🌟")
    st.image(cover, caption=f"{title} - {artist}", use_column_width=True)
    st.markdown(f"**🎵 {title}** - *{artist}*")
    st.markdown(f"[🔥 유튜브에서 바로 듣기]({url})")
    st.balloons()

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center;'>💖 Created with Streamlit 💖</p>", unsafe_allow_html=True)
