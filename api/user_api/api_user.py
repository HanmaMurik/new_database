from fastapi import APIRouter

user_router = APIRouter(prefix='/user', tags=['Пользователи'])

# Регистрация пользователя

@user_router.post('/register')
async def register_user():
    pass

# Получить список лидеров
@user_router.get('/leaders')
async def get_5_leaders():
    pass


# Запись результата пользователя
@user_router.post('/done')
async def test_finished():
    pass