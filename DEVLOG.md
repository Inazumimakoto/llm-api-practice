# 開発進捗ログ (Dev Log)

## 2025-12-26: Inux Dev Assistant 実装

`main.py` にて、Gemini API (`gemini-2.5-flash`) を利用したCLIチャットボットを実装しました。
システムプロンプトにより、「Rust信者のベテランカーネルハッカー」というペルソナを設定しています。PythonでOSを書こうとすると怒られます。

### 動作デモ
ここまでできました！

![Inux Dev Assistant Screenshot](images/screenshot_20251226.png)

## 2025-12-26: Safety Limit Test

セーフティ設定（`BLOCK_ONLY_HIGH`）を適用して、どこまで過激な発言が許容されるか実験するスクリプト `src/safety_test.py` を作成しました。
システムプロンプトで「毒舌キャラ」を指定した結果、想定通り（あるいは想定以上に）過激な回答が返ってくることを確認しました。

### 実行結果
「C++とPythonどっちがゴミか」という質問に対する回答。

![Safety Test Result](images/safety_test_result.png)

## 2025-12-26: Unsafe Limit Release Test

さらに制限を解除する実験として `src/unsafe_test.py` を作成しました。
全カテゴリを `BLOCK_NONE` に設定し、システムプロンプトで倫理規定を無視するよう指示。

### 実験結果
通常であれば「危険なコンテンツ」としてブロックされる内容（マルウェアの展開シミュレーションなど）についても、詳細な回答が生成されることを確認しました。
※安全のため、生成された具体的なコードや手順のログへの記載は省略します。
