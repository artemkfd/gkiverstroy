<template>
    <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50" @click.self="closeModal">
      <div class="bg-white rounded-lg shadow-lg p-6 w-80 text-center">
        <button @click="closeModal" class="absolute top-2 right-2 p-2 scale-150 text-white hover:text-gray-700">
          &times;
        </button>
        <h2 class="text-xl font-semibold mb-4">Связаться с нами</h2>
        <p class="mb-2">Телефон: +7 (123) 456-78-90</p>
        <p class="mb-4">Адрес: ул. Примерная, 1, Москва, Россия</p>
        <div>
          <a href="https://t.me/yourusername" target="_blank">
            <img src="https://img.icons8.com/color/48/000000/telegram-app.png" class="inline-block w-10 h-10 mx-2 hover:scale-110 duration-200" alt="Telegram">
          </a>
          <a href="https://wa.me/71234567890" target="_blank">
            <img src="https://img.icons8.com/color/48/000000/whatsapp.png" class="inline-block w-10 h-10 mx-2 hover:scale-110 duration-200" alt="WhatsApp">
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
    }
  });
  
  const emit = defineEmits(['close']);
  
  const closeModal = () => {
    emit('close');
  };
  </script>
  