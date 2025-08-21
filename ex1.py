import streamlit as st
st.title('우왕.')
st.write('hello everyone..')
st.title('재밌당.')

import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

# -------------------
# 페이지 배경 색상 변경
# -------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ADD8E6;  /* light sky blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Mendelian Genetics - Drosophila Eye Color Simulation 🪰")

# -------------------
# 부모 선택
# -------------------
st.header("1. Select Parent Chromosomes")

father = st.selectbox("Father (Male) ♂:", ["XᴳY", "XᵍY"])
mother = st.selectbox("Mother (Female) ♀:", ["XᴳXᴳ", "XᴳXᵍ", "XᵍXᵍ"])

# -------------------
# 표현형 판별 함수
# -------------------
def phenotype(genotype):
    if genotype in ["XᴳXᴳ", "XᴳXᵍ"]:
        return "Red Eyes ♀"
    elif genotype == "XᵍXᵍ":
        return "White Eyes ♀"
    elif genotype == "XᴳY":
        return "Red Eyes ♂"
    elif genotype == "XᵍY":
        return "White Eyes ♂"

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
# Punnett Square (2x2) - 영어로
# -------------------
square = [
    [eggs[0] + sperms[0], eggs[0] + sperms[1]],
    [eggs[1] + sperms[0], eggs[1] + sperms[1]],
]
df_square = pd.DataFrame(
    square,
    index=[f"Egg: {eggs[0]}", f"Egg: {eggs[1]}"],
    columns=[f"Sperm: {sperms[0]}", f"Sperm: {sperms[1]}"]
)

st.header("2. Punnett Square 🧬")
st.table(df_square)

# -------------------
# 이론적 표현형 비율
# -------------------
all_genos = [square[0][0], square[0][1], square[1][0], square[1][1]]
phenotypes_list = [phenotype(g) for g in all_genos]
expected = (pd.Series(phenotypes_list).value_counts(normalize=True) * 100).sort_index()

st.header("3. Theoretical Phenotype Ratio (%) 📊")
st.write(expected)

# 색상 지정
color_map = {"Red Eyes ♀": "red", "Red Eyes ♂": "red",
             "White Eyes ♀": "lightgray", "White Eyes ♂": "lightgray"}

fig, ax = plt.subplots()
bars = expected.plot(kind="bar", ax=ax, color=[color_map[x] for x in expected.index])
plt.ylabel("Ratio (%)")

# 막대 위에 비율 표시
for bar in bars.patches:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f"{bar.get_height():.1f}%", ha='center', va='bottom')

st.pyplot(fig)

# -------------------
# 시뮬레이션
# -------------------
st.header("4. Offspring Simulation 🎲")
simulate = st.radio("Do you want to simulate offspring? 🐞", ["No", "Yes"])
N = st.slider("Number of Offspring to Simulate (N)", min_value=10, max_value=5000, value=100, step=10)

if simulate == "Yes":
    sim_genos = []
    for _ in range(N):
        e = random.choice(eggs)
        s = random.choice(sperms)
        sim_genos.append(e + s)

    sim_phenos = [phenotype(g) for g in sim_genos]
    sim_counts = pd.Series(sim_phenos).value_counts().sort_index()

    st.subheader(f"Simulation Result (N={N}) 🐜")
    st.write(sim_counts)

    fig2, ax2 = plt.subplots()
    bars2 = sim_counts.plot(kind="bar", ax=ax2, color=[color_map[x] for x in sim_counts.index])
    plt.ylabel("Count")

    # 막대 위에 개체 수 표시
    for bar in bars2.patches:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f"{int(bar.get_height())}", ha='center', va='bottom')

    st.pyplot(fig2)

    # 비교
    sim_pct = (sim_counts / N * 100).reindex(expected.index).fillna(0)
    compare = pd.DataFrame({
        "Theoretical (%)": expected,
        f"Simulated (%) [N={N}]": sim_pct
    })
    st.subheader("Theoretical vs Simulated (%) ⚖️")
    st.dataframe(compare.round(2))

# -------------------
# 과학적 설명
# -------------------
st.header("5. Scientific Explanation 🧪")
st.markdown("""
- Drosophila eye color is **X-linked**, located on the X chromosome.  
- Red Eyes (Xᴳ) are dominant, White Eyes (Xᵍ) are recessive.  
- **Females (XX)** can be carriers, while **males (XY)** express the allele on their single X chromosome directly.  
- This explains why recessive traits (White Eyes) are more easily seen in males.  
""")