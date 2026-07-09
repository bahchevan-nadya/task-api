# Task API
Мини-сервис для учета задач, разработанный на FastAPI.

## Стек
- FastAPI
- SQLAlchemy
- SQLite
- Pytest
- Docker

## Установка
Создать виртуальное окружение:
```bash
python -m venv .venv
```
Активировать окружение.
```bash
.venv\Scripts\activate
```
Установить зависимости:
```bash
pip install -r requirements.txt
```

## Запуск
```bash
python -m uvicorn app.main:app --reload
```
Swagger доступен по адресу:
```
http://127.0.0.1:8000/docs
```

## Запуск тестов
```bash
pytest
```

## Docker
Сборка образа:
```bash
docker build -t task-api .
```
Запуск контейнера:
```bash
docker run -p 8000:8000 task-api
```