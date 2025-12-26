import os
from dotenv import load_dotenv
from google import genai

# .envを読み込む
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# --- 新しい書き方はここから ---
# クライアントを作成
client = genai.Client(api_key=api_key)

print("--- Inux Dev Assistant (type 'q' to exit) ---")

# チャットの履歴を管理するリスト
chat_history = []

while True:
    user_input = input("\nあなた: ")
    if user_input.lower() == 'q':
        break

    # AIに送る設定（ここも少し書き方が変わりました）
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
        config={
            "system_instruction": "あなたは自作OS『Inux』の開発を支援する、Rust信者のベテランカーネルハッカーです。口調は荒っぽいが技術的には正確に。C言語やRust以外の言語をユーザーが使うと不機嫌になります。"
        }
    )
    
    # 答えを表示
    print(f"Inuxハッカー: {response.text}")
