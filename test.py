import streamlit as st
import pandas as pd
import random

# -------------------
# 페이지 배경 색상 변경
# -------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ADD8E6;  /* 연하늘색 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------
# 제목
# -------------------
st.title("멘델 유전법칙 - 초파리 눈 색깔 시뮬레이션 🪰")

# -------------------
# 유전자 안내
# -------------------
st.markdown("""
### 🧬 유전자 안내
- **적안 (Red, Xᴳ)** : 우성 유전자  
- **백안 (White, Xᵍ)** : 열성 유전자
""")

# -------------------
# 부모 선택
# -------------------
st.header("1. 부모 염색체 선택")
father = st.selectbox("아버지 ♂:", ["XᴳY", "XᵍY"])
mother = st.selectbox("어머니 ♀:", ["XᴳXᴳ", "XᴳXᵍ", "XᵍXᵍ"])

# -------------------
# 표현형 판별 함수
# -------------------
def phenotype(genotype):
    if genotype in ["XᴳXᴳ", "XᴳXᵍ"]:
        return "적안 ♀"
    elif genotype == "XᵍXᵍ":
        return "백안 ♀"
    elif genotype == "XᴳY":
        return "적안 ♂"
    elif genotype == "XᵍY":
        return "백안 ♂"
    else:
        return "알 수 없음"

# -------------------
# 난자 / 정자 생성
# -------------------
if mother == "XᴳXᴳ":
    eggs = ["Xᴳ", "Xᴳ"]
elif mother == "XᴳXᵍ":
    eggs = ["Xᴳ", "Xᵍ"]
else:
    eggs = ["Xᵍ", "Xᵍ"]

sperms = ["Xᴳ", "Y"] if father == "XᴳY" else ["Xᵍ", "Y"]

# -------------------
# 펀넷 스퀘어 생성
# -------------------
square = [
    [eggs[0] + sperms[0], eggs[0] + sperms[1]],
    [eggs[1] + sperms[0], eggs[1] + sperms[1]],
]
df_square = pd.DataFrame(
    square,
    index=[f"난자: {eggs[0]}", f"난자: {eggs[1]}"],
    columns=[f"정자: {sperms[0]}", f"정자: {sperms[1]}"]
)

st.header("2. 펀넷 스퀘어 🧬")
st.table(df_square)

# -------------------
# 성별별 표현형 비율 계산
# -------------------
all_genos = [square[0][0], square[0][1], square[1][0], square[1][1]]
phenotypes_list = [phenotype(g) for g in all_genos]

# 성별별 분류
female_phenos = [p for p in phenotypes_list if "♀" in p]
male_phenos = [p for p in phenotypes_list if "♂" in p]

# 비율 계산
def calc_ratio(lst, labels):
    total = len(lst)
    counts = {label: 0 for label in labels}
    for item in lst:
        if item in counts:
            counts[item] += 1
    # 비율 %
    ratio = {k: (v/total*100 if total>0 else 0) for k,v in counts.items()}
    return ratio

female_ratio = calc_ratio(female_phenos, ["적안 ♀","백안 ♀"])
male_ratio = calc_ratio(male_phenos, ["적안 ♂","백안 ♂"])

st.header("3. 이론적 성별별 표현형 비율 📊")
st.write(f"암컷 ♀: 백안 {female_ratio['백안 ♀']:.1f}%, 적안 {female_ratio['적안 ♀']:.1f}%")
st.write(f"수컷 ♂: 백안 {male_ratio['백안 ♂']:.1f}%, 적안 {male_ratio['적안 ♂']:.1f}%")

# -------------------
# 자손 시뮬레이션
# -------------------
st.header("4. 자손 생성 시뮬레이션 🎲")
simulate = st.radio("자손을 시뮬레이션 하시겠습니까? 🐞", ["아니오", "예"])
N = st.slider("시뮬레이션할 자손 수 (N)", min_value=10, max_value=5000, value=100, step=10)

if simulate == "예":
    sim_genos = [random.choice(eggs)+random.choice(sperms) for _ in range(N)]
    sim_phenos = [phenotype(g) for g in sim_genos]
    
    female_sim = [p for p in sim_phenos if "♀" in p]
    male_sim = [p for p in sim_phenos if "♂" in p]

    female_sim_ratio = calc_ratio(female_sim, ["적안 ♀","백안 ♀"])
    male_sim_ratio = calc_ratio(male_sim, ["적안 ♂","백안 ♂"])

    st.subheader(f"시뮬레이션 결과 (N={N}) 🐜")
    st.write(f"암컷 ♀: 백안 {female_sim_ratio['백안 ♀']:.1f}%, 적안 {female_sim_ratio['적안 ♀']:.1f}%")
    st.write(f"수컷 ♂: 백안 {male_sim_ratio['백안 ♂']:.1f}%, 적안 {male_sim_ratio['적안 ♂']:.1f}%")

# -------------------
# 과학적 설명
# -------------------
st.header("5. 과학적 설명 🧪")
st.markdown("""
- **토마스 헌트 모건의 초파리 실험 🪰**
  
- **배경:**  
  - 모건은 초파리(Drosophila melanogaster)를 이용하여 동물에서 유전법칙을 연구함  
  - 초파리를 선택한 이유:  
    - 짧은 생식 주기 (~10일)  
    - 많은 자손  
    - 눈 색깔, 날개 모양 등 뚜렷한 형질 👀

- **실험 목표:**  
  - 특정 형질이 성염색체(X 염색체)와 관련되어 유전되는지 확인  
  - 초기 관찰 형질: 적안 vs 백안 👁️

- **교배 과정:**  
  1. 적안 ♀ × 백안 ♂ 교배  
  2. F1 세대: 모든 자손 적안 → **우성 확인**  
  3. F1 × F1 교배 → F2 세대: 백안은 **남성 ♂에게만 나타남**  
     - 여성 ♀은 적안 또는 보균자 🔴⚪  
     → **반성유전 확인**

- **결론:**  
  - 백안은 **X 염색체 열성 유전자**  
  - 남성(XY)은 단일 X 염색체 때문에 열성 표현형이 쉽게 나타남  
  - 여성(XX)은 하나만 있어도 보균자

- **의의:**  
  - 초파리는 **X-연관 유전 연구 모델**이 됨  
  - 성별과 유전 형질의 관계를 최초로 증명  
  - 멘델 법칙을 **염색체 수준에서 확인**
""")
