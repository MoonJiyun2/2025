# streamlit_app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="GitHub 시뮬레이션 시각화", layout="wide")
st.title("GitHub 시뮬레이션 시각화 앱")

# ---------------------------
# 1️⃣ 사전 렌더링 영상 재생
# ---------------------------
st.subheader("GitHub에 올린 mp4 영상 재생")
video_url = "https://raw.githubusercontent.com/USERNAME/REPO/BRANCH/simulation.mp4"
st.video(video_url)

# ---------------------------
# 2️⃣ 실시간 애니메이션 예시
# ---------------------------
st.subheader("실시간 애니메이션 예시 (영상처럼)")

placeholder = st.empty()
for i in range(50):
    x = np.linspace(0, 10, 100)
    y = np.sin(x + i / 5)  # 예시: 사인파 시뮬레이션

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_ylim(-1, 1)
    ax.set_title(f"프레임 {i+1}")

    placeholder.pyplot(fig)
    time.sleep(0.1)
