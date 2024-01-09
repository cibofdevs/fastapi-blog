from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db import models
from db.database import engine
from router import post

app = FastAPI()
app.include_router(post.router)

# generate database
models.Base.metadata.create_all(engine)

# mount static file
app.mount("/images", StaticFiles(directory="images"), name="images")
