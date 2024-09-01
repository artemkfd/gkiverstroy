import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from flask import Flask, request
import logging

# Загружаем переменные окружения из файла .env
load_dotenv()

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s', level=logging.INFO)

app = Flask(__name__)

# Инициализация Telegram-бота
class TelegramBot:
    def __init__(self):
        self.token = os.environ.get('TELEGRAM_BOT_TOKEN')
        self.bot = Bot(token=self.token)
        self.application = ApplicationBuilder().token(self.token).build()
        # Регистрируем хендлеры
        self.application.add_handler(CommandHandler("start", self.start))

    async def send_message(self, chat_id, message):
        await self.bot.send_message(chat_id=chat_id, text=message)

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text('Привет! Я ваш Telegram-бот.')

# Создаем экземпляр бота
telegram_bot = TelegramBot()

@app.route('/send_message', methods=['POST'])
def send_message_route():
    data = request.json
    chat_id = data.get('chat_id')
    message = data.get('message')

    try:
        asyncio.run(telegram_bot.send_message(chat_id, message))
        return 'Message sent', 200
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения в Telegram: {e}")
        return 'Error', 500

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.json, telegram_bot.bot)
    # Обрабатываем входящие обновления
    telegram_bot.application.process_update(update)
    return 'ok', 200

async def set_webhook():
    await telegram_bot.bot.set_webhook(url='https://gkiverstroy.ru/webhook')

if __name__ == '__main__':
    # Установите вебхук
    asyncio.run(set_webhook())

    # Запускаем Flask
    app.run(host='0.0.0.0', port=5000)