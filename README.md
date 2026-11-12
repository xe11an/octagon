# Octagon Book API

REST API для управления каталогом книг и категорий (FastAPI + PostgreSQL + SQLAlchemy).


### 1. Подготовка базы данных (PostgreSQL)
Создайте пользователя и базу данных:
sudo -u postgres psql
CREATE USER octagon WITH PASSWORD '12345';
CREATE DATABASE octagon_db OWNER octagon;
\q

### 2. Клонирование репозитория
git clone https://github.com/xe11an/octagon.git
cd octagon

### 3. Настройка окружения
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 4. Переменные окружения
Создайте файл .env в корне проекта:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345

### 5. Инициализация БД
python3 -m app.init_db

### 6. Запуск
uvicorn app.main:app --reload
Документация: http://127.0.0.1:8000/docs