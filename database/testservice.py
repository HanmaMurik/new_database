from database.models import Question
from database import get_db
from datetime import datetime
# Функция добавления вопроса
def add_question_db(q_text, answer, v1, v2, v3=None, v4=None):
    db = next(get_db())

    new_question = db.query(q_text=q_text, answer=answer, v1=v1, v2=v2, v3=v3, v4=v4, reg_gdate=datetime.now())

    db.add(new_question)
    db.commit()
    return 'что-то'


# Функция получения вопросов (20 шт)
def get_20_questions_db():
    db = next(get_db())

    all_question = db.query(Question).all()

    return all_question[:20]

