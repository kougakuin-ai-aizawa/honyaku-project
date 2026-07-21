from openai import OpenAI

# クライアント初期化（環境変数 OPENAI_API_KEY を自動参照）
client = OpenAI()

def translate_ja_to_en_gpt(text: str) -> str:
    """
    OpenAI APIを使って日本語を英語に翻訳する関数
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # 軽量で高速・安価なモデル
            messages=[
                {
                    "role": "system", 
                    "content": "あなたはプロの翻訳家です。与えられた日本語を、自然で適切な英語に翻訳してください。"
                },
                {"role": "user", "content": text}
            ],
            temperature=0.3 # 低めに設定して一貫性・正確性を高める
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return ""

# 実行例
japanese_text = "こんにちは！現在翻訳アプリを開発しています。"
english_text = translate_ja_to_en_gpt(japanese_text)

print(f"訳文: {english_text}")
