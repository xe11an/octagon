from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.db import crud
from app.db.db import get_db
from app import schemas

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[schemas.BookResponse])
def read_books(category_id: Optional[int] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Фильтрация по категории (если передана)
    if category_id:
        # Здесь можно добавить функцию в crud.py, но для простоты отфильтруем тут
        return db.query(crud.models.Book).filter(crud.models.Book.category_id == category_id).offset(skip).limit(limit).all()
    return crud.get_books(db, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # Проверяем, существует ли категория
    db_category = crud.get_category(db, category_id=book.category_id)
    if db_category is None:
        raise HTTPException(status_code=400, detail="Category not found")
    return crud.create_book(
        db=db, title=book.title, description=book.description, 
        price=book.price, category_id=book.category_id, url=book.url
    )

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    # Если меняется категория, проверяем её существование
    if book.category_id is not None:
        db_category = crud.get_category(db, category_id=book.category_id)
        if db_category is None:
            raise HTTPException(status_code=400, detail="Category not found")
            
    db_book = crud.update_book(db, book_id=book_id, title=book.title, price=book.price)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return None