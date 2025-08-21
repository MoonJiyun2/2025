


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
st.title("토머스 모건의 초파리 적안/백안 교배 실험 시뮬레이션 🪰")

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

st.header("2. 퍼넷 스퀘어 🧬")
st.table(df_square)

# -------------------
# 자손 성별과 표현형 계산 함수
# -------------------
def get_offspring(father_sperm, mother_egg, N):
    offspring = []
    for _ in range(N):
        egg = random.choice(mother_egg)
        sperm = random.choice(father_sperm)
        child_genotype = egg + sperm
        # 성별 판정
        sex = "♀" if (egg == "Xᴳ" or egg == "Xᵍ") and sperm == "Xᴳ" or sperm == "Xᵍ" else "♂"
        # 표현형 판정
        if sex == "♀":
            pheno = "적안 ♀" if "Xᴳ" in child_genotype else "백안 ♀"
        else:
            pheno = "적안 ♂" if "Xᴳ" in child_genotype else "백안 ♂"
        offspring.append(pheno)
    return offspring

# -------------------
# 성별별 비율 계산 함수
# -------------------
def calc_ratio(lst, labels):
    total = len(lst)
    counts = {label: 0 for label in labels}
    for item in lst:
        if item in counts:
            counts[item] += 1
    ratio = {k: (v/total*100 if total>0 else 0) for k,v in counts.items()}
    return ratio

# -------------------
# 이론적 4개 조합 시 비율 계산
# -------------------
theory_offspring = get_offspring(sperms, eggs, 4)
female_theory = [p for p in theory_offspring if "♀" in p]
male_theory = [p for p in theory_offspring if "♂" in p]

female_ratio = calc_ratio(female_theory, ["적안 ♀","백안 ♀"])
male_ratio = calc_ratio(male_theory, ["적안 ♂","백안 ♂"])

st.header("3. 이론적 성별별 표현형 비율 📊")
st.write(f"암컷 ♀: 백안 {female_ratio['백안 ♀']:.1f}%, 적안 {female_ratio['적안 ♀']:.1f}%")
st.write(f"수컷 ♂: 백안 {male_ratio['백안 ♂']:.1f}%, 적안 {male_ratio['적안 ♂']:.1f}%")



# -------------------
# 과학적 설명
# -------------------
st.header("5. 배경지식 🧪")
st.markdown("""
- **토머스 헌트 모건의 초파리 실험 🪰**
  
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
