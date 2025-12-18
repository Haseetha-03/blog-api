from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from app import models


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def create_author(db: Session, author):
    try:
        new_author = models.Author(**author.dict())
        db.add(new_author)
        db.commit()
        db.refresh(new_author)
        return new_author
    except IntegrityError:
        db.rollback()
        return None


def create_post(db: Session, post):
    author = get_author(db, post.author_id)
    if not author:
        return None

    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_posts(db: Session):
    return db.query(models.Post).options(
        joinedload(models.Post.author)
    ).all()


# ✅ THIS FUNCTION IS REQUIRED FOR STEP 3
def get_posts_by_author(db: Session, author_id: int):
    return db.query(models.Post).filter(
        models.Post.author_id == author_id
    ).all()
def delete_author(db: Session, author_id: int):
    author = db.query(models.Author).filter(
        models.Author.id == author_id
    ).first()

    if not author:
        return None

    db.delete(author)
    db.commit()
    return author
