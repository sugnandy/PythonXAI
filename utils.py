import streamlit as st
import base64


def load_openai_api() -> str:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    if not openai_api_key:
        st.error("請先在 Secrets 中填寫 OpenAI API 金鑰")
        st.stop()
    return openai_api_key


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
