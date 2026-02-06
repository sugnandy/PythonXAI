import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是 AI 的訊息")


#  範例對話紀錄
history = [
    {"role": "user", "content": "你好,AI!"},
    {"role": "assistant", "content": "我什麼可以幫忙的嗎?"},
    {"role": "user", "content": "請問 st.chat_message 怎麼用?"},
    {
        "role": "assistant",
        "content": "st.chat_message 用來顯示聊天訊息，可以指定角色為 user 或 assistant。",
    },
]


for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
