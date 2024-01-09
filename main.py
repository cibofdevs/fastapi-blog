from fastapi import FastAPI
from db import models
from db.database import engine
from router import post

app = FastAPI()
app.include_router(post.router)

models.Base.metadata.create_all(engine)
