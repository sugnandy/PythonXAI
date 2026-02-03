import streamlit as st

st.title("數字輸入練習")
number = st.number_input(
    "請輸入一個數字", min_value=0, max_value=1000, value=50, step=1
)
st.write(f"你輸入的數字是: {number}")

st.title("成績等第判斷")
score = st.number_input("請輸入成績", min_value=0, max_value=100, value=90, step=1)
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "F"
elif score >= 40:
    grade = "傻逼"
elif score >= 20:
    grade = "垃圾"
elif score >= 10:
    grade = "弱智"
else:
    grade = "白痴"
st.write(f"你的成績等第是: {grade}")

st.title("氣球按鈕")
if st.button("點我"):
    st.balloons()


st.title("下雪按鈕")
if st.button("點擊我"):
    st.snow()
