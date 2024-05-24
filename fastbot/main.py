from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.head("/")
@app.get("/")
def read_root():
    return {"status": "online"}