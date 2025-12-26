import os
from dotenv import load_dotenv

# .envを読み込む（プロジェクトルートの.envを探してくれる）
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 使用するモデルIDを一元管理
GENERATION_MODEL_ID = "gemini-2.5-flash"
