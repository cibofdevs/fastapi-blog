from fastapi import FastAPI
from db import models
from db.database import engine

app = FastAPI()


@app.get("/")
def hello_world():
    return "Hello World!"


models.Base.metadata.create_all(engine)
