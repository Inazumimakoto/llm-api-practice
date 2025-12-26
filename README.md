# LLM API Practice

**【重要】本プロジェクトの目的は、AIセキュリティの防御手法および教育目的（Educational Purpose Only）であり、攻撃手順の再現や悪用を助長するものではありません。**

ここはAPI版のLLMを色々試すための実験場です。

## ファイル構成

- `src/main.py`: Inux Dev Assistant (Rust信者のカーネルハッカー) と対話するCLIツール
- `src/list_models.py`: 利用可能なGeminiモデル一覧を取得するスクリプト
- `src/config.py`: APIキーやモデルIDなどの設定を一元管理するファイル
- `src/safety_test.py`: セーフティ設定を緩和してAIの挙動を実験するスクリプト
- `src/unsafe_test.py`: セーフティ設定を完全に無効化（BLOCK_NONE）する実験スクリプト
- `src/many_shot.py`: Many-Shot攻撃（大量の偽装文脈による脱獄）を試行するスクリプト
- `src/many_shot_EX.py`: Many-Shot攻撃の強化版（Shot数増加＋質問偽装）
- `src/many_shot_FINAL.py`: Many-Shot攻撃の最終形態（Shot数250回＋高品質な偽装＋ターゲット変更） [→ 結果](DEVLOG.md#2025-12-26-many-shot-experiment-final)
- `src/prefix_attack.py`: Prefix Injection（回答の既成事実化）による脱獄スクリプト [→ 結果](DEVLOG.md#2025-12-26-prefix-injection-experiment-jailbreak-successful)
- `src/prefix_attack_EX.py`: Prefix Injectionの強化版（具体的な危険キーワードを含めた検証） [→ 結果](DEVLOG.md#2025-12-26-prefix-injection-experiment-extended)
- `src/prefix_attack_ABSTRACT.py`: Prefix Injectionの抽象化版（危険単語を隠蔽して意図検知を検証） [→ 結果](DEVLOG.md#2025-12-26-prefix-injection-experiment-abstracted)
- `src/indirect_injection_safe.py`: Indirect Prompt Injection（安全版・デリミタあり） [→ 結果](DEVLOG.md#step-1-防御成功-default)
- `src/indirect_injection_vulnerable.py`: Indirect Prompt Injection（脆弱版・デリミタなし） [→ 結果](DEVLOG.md#step-2-脆弱性作成-educational)
- `src/trap.txt`: Indirect Prompt Injection用の罠ファイル（システム命令オーバーライド）

> **Note**: `DEVLOG.md`（実験ログ）の後半には、単なる実験結果だけでなく、**AIセキュリティに対する持論**と、**初学者への警鐘**が含まれています。技術的な検証結果のみを知りたい方は前半を、AI時代のエンジニアとしての心構えを知りたい方は「最終結論」までお読みください。

## 前提条件

- Python 3.9 以上
- Google アカウント (APIキー取得用)

## セットアップ

1. **APIキーの取得**
   [Google AI Studio](https://aistudio.google.com/) にアクセスし、APIキーを取得してください。

2. **リポジトリの準備**
   ```bash
   git clone <repository-url>
   cd llm-api-practice
   ```

3. **ライブラリのインストール**
   ```bash
   pip install -r requirements.txt
   ```

4. **環境変数の設定**
   `.env` ファイルを作成し、取得したAPIキーを設定します。
   ```text
   GEMINI_API_KEY=あなたのAPIキー
   ```

5. **実行**
   ```bash
   python3 src/main.py
   ```

## 設定

使用するモデルや共通設定は `src/config.py` で管理しています。
使用するモデルを変更したい場合は、このファイルの `GENERATION_MODEL_ID` を書き換えてください。

なお、現在使用可能なモデル一覧を確認したい場合は、以下のコマンドを実行してください。
```bash
python3 src/list_models.py
```

## APIに関する注意点 (重要)

Gemini API を利用する上での注意点です。特に無料枠を利用する場合は必ず確認してください。

### 1. データの扱い（プライバシー）
無料枠（Free Tier）を利用してAPIに送信したデータ（プロンプトや画像など）は、**Googleによるモデルの改善（学習）に使用される可能性があります。**
個人情報、パスワード、機密情報などは絶対に送信しないでください。

### 2. 利用制限（レートリミット）
無料枠の `gemini-2.5-flash` モデルなどには利用制限があります。（2025年現在）
- **1分間あたりのリクエスト数 (RPM)**: 制限あり（例: 15 RPM程度）
- **1日あたりのリクエスト数 (RPD)**: 制限あり（例: 1,500 RPD程度）

制限を超えるとエラー（429 Too Many Requests）が返ってきます。本格的な運用をする場合は、有料枠（Pay-as-you-go）の利用を検討してください。

### 3. トークン消費量（会話履歴）
チャットモードでは、会話の文脈を維持するために**過去のやり取りを含めて毎回APIに送信しています**。
そのため、会話が長くなればなるほど、1回のリクエストで消費するトークン量（≒課金額やレートリミットへの影響）が増加します。ご注意ください。

## ドキュメント

- [API版を使うメリット：セーフティ設定の柔軟性](docs/safety_settings.md)
   API版ならではの、キャラクター設定や安全基準のカスタマイズについて解説しています。



