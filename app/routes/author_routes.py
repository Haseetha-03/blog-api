from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(prefix="/authors", tags=["Authors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AuthorResponse)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    result = crud.create_author(db, author)
    if not result:
        raise HTTPException(status_code=400, detail="Email already exists")
    return result


# 🔽🔽 THIS IS STEP 3 ENDPOINT 🔽🔽
@router.get("/{author_id}/posts", response_model=list[schemas.PostResponse])
def get_author_posts(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    return crud.get_posts_by_author(db, author_id)
@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    deleted_author = crud.delete_author(db, author_id)
    if not deleted_author:
        raise HTTPException(status_code=404, detail="Author not found")

    return {"message": "Author and associated posts deleted successfully"}
