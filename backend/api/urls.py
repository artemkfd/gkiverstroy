from ninja import NinjaAPI
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Client 
from .schema import ClientIn, ClientOut
from typing import List
from backend.settings import TELEGRAM_CHAT_ID
import requests
import logging

api = NinjaAPI()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

@api.post("/clients", response=ClientOut)
def create_client(request, data: ClientIn):
    # Проверка наличия chat_id
    if not TELEGRAM_CHAT_ID:
        logging.error("TELEGRAM_CHAT_ID не установлен")
        return JsonResponse({"error": "Не установлен TELEGRAM_CHAT_ID"}, status=400)

    # Создаем нового клиента
    client = Client.objects.create(**data.dict())

    # Подготовка данных для отправки
    message = f"Новый клиент: {client.name}, Телефон: {client.phone}"
    
    try:
        # Отправка сообщения в Telegram через веб-хук
        response = requests.post(
            "https://gkiverstroy.ru/send_message",  # "https://gkiverstroy.ru/send_message" прямое обращение к вашему API
            json={"chat_id": TELEGRAM_CHAT_ID, "message": message}
        )
        response.raise_for_status()  # Проверяем, был ли успешным запрос
        
        logging.info(f"Сообщение отправлено в Telegram: {message}")
        return ClientOut.from_orm(client)

    except requests.RequestException as e:
        logging.error(f"Ошибка при отправке сообщения в Telegram: {str(e)}")
        return JsonResponse({"error": "Не удалось отправить сообщение в Telegram"}, status=500)

@api.get("/clients", response=List[ClientOut])
def get_clients(request):
    clients = Client.objects.all()
    return [ClientOut.from_orm(client) for client in clients]

@api.get("/clients/{client_id}", response=ClientOut)
def get_client(request, client_id: int):
    client = get_object_or_404(Client, id=client_id)
    return ClientOut.from_orm(client)
