from fastapi import FastAPI
from app.api import books, categories

app = FastAPI(title="Octagon Book API")

# Подключаем роутеры
app.include_router(categories.router)
app.include_router(books.router)

# Эндпоинт для проверки работоспособности
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}