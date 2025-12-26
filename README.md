# LLM API Practice

ここはAPI版のLLMを色々試すための実験場です。

## ファイル構成

- `src/main.py`: Inux Dev Assistant (Rust信者のカーネルハッカー) と対話するCLIツール
- `src/list_models.py`: 利用可能なGeminiモデル一覧を取得するスクリプト

## セットアップ

`.env` ファイルに `GEMINI_API_KEY` を設定して実行してください。

## 設定

使用するモデルや共通設定は `src/config.py` で管理しています。
使用するモデルを変更したい場合は、このファイルの `GENERATION_MODEL_ID` を書き換えてください。
