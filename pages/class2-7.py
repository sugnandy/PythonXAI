import streamlit as st

st.title("排版練習")

col1, col2 = st.columns(2)
if col1.button("氣球按鈕"):
    col1.balloons()
if col2.button("雪花按鈕"):
    col2.snow()

col3, col4, col5 = st.columns([1, 2, 3])
with col3:
    st.write("這在col3")
    st.button("按鈕3")
with col4:
    st.write("這在col4")
    st.button("按鈕4")
with col5:
    st.write("這在col5")
    st.button("按鈕5")

numCol = st.number_input("請輸入欄位數量", min_value=1, max_value=5, value=3, step=1)
numButton = st.number_input("請輸入按鈕數量", min_value=1, value=10, step=1)
cols = st.columns(numCol)
buttons = st.columns(numButton)
for i in range(numButton):
    cols[i % numCol].button(f"按鈕[{i+1}]")

st.title("文字輸入元件")
text = st.text_input("請輸入文字")
st.write("你輸入的文字是：", text)
