import random
import shutil
import string

from fastapi import APIRouter, Depends, UploadFile, File
from router.schemas import PostBase, PostDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_post

router = APIRouter(
    prefix="/post",
    tags=["post"]
)


@router.post("")
def create(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)


@router.get("/all")
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return db_post.delete(id, db)


@router.post("/image")
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    rand_str = "".join(random.choice(letter) for i in range(6))
    new = f"_{rand_str}."
    filename = new.join(image.filename.rsplit(".", 1))
    path = f"images/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {
        "filename": path
    }
