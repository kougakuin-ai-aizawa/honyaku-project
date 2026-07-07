from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# FastAPIのアプリ本体を作成
app = FastAPI()

# 「templates」フォルダの中にあるHTMLを使うよ、という設定
templates = Jinja2Templates(directory="templates")

# ブラウザからアクセスされたときの処理
@app.get("/")
async def serve_home(request: Request):
    """
    トップページ（/）にアクセスが来たら、
    さっき作ったHTML画面をブラウザに返して表示させる
    """
    return templates.TemplateResponse("mojiokosi.html", {"request": request})