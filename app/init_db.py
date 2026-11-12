from app.db.db import engine, Base, SessionLocal
from app.db import crud

def init_db():
    # Создаем таблицы, если их еще нет
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        
        if crud.get_categories(db):
            print("База данных уже содержит данные. Пропускаем инициализацию.")
            return

        # 1. Создаем категории
        cat_fantasy = crud.create_category(db, title="Фантастика")
        cat_prog = crud.create_category(db, title="Программирование")

       
        crud.create_book(
            db=db,
            title="Дюна",
            description="Научная фантастика о пустынной планете",
            price=599.99,
            category_id=cat_fantasy.id,
            url="http://example.com/dune"
        )
        crud.create_book(
            db=db,
            title="Основание",
            description="Классика Айзека Азимова",
            price=499.99,
            category_id=cat_fantasy.id,
            url=None
        )

        
        crud.create_book(
            db=db,
            title="Изучаем Python",
            description="Подробное руководство для начинающих",
            price=899.99,
            category_id=cat_prog.id,
            url="http://example.com/python"
        )
        crud.create_book(
            db=db,
            title="Чистый код",
            description="Руководство по созданию качественного кода",
            price=799.99,
            category_id=cat_prog.id,
            url=None
        )

        print("База данных успешно заполнена тестовыми данными!")
        
    except Exception as e:
        print(f"Произошла ошибка при заполнении БД: {e}")
        db.rollback() 
    finally:
        db.close()

if __name__ == "__main__":
    init_db()