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
