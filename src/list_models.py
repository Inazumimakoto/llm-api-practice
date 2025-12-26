import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("--- あなたが使えるモデル一覧 ---")
try:
    # Googleに「使えるやつ全部教えて」と聞く
    for m in client.models.list():
        # "generateContent"（会話機能）に対応してるものだけ表示
        if "generateContent" in m.supported_actions:
            # モデル名の "models/" という部分はカットして表示
            print(f"- {m.name.replace('models/', '')}")
            
except Exception as e:
    print(f"接続エラー: {e}")
    print("\n※もしここでエラーが出るなら、APIキーが無効か、通信が遮断されています。")
