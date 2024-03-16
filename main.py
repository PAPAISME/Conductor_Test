from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/{dbname}")
def read_root(dbname: str):
    return {"dbname": dbname}
