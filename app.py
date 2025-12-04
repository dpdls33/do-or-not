import streamlit as st
import random
import time

st.set_page_config(page_title="룰렛 돌리기", page_icon="🎡", layout="centered")

st.title("🎡 할까? 말까? 룰렛 돌리기 🎡")
st.write("아래 버튼을 눌러 룰렛을 돌려보세요!")

options = ["🙆 할래", "🙅 말래", "🤔 애매하긴해"]

# 룰렛 스타일
roulette_style = """
<style>
.result-box {
    font-size: 80px;
    font-weight: bold;
    color: #ff007f;
    text-align: center;
    padding: 20px;
    margin-top: 40px;
    animation: pop 0.5s ease-in-out;
}
@keyframes pop {
    0% {transform: scale(0.5); opacity: 0;}
    100% {transform: scale(1); opacity: 1;}
}
</style>
"""
st.markdown(roulette_style, unsafe_allow_html=True)

placeholder = st.empty()

if st.button("🎯 룰렛 돌리기!", use_container_width=True):
    # 룰렛 도는 애니메이션
    for _ in range(20):
        spin_choice = random.choice(options)
        placeholder.markdown(f"<h1 style='text-align:center;'>{spin_choice}</h1>", unsafe_allow_html=True)
        time.sleep(0.1)

    # 최종 결과
    result = random.choice(options)
    placeholder.markdown(
        f"<div class='result-box'>{result}</div>",
        unsafe_allow_html=True
    )
