# Используем официальный образ Python
FROM python:3.10-alpine

# Устанавливаем рабочую директорию
WORKDIR /backend

# Устанавливаем необходимые пакеты
RUN apk add --no-cache build-base gfortran postgresql-dev

# Копируем файл зависимостей
COPY ./requirements.txt ./

# Устанавливаем зависимости
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY ./ ./

# Выполняем миграции, собираем статические файлы и запускаем сервер
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn backend.wsgi:application --bind 0.0.0.0:8000"]


# Выполняем миграции и запускаем сервер
# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
# CMD ["sh", "-c", "python manage.py migrate && gunicorn myproject.wsgi:application --bind 0.0.0.0:8000"]