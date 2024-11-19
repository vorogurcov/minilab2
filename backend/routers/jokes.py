import requests

from fastapi import APIRouter

from backend.config import settings

jokes_router = APIRouter(prefix=settings.URL_PREFIX + '/joke', tags=['Jokes'])

@jokes_router.get('/random')
def get_random_joke():
    joke_url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(joke_url)
    joke = response.json()

    if response.status_code == 200:  # Проверка кода ответа
        return joke
    elif response.status_code == 404:
        return {"status": 401,
                "message": "Ай-ай-ай, неверный токен авторизации!"}  # Отправляем своё сообщение и код ошибки
    else:
        return joke