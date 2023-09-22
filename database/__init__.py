from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ссылка к базе данных
SQLALCHEMY_DATABASE_URL = 'sqlite:///data.db'
# Подключение к базе
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Соединение с базой
SessionLocal = sessionmaker(bind=engine)
# Класс для наследования в таблицах
Base = declarative_base()


# Импорт всех моделей
from database import models


# Генератор соединений с базой
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()