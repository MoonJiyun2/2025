import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

st.title("모건의 초파리 적안/백안 교배 실험 시뮬레이션")

# -------------------
# 부모 선택
# -------------------
st.header("1. 부모의 염색체를 선택하세요")

father = st.selectbox("부 (수컷):", ["XᴳY", "XᵍY"])
mother = st.selectbox("모 (암컷):", ["XᴳXᴳ", "XᴳXᵍ", "XᵍXᵍ"])

# -------------------
# 표현형 판별 함수
# -------------------
def phenotype(genotype):
    # 암컷
    if genotype in ["XᴳXᴳ", "XᴳXᵍ"]:
        return "적안 ♀"
    elif genotype == "XᵍXᵍ":
        return "백안 ♀"
    # 수컷
    elif genotype == "XᴳY":
        return "적안 ♂"
    elif genotype == "XᵍY":
        return "백안 ♂"

# -------------------
# 난자 / 정자 생성
# -------------------
if mother == "XᴳXᴳ":
    eggs = ["Xᴳ", "Xᴳ"]
elif mother == "XᴳXᵍ":
    eggs = ["Xᴳ", "Xᵍ"]
else:
    eggs = ["Xᵍ", "Xᵍ"]

sperms = ["Xᴳ","Y"] if father == "XᴳY" else ["Xᵍ","Y"]

# -------------------
# Punnett Square (2x2)
# -------------------
square = [
    [eggs[0] + sperms[0], eggs[0] + sperms[1]],
    [eggs[1] + sperms[0], eggs[1] + sperms[1]],
]
df_square = pd.DataFrame(
    square,
    index=[f"난자:{eggs[0]}", f"난자:{eggs[1]}"],
    columns=[f"정자:{sperms[0]}", f"정자:{sperms[1]}"]
)

st.header("2. Punnett Square 결과")
st.table(df_square)

# -------------------
# 이론적 표현형 비율
# -------------------
all_genos = [square[0][0], square[0][1], square[1][0], square[1][1]]
phenotypes = [phenotype(g) for g in all_genos]
expected = (pd.Series(phenotypes).value_counts(normalize=True) * 100).sort_index()

st.header("3. 이론적 표현형 비율 (퍼넷 스퀘어 기반)")
st.write(expected)

fig, ax = plt.subplots()
expected.plot(kind="bar", ax=ax)
plt.ylabel("비율 (%)")
st.pyplot(fig)

# -------------------
# 시뮬레이션
# -------------------
st.header("4. 자손 수 선택 & 시뮬레이션")
simulate = st.radio("“자손 생성 시뮬레이션”을 하겠습니까?", ["아니오", "네"])
N = st.slider("시뮬레이션 자손 수 (N)", min_value=10, max_value=5000, value=100, step=10)

if simulate == "네":
    # 자손 N마리 생성 (난자+정자 무작위 결합)
    sim_genos = []
    for _ in range(N):
        e = random.choice(eggs)
        s = random.choice(sperms)
        sim_genos.append(e + s)

    sim_phenos = [phenotype(g) for g in sim_genos]
    sim_counts = pd.Series(sim_phenos).value_counts().sort_index()

    st.subheader(f"시뮬레이션 결과 (N={N}) — 개체 수")
    st.write(sim_counts)

    fig2, ax2 = plt.subplots()
    sim_counts.plot(kind="bar", ax=ax2)
    plt.ylabel("개체 수")
    st.pyplot(fig2)

    # 이론값과 비교(퍼센트)
    sim_pct = (sim_counts / N * 100).reindex(expected.index).fillna(0)
    compare = pd.DataFrame({
        "이론값(%)": expected,
        f"시뮬(%) [N={N}]": sim_pct
    })
    st.subheader("이론값 vs 시뮬레이션(%) 비교")
    st.dataframe(compare.round(2))

# -------------------
# 과학적 설명 (추후 내용 추가 가능)
# -------------------
st.header("5. 과학적 지식 설명")
st.markdown("""
- 초파리의 눈 색깔은 **X 염색체에 위치한 유전자**에 의해 결정됩니다.  
- 적안(Xᴳ)은 우성, 백안(Xᵍ)은 열성입니다.  
- **암컷(XX)** 은 대립유전자가 2개이므로 보인자 개념이 존재하고,  
  **수컷(XY)** 은 X 하나만 가져 바로 표현형이 나타납니다.  
- 따라서 수컷에서 열성 형질(백안)이 더 쉽게 발현될 수 있습니다.  
""")