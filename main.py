# streamlit run main.py
import streamlit as st

st.set_page_config(page_title="我的第一個網站", page_icon="🏠", layout="wide")

all_pages = {
    "": [
        st.Page("pages/hand_book.py", title="課程筆記", icon="📖"),
    ],
    "📚 程式練習": [
        st.Page("pages/class1-2.py", title="Markdown語法", icon="📝"),
        st.Page("pages/class2-1.py", title="成績等第判斷", icon="📊"),
        st.Page("pages/class2-3.py", title="金字塔系列", icon="🔺"),
        st.Page("pages/class2-7.py", title="排版練習", icon="🎨"),
        st.Page("pages/class3-1.py", title="點餐機", icon="🍔"),
        st.Page("pages/class3-5.py", title="猜數字遊戲", icon="🎲"),
        st.Page("pages/class4-1.py", title="圖片元件", icon="🖼️"),
        st.Page("pages/class4-2.py", title="購物平台", icon="🛒"),
        st.Page("pages/class5-4.py", title="聊天機器人", icon="🤖"),
        st.Page("pages/class5-5.py", title="對話輸入", icon="💬"),
        st.Page("pages/class5-6.py", title="對話AI機器人", icon="🧠"),
        st.Page("pages/class5-7.py", title="圖片上傳", icon="📤"),
        st.Page("pages/class5-8.py", title="圖片辨識", icon="🔎"),
        st.Page("pages/class5-9.py", title="網頁載入動畫", icon="🔎"),
        st.Page("pages/class5-10.py", title="AI 圖片生成", icon="🔎"),
    ],
}

nav = st.navigation(all_pages, position="sidebar")
nav.run()
