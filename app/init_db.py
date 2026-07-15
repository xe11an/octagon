from app.db.db import engine, Base, SessionLocal
from app.db.models import Category, Book
from app.db import crud

Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    cat1 = crud.create_category(db, "Фантастика")
    cat2 = crud.create_category(db, "Программирование")
  
    crud.create_book(db, "Дюна", "Научная фантастика о пустынной планете", 599.99, "", cat1.id)
    crud.create_book(db, "Основание", "Классика Айзека Азимова", 499.99, "", cat1.id)

    crud.create_book(db, "Изучаем Python", "Подробное руководство для начинающих", 899.99, "", cat2.id)
    crud.create_book(db, "Чистый код", "Руководство по созданию качественного кода", 799.99, "", cat2.id)

    print("База данных успешно заполнена!")
finally:
    db.close()
