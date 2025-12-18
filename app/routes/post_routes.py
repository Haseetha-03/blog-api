from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(prefix="/posts", tags=["Posts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = crud.create_post(db, post)
    if not new_post:
        raise HTTPException(status_code=400, detail="Author not found")
    return new_post

@router.get("/", response_model=list[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)
