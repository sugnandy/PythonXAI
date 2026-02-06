import streamlit as st
import openai
from utils import load_openai_api, encode_image

openai.api_key = load_openai_api()

st.title("AI 圖片分析")

uploaded_file = st.file_uploader("請上傳圖片檔案", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="已上傳的圖片", width=300)

    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    base64_image = encode_image("temp_image.jpg")

    prompt = st.chat_input("請輸入想要對話訊息")
    if prompt:
        response = openai.chat.completions.create(
            model="gpt-5.1-chat-latest",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt,
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                },
            ],
        )

        assistant_message = response.choices[0].message.content
        st.write(assistant_message)
