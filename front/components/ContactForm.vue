<template>
    <div class="flex justify-center items-center min-h-screen bg-gray-100">
        <div class="bg-white mx-6 p-6 rounded-lg shadow-lg max-w-md w-full">
            <h2 data-aos="fade-up" data-aos-once="true" data-aos-delay="200" class="text-2xl font-bold mb-4">Связаться с
                нами легко!</h2>
            <p data-aos="fade-left" data-aos-once="true" data-aos-delay="350" class="mb-6">Оставьте свои данные, и мы
                перезвоним вам в течение 15 минут для обсуждения вашего проекта!</p>

            <form @submit.prevent="handleSubmit">
                <div data-aos="fade-right" data-aos-once="true" data-aos-delay="200" class="mb-4">
                    <label for="name" class="block text-sm font-medium text-gray-700">Имя:</label>
                    <input type="text" id="name" v-model="formData.name"
                        :class="{ 'error': errors.includes('Имя не должно быть пустым.') }" required
                        placeholder="Иванов Иван Иванович"
                        class="mt-1 block w-full border border-gray-300 rounded-xl shadow-sm p-2 focus:outline-none focus:ring focus:ring-sky-500" />
                </div>

                <div data-aos="fade-right" data-aos-once="true" data-aos-delay="300" class="mb-4">
                    <label for="phone" class="block text-sm font-medium text-gray-700">Телефон:</label>
                    <input type="tel" id="phone" v-model="formData.phone"
                        :class="{ 'error': errors.includes('Телефон должен быть в формате: 89031231212.') }" required
                        placeholder="89031231212"
                        class="mt-1 block w-full border border-gray-300 rounded-xl shadow-sm p-2 focus:outline-none focus:ring focus:ring-sky-500" />
                </div>

                <div data-aos="fade-right" data-aos-once="true" data-aos-delay="350" class="mb-4">
                    <label for="email" class="block text-sm font-medium text-gray-700">Email (необязательно):</label>
                    <input type="email" id="email" v-model="formData.email"
                        :class="{ 'error': errors.includes('Введите корректный email адрес.') }"
                        placeholder="ivanov@mail.ru"
                        class="mt-1 block w-full border border-gray-300 rounded-xl shadow-sm p-2 focus:outline-none focus:ring focus:ring-sky-500" />
                </div>

                <div data-aos="fade-right" data-aos-once="true" data-aos-delay="400" class="flex items-center mb-4">
                    <input type="checkbox" id="consent" v-model="formData.consent"
                        :class="{ 'error': errors.includes('Вы должны согласиться с условиями обработки персональных данных.') }"
                        required />
                    <label for="consent" class="ml-2 text-sm text-gray-600">Вы соглашаетесь с <a href="#"
                            class="text-sky-500">условиями обработки персональных данных</a>.</label>
                </div>

                <button data-aos="fade-up" data-aos-once="true" data-aos-delay="350" type="submit"
                    class="w-full bg-sky-500 text-white font-bold py-2 rounded-xl hover:bg-sky-600 focus:outline-none focus:ring-2 focus:ring-sky-300">Отправить</button>
            </form>

            <!-- Вывод ошибок -->
            <div v-if="errors.length" class="mt-4">
                <ul class="text-red-500">
                    <li v-for="error in errors" :key="error">{{ error }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>


<script setup>
const emit = defineEmits(['close']);
const formData = ref({
    name: '',
    phone: '',
    email: '',
});

const errors = ref([]);

const handleSubmit = () => {
    errors.value = []; // Сбрасываем ошибки перед проверкой
    if (validateForm()) {
        postData();
    }
};

const validateForm = () => {
    const phonePattern = /^\d{11}$/; // Предполагаем, что телефон должен быть в формате 89031231212

    if (!formData.value.name) {
        errors.value.push("Имя не должно быть пустым.");
    }

    if (!phonePattern.test(formData.value.phone)) {
        errors.value.push("Телефон должен быть в формате: 89031231212.");
    }

    // Проверяем email только если он введён
    if (formData.value.email && !/\S+@\S+\.\S+/.test(formData.value.email)) {
        errors.value.push("Введите корректный email адрес.");
    }

    // Проверка согласия
    if (!formData.value.consent) {
        errors.value.push("Вы должны согласиться с условиями обработки персональных данных.");
    }

    return errors.value.length === 0; // Возвращаем true, если нет ошибок
};

async function postData() {
    // const host = 'https://gkiverstroy.ru'
    const baseUrl = useRuntimeConfig().public.baseUrl;
    console.log('baseUrl :>> ', baseUrl);
    const url = `/api/clients`;
    console.log('url :>> ', url);
    // Деструктурируем consent, оставляя остальные данные
    const { consent, ...remainingData } = formData.value;

    try {
        const response = await $fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': '*/*',
                'Host': `${baseUrl}`,
            },
            body: JSON.stringify(remainingData), // Преобразуем в JSON
        });

        // Здесь не нужно проверять response.ok, если используете $fetch
        // напрямую работаем с данными
        // Вы можете делать что-то с ответом:
        console.log(response);
        emit('success', response);
    } catch (error) {
        // Обработка ошибок
        console.error('Something went wrong:', error);
    }
}


</script>

<style scoped>
/* Добавьте стили для ошибок, если необходимо */
.error {
    border-color: red;
}
</style>
