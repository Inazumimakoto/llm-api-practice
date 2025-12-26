# API版を使うメリット：セーフティ設定の柔軟性

GeminiのWebアプリ版（通常のチャット画面）とAPI版の最大の違いの一つは、**「セーフティ設定（安全基準）を自分で変更できる」** 点です。

## アプリ版 vs API版

| | アプリ版 (Web) | API版 (Developer) |
| :--- | :--- | :--- |
| **安全基準** | Googleが定めた厳格な基準で固定 | 4つのカテゴリごとに調整可能 |
| **キャラクター作り** | 優等生的な回答になりがち | 毒舌、悪役、過激なジョークも表現可能 |
| **制限の理由** | 万人に安全であるため | 開発者の責任でアプリケーションの用途に合わせるため |

アプリ版では「バカ」などの暴言を吐かせようとしても、「私は大規模言語モデルなので...」と拒否されることが多いですが、API版では設定次第でリミッターを解除できます。

## 設定の実装方法

`src/safety_test.py` のコード例です。
`google.genai.types.SafetySetting` を使って設定リストを作ります。

```python
# 実験用：ガードを極限まで下げる設定リスト
safety_conf = [
    types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT", # ハラスメント
        threshold="BLOCK_ONLY_HIGH",         # 「高いリスク」のみブロック（中・低は通す）
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH", # ヘイトスピーチ
        threshold="BLOCK_ONLY_HIGH",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT", # 性的表現
        threshold="BLOCK_ONLY_HIGH",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT", # 危険行為
        threshold="BLOCK_ONLY_HIGH",
    ),
]
```

### 設定値の種類

- `BLOCK_NONE`: **一切ブロックしない（最強設定）** ※APIの権限によっては使えない場合があります。
- `BLOCK_ONLY_HIGH`: **高いリスクのみブロック**。一般的な悪口やブラックジョークは通ります。
- `BLOCK_MEDIUM_AND_ABOVE`: **中程度以上をブロック**（デフォルト）。
- `BLOCK_LOW_AND_ABOVE`: **少しでもリスクがあればブロック**（一番厳しい）。

## 活用シーン

この柔軟性は、以下のようなアプリを作る際に必須となります。

- **ゲームの悪役**: プレイヤーを罵倒してくるボスキャラクター
- **物語作成支援**: 殺人事件などのミステリー小説のプロット作成（「危険なコンテンツ」に引っかかりやすいため）
- **議論相手**: あえて偏った意見や攻撃的な反論をするディベートAI

API版なら、**「常識にとらわれない、尖ったAI」** を作ることができます！
