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
    checker = db.query(UserAnswer).filter_by(user_id=user_id, correctness=True).all()

    if checker:
        return len(checker)
    return 0

# вывод лидеров
def show_leaders_db() -> list:
    # Сгенерировать подключение
    db = next(get_db())

    rating = db.query(UserAnswer).all()

    return rating[:5]



# Запись результатов
def add_user_answer_db(user_id, question_id,  user_answer, correctness) -> bool:
    db = next(get_db())
    add_answer = UserAnswer(user_id=user_id, question_id= question_id, user_answer=user_answer, correctness=correctness, answer_date=datetime.now())
    db.add(add_answer)
    db.commit()
    return True