import openai  # pip install openai
from dotenv import load_dotenv
import os

load_dotenv()  # 讀取 .env 檔案中的環境變數

# 設定 API 金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    user_input = input("你:")  # 終端機輸入使用者訊息
    if user_input.lower() in ["exit", "quit"]:
        break

    response = openai.chat.completions.create(
        model="gpt-5.1-chat-latest",
        messages=[
            {"role": "system", "content": "請用繁體中文進行後繼續對話"},
            {"role": "user", "content": user_input},
        ],
    )

    assistant_missage = response.choices[0].message.content
    print(f"AI:{assistant_missage}")
