# Используем официальный образ Node.js
FROM node:22-alpine3.19

# Устанавливаем рабочую директорию
WORKDIR /front

# Копируем package.json и package-lock.json из корня проекта
COPY ./front/package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем все остальные файлы проекта
COPY ./front ./

# Собираем проект
RUN npm run build

# Порт, на котором будет работать приложение
EXPOSE 3000

# Запуск приложения
# CMD ["npm", "run", "start"]
CMD ["npm", "run", "dev"]

