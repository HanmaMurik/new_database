from fastapi import APIRouter


test_process_router = APIRouter(prefix='/test', tags=['Процесс прохождения теста'])

# получить 20 вопросов
@test_process_router.get('/get-questions')
async def get_questions():
    pass

# Проверка каждого ответа пользователя
@test_process_router.post('/check-answer')
async def check_answer():
    pass


@test_process_router.post('/add-question')
async def add_question():
    pass