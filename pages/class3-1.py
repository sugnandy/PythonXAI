import streamlit as st

st.title("點餐機")

ss = st.session_state

if "order" not in ss:
    ss.order = []

col1, col2 = st.columns([9, 1])
foodInput = col1.text_input("請輸入點餐")
if col2.button("加入"):
    ss.order.append(foodInput)
    st.rerun()

st.write("### 購物籃")
for i in range(len(ss.order)):
    col3, col4 = st.columns([9, 1])
    col3.write(ss.order[i])
    if col4.button("刪除", key=f"del{i}"):
        ss.order.pop(i)
        st.rerun()
