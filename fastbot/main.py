from typing import Union

from fastapi import FastAPI

from fastbot.whatsapp.router import router as whatsapp_router


app = FastAPI()

app.include_router(whatsapp_router)


@app.head("/")
@app.get("/")
def read_root():
    return {"status": "online"}