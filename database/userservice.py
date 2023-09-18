from datetime import datetime
from database import get_db
from database.models import User, UserAnswer



# Регистрация
def register_user_db(name: str, phone_number: str) -> int:
    # Сгенерировать подключение
    db = next(get_db())
    # запрос на получение определенного пользователя
    exact_user = db.query(User).filter_by(phone_number=phone_number).first()
    # если есть пользователь в базе
    if exact_user:
        return exact_user.id
    # Если нету пользователся в базе. Регестрируем
    else:
        # Регестрируем
        new_user = User(name=name, phone_number=phone_number, reg_data=datetime.now())

        # Добовляем запись в базу
        db.add(new_user)
        # Сохроняем изменения
        db.commit()

        return new_user.id


# вывод результатов
def get_user_score_db(user_id: int) -> int:
    # Сгенерировать подключение
    db = next(get_db())
    # Делаем проверку
    checker =  db.query(UserAnswer).filter_by(user_id=user_id, correctness=True).all()

    if checker:
        return len(checker)
    else:
        pass

# вывод лидеров
def show_leaders_db() -> list:
    # Сгенерировать подключение
    db = next(get_db())