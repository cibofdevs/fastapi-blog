import datetime

from router.schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DbPost


def create(db: Session, request: PostBase):
    new_post = DbPost(
        image_url=request.image_url,
        title=request.title,
        content=request.content,
        creator=request.creator,
        timestamp=datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # capture generated id
    return new_post


def get_all(db: Session):
    return db.query(DbPost).all()
