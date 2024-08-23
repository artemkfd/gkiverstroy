<template>
    <div class="flex justify-center items-center min-h-screen bg-gray-100">
        <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
            <h2 data-aos="fade-up" data-aos-once="true" data-aos-delay="200" class="text-2xl font-bold mb-4">Связаться с нами легко!</h2>
            <p data-aos="fade-left" data-aos-once="true"  data-aos-delay="350" class="mb-6">Оставьте свои данные, и мы перезвоним вам в течение 15 минут для обсуждения вашего проекта!</p>

            <form  @submit.prevent="handleSubmit">
                <div data-aos="fade-right" data-aos-once="true"  data-aos-delay="200" class="mb-4">
                    <label for="name" class="block text-sm font-medium text-gray-700">Имя:</label>
                    <input type="text" id="name" v-model="formData.name" required class="mt-1 block w-full border border-gray-300 rounded-xl shadow-sm p-2 focus:outline-none focus:ring focus:ring-sky-500" />
                </div>

                <div data-aos="fade-right" data-aos-once="true"  data-aos-delay="300" class="mb-4">
                    <label for="phone" class="block text-sm font-medium text-gray-700">Телефон:</label>
                    <input type="tel" id="phone" v-model="formData.phone" required class="mt-1 block w-full border border-gray-300 rounded-xl shadow-sm p-2 focus:outline-none focus:ring focus:ring-sky-500" />
                </div>

                <div data-aos="fade-right" data-aos-once="true"  data-aos-delay="350" class="mb-4">
                    <label for="email" class="block text-sm font-medium text-gray-700">Email:</label>
                    <input type="email" id="email" v-model="formData.email" required class="mt-1 block w-full border border-gray-300 rounded-xl shadow-sm p-2 focus:outline-none focus:ring focus:ring-sky-500" />
                </div>

                <button data-aos="fade-up" data-aos-once="true"  data-aos-delay="350" type="submit" @click="handleSubmit" class="w-full bg-sky-500 text-white font-bold py-2 rounded-xl hover:bg-sky-600 focus:outline-none focus:ring-2 focus:ring-sky-300">Отправить</button>
            </form>
        </div>
    </div>
</template>


<script setup>
const formData = ref({
    name: '',
    phone: '',
    email: '',
});

const handleSubmit = () => {
    // Здесь можно добавить логику для отправки данных формы
    console.log('Форма отправлена:', formData.value);

    // Очистка формы после отправки
    formData.value = {
        name: '',
        phone: '',
        email: '',
    };
};
</script>

<style  scoped></style>