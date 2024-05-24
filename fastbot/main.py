from typing import Union

from fastapi import FastAPI

from fastbot.whatsapp import router as wa_router


app = FastAPI()

app.include_router(wa_router)


@app.head("/")
@app.get("/")
def read_root():
    return {"status": "online"}