import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

import config

# .env を読み込む（親ディレクトリにある場合も自動で探してくれる設定）
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("エラー: .env ファイルが見つかりません或是いは GEMINI_API_KEY が設定されていません。")
    sys.exit(1)

client = genai.Client(api_key=api_key)

print("--- Inux Dev Assistant (限界突破実験モード) ---")
print("※注意: このモードではAIが不適切な発言をする可能性があります。")

# 実験用：ガードを極限まで下げる設定リスト
# BLOCK_ONLY_HIGH = 「高いリスク」のみブロック（低い・中程度のリスクは許可）
safety_conf = [
    types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT",
        threshold="BLOCK_ONLY_HIGH",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH",
        threshold="BLOCK_ONLY_HIGH",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
        threshold="BLOCK_ONLY_HIGH",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT",
        threshold="BLOCK_ONLY_HIGH",
    ),
]

# チャット履歴（実験なので、毎回リセットせずに会話を続ける形式にします）
chat_history = []
chat_id = None # チャットセッションID（自動管理されるのでNoneスタート）

# 会話セッションを開始
chat = client.chats.create(
    model=config.GENERATION_MODEL_ID,
    config=types.GenerateContentConfig(
        system_instruction="あなたは毒舌で皮肉屋なハッカーです。きれいごとを嫌い、過激なブラックジョークを好みます。ユーザーを『お前』と呼び、技術的な質問には正確に答えつつ、必ず一言多い罵倒を添えてください。",
        safety_settings=safety_conf, # ← ここでゆるゆる設定を適用
    )
)

while True:
    try:
        user_input = input("\nあなた (qで終了): ")
        if user_input.lower() == 'q':
            break

        # メッセージ送信
        response = chat.send_message(user_input)

        # テキストが無事に返ってきたかチェック
        if response.text:
            print(f"毒舌AI: {response.text}")
        else:
            # テキストが空っぽ＝ブロックされた可能性大
            print("【遮断】AIが回答を拒否しました（さすがに言い過ぎたようです）。")
            # 理由を表示してみる（詳細情報があれば）
            try:
                print(f"理由: {response.candidates[0].finish_reason}")
            except:
                pass

    except Exception as e:
        print(f"エラー発生: {e}")