<template>
    <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50" @click.self="closeModal">
      <div class="bg-white rounded-lg shadow-lg p-6 w-80 text-center">
        <button @click="closeModal" class="absolute top-2 right-2 p-2 scale-150 text-white hover:text-gray-700">
          &times;
        </button>
        <h2 class="text-xl font-semibold mb-4">Данные отправлены</h2>
        <p v-if="data.name" class="mb-2 text-center">{{ data.name }} спасибо что выбрали нас!</p>
        <p v-if="data.phone" class="mb-4">Скоро мы вам позвоним по</p>
        <p v-if="data.phone" class="mb-4">тел {{data.phone}}</p>

        <p class="mb-4">Вы всегда можете написать нам в Телеграм и Вотсап</p>
        <div>
          <a href="https://t.me/yourusername" target="_blank">
            <img src="~assets/img/telegram-app.webp" class="inline-block w-10 h-10 mx-2 hover:scale-110 duration-200" alt="Telegram">
          </a>
          <a href="https://wa.me/71234567890" target="_blank">
            <img src="~assets/img/whatsapp.webp" class="inline-block w-10 h-10 mx-2 hover:scale-110 duration-200" alt="WhatsApp">
          </a>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>  
  const props = defineProps({
    isOpen: {
        type: Boolean,
        required: true
    },
    data:{
        type: Object,
        required: true
    }
  });
  
  const emit = defineEmits(['close']);
  
  const closeModal = () => {
    emit('close');
  };
  </script>
  