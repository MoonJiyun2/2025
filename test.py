
# streamlit_app.py
import streamlit as st
import requests
import time
import numpy as np
import matplotlib.pyplot as plt

st.title("GitHub 시뮬레이션 시각화")

# ---------------------------
# 1️⃣ GitHub에서 코드 가져오기
# ---------------------------
code_url = "https://raw.githubusercontent.com/USERNAME/REPO/BRANCH/simulation.py"
try:
    code = requests.get(code_url).text
    st.subheader("GitHub 코드 가져오기 성공!")
except:
    st.error("GitHub 코드 가져오기 실패")
    code = None

# ---------------------------
# 2️⃣ 코드 실행 (선택)
# ---------------------------
if code:
    try:
        exec(code)
        st.success("코드 실행 완료!")
    except Exception as e:
        st.error(f"코드 실행 중 오류: {e}")

# ---------------------------
# 3️⃣ 사전 렌더링 영상 재생
# ---------------------------
st.subheader("GitHub에 올린 mp4 영상 재생")
video_url = "https://raw.githubusercontent.com/USERNAME/REPO/BRANCH/simulation.mp4"
st.video(video_url)

# ---------------------------
# 4️⃣ 실시간 애니메이션 예시
# ---------------------------
st.subheader("실시간 애니메이션 예시 (영상처럼)")

placeholder = st.empty()
for i in range(50):
    x = np.linspace(0, 10, 100)
    y = np.sin(x + i / 5)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_ylim(-1, 1)

    placeholder.pyplot(fig)
    time.sleep(0.1)
