
import streamlit as st

# 앱 제목
st.title("🎵 MBTI 기반 음악 추천 웹사이트")

# 데이터
music_data = {
    "INTJ": [("Numb", "Linkin Park", "https://youtu.be/kXYiU_JCYtU")],
    "ENFP": [("Happy", "Pharrell Williams", "https://youtu.be/ZbZSe6N_BXs")],
    "ISTP": [("Believer", "Imagine Dragons", "https://youtu.be/7wtfhZwyrcc")],
    "INFJ": [("Yellow", "Coldplay", "https://youtu.be/yKNxeF4KMsY")],
    # MBTI 16가지 전부 채워넣기
}

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요", list(music_data.keys()))

# 버튼
if st.button("음악 추천받기"):
    songs = music_data[mbti]
    st.subheader(f"{mbti}에게 어울리는 음악 🎶")
    for title, artist, url in songs:
        st.write(f"**{title}** - {artist}")
        st.markdown(f"[유튜브에서 듣기]({url})")
