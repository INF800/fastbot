from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastbot.whatsapp.router import router as whatsapp_router


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(whatsapp_router)

templates = Jinja2Templates(directory="templates")

@app.head("/")
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )