import streamlit as st

upload_file = st.file_uploader("上傳檔案", type=["png", "jpg", "jpeg"])

if upload_file:
    st.image(upload_file, caption="已上傳的圖片", width=300)
