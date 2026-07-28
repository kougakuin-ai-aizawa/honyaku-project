import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# ブラウザからの通信（CORS）を許可する設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 開発用（どこからのアクセスも許可）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI クライアントの初期化（環境変数 OPENAI_API_KEY を参照）
client = OpenAI()

class TranslationRequest(BaseModel):
    text: str

@app.post("/translate")
async def translate(req: TranslationRequest):
    if not req.text.strip():
        return {"translation": ""}
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "あなたはプロの翻訳家です。与えられた日本語を自然な英語に翻訳し、余計な解説は含めず訳文のみを出力してください。"
                },
                {"role": "user", "content": req.text}
            ],
            temperature=0.3
        )
        translated_text = response.choices[0].message.content.strip()
        return {"translation": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
