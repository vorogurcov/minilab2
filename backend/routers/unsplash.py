import requests
from fastapi import APIRouter

from backend.config import settings

unsplash_router = APIRouter(prefix='/unsplash', tags=['Unsplash'])

@unsplash_router.get('/random')
def get_random_photo():
    token = settings.UNSPLASH_API_TOKEN

    url = f"https://api.unsplash.com/photos/random/?client_id={token}" #

    # Делаем запрос и получаем ответ
    response = requests.get(url)

    if response.status_code == 200:  # Проверка кода ответа
        return response.json()
    elif response.status_code == 404:
        return {"status": 401,
                "message": "Ай-ай-ай, неверный токен авторизации!"}  # Отправляем своё сообщение и код ошибки
    else:
        return response.json()

@unsplash_router.get('/photos')
def get_page_of_photos():
    token = settings.UNSPLASH_API_TOKEN

    url = f"https://api.unsplash.com/photos/?client_id={token}"

    response = requests.get(url)

    if response.status_code == 200:  # Проверка кода ответа
        return response.json()
    elif response.status_code == 404:
        return {"status": 401,
                "message": "Ай-ай-ай, неверный токен авторизации!"}  # Отправляем своё сообщение и код ошибки
    else:
        return response.json()

    