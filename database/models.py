from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Users Table

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    phone_number = Column(String)

    reg_date = Column(DateTime)

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, autoincrement=True, primary_key=True)
    q_text = Column(String, nullable=False)
    answer = Column(Integer, nullable=False)
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String, nullable=True)
    v4 = Column(String, nullable=True)

    reg_date = Column(DateTime)
# Таблица ответов пользователей
class UserAnswer(Base):
    __tablename__ = 'user_answers'
    id = Column(Integer, autoincrement=True, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user_answer = Column(Integer)

    correctness = Column(Boolean)
    question_id = Column(Integer, ForeignKey('questions.db'))

    answer_date = Column(DateTime)

    users_fk = relationship(User)
    question_fk = relationship(Question)















