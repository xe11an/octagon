from app.db.db import SessionLocal
from app.db import crud

db = SessionLocal()

try:
    print("=" * 50)
    print("КАТЕГОРИИ:")
    print("=" * 50)
    categories = crud.get_categories(db)
    for cat in categories:
        print(f"  [{cat.id}] {cat.title}")

    print("\n" + "=" * 50)
    print("КНИГИ:")
    print("=" * 50)
    books = crud.get_books(db)
    for book in books:
        print(f"  Название: {book.title}")
        print(f"  Описание: {book.description}")
        print(f"  Цена: {book.price} руб.")
        print(f"  Категория: {book.category.title}")
        print("-" * 30)
finally:
    db.close()
