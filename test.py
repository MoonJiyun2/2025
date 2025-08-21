


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
### 🔬 모건의 초파리 실험 (X-연관 유전)

#### 🪰 왜 초파리인가?
- 짧은 생식 주기 (~10일)
- 많은 자손
- 눈 색깔, 날개 모양 등 뚜렷한 형질 👀

---

#### 🧬 실험 과정
1. **적안 ♀ × 백안 ♂ 교배**
   - F1 세대 → 모두 적안  
   - → **적안이 우성임을 확인**

2. **F1 × F1 교배**
   - F2 세대에서 **백안이 수컷 ♂에게만 나타남**
   - 암컷 ♀은 모두 적안 또는 보인자(보균자)

---

#### 📌 결론
- **백안(Xᵍ)** : X 염색체 열성 유전자  
- **적안(Xᴳ)** : X 염색체 우성 유전자  
- 수컷(XY): X 하나만 있어도 백안 표현 → **열성 형질 잘 드러남**  
- 암컷(XX): X 두 개라서 보균자 가능

---

#### 🌍 의의
- 백안이 **X 염색체에 위치한 유전자**임을 최초로 증명  
- 성별과 유전 형질이 연결됨을 밝힘 
- 반성유전을 밝힘

""")

