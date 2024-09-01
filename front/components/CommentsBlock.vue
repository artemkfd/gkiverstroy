<template>
    <!-- <div>
        <section class="py-12 bg-gray-100 duration-300" :class="{ 'blur-md': isGalleryModalOpen || isModalOpen }">
            <div class="container mx-auto">
                <h2 class="text-3xl font-bold text-center mb-8 text-gray-800">Отзывы наших клиентов</h2>
                <div class="grid grid-cols-1 md:grid-cols-2  lg:grid-flow-col lg:gap-4 lg:overflow-x-scroll gap-8 px-4">
                    <div data-aos="fade-right" data-aos-delay="200"
                        class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl duration-300 w-[500px]">
                        <p class="font-semibold">Алексей П.</p>
                        <p class="text-yellow-500">{{ stars }}</p>
                        <p class="mt-2">"Отличное качество резки! Заказывал детали для своего проекта, и они были
                            выполнены точно по
                            размерам. Очень доволен!"</p>
                    </div>
                    <div data-aos="fade-up" data-aos-delay="250"
                        class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl duration-300">
                        <p class="font-semibold">Мария И.</p>
                        <p class="text-yellow-500">{{ stars }}</p>
                        <p class="mt-2">"Сервис на высшем уровне! Быстрая доставка и внимательное отношение к клиентам.
                            Рекомендую
                            всем!"</p>
                    </div>
                    <div data-aos="fade-left" data-aos-delay="300"
                        class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl duration-300">
                        <p class="font-semibold">Дмитрий К.</p>
                        <p class="text-yellow-500">{{ starsFour }}</p>
                        <p class="mt-2">"Лазерная резка сделана аккуратно, но сроки выполнения немного затянулись. В
                            целом,
                            результат оправдал ожидания!"</p>
                    </div>
                    <div class="overflow-hidden relative">
                        <div data-aos="fade-right" data-aos-delay="200"
                         class="flex overflow-x-scroll scroll-smooth" id="comments-container">
                            <div v-for="comment in comments"
                                class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl duration-300">
                                <p class="font-semibold">{{ comment.name }}</p>
                                <p class="text-yellow-500">{{ comment.stars }}</p>
                                <p class="mt-2">{{ comment.text }}</p>
                            </div>
                        </div>

                        <button
                            class="absolute left-0 top-1/2 transform -translate-y-1/2 bg-gray-300 p-2 rounded-full hover:bg-gray-400"
                            onclick="scrollLeft()">
                            ◀
                        </button>

                        <button
                            class="absolute right-0 top-1/2 transform -translate-y-1/2 bg-gray-300 p-2 rounded-full hover:bg-gray-400"
                            onclick="scrollRight()">
                            ▶
                        </button>
                    </div>
                </div>
                <div class="text-center mt-8 text-gray-400 hover:text-gray-600">
                    <button v-if="showComments" @click="showComments = !showComments">Скрыть</button>
                    <button v-else @click="showComments = !showComments">Посмотреть ещё</button>
                </div>
            </div>
        </section>
    </div> -->
    <div data-aos="fade-down" data-aos-delay="200" class="container  mx-auto overflow-hidden relative">
        <div class="flex overflow-x-scroll scroll-smooth gap-6 lg:gap-10 snap-x px-16 py-6 " ref="commentsContainer" id="commentsContainer" style="scroll-behavior: smooth;">
            <div v-for="comment in comments" :key="comment.id"
                
                class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl duration-300 flex-shrink-0 w-[90%] sm:w-1/2 lg:w-1/3 snap-center">
                <p class="font-semibold">{{ comment.name }}</p>
                <p class="text-yellow-500">{{ comment.stars }}</p>
                <p class="mt-2">{{ comment.text }}</p>
            </div>
        </div>

        <button
            class="absolute left-2 top-1/2 transform -translate-y-1/2 bg-gradient-to-r from-gray-300 to-gray-300 p-3 rounded-full font-bold  text-white shadow-lg transition-transform duration-200 hover:scale-125 disabled:opacity-50"
            @click="scrollLeft" :disabled="isAtStart">
            &lt;
        </button>

        <button
            class="absolute right-2 top-1/2 transform -translate-y-1/2 bg-gradient-to-r from-gray-300 to-gray-300 p-3 rounded-full font-bold  text-white shadow-lg transition-transform duration-200 hover:scale-125 disabled:opacity-50"
            @click="scrollRight" :disabled="isAtEnd">
            &gt;
        </button>
    </div>
</template>

<script setup>
const showComments = ref(false)
const stars = ref('⭐️⭐️⭐️⭐️⭐️')
const starsFour = ref('⭐️⭐️⭐️⭐️')

// const comments = [
//     {
//         id: 1,
//         name: 'Алексей П.',
//         stars: '⭐️⭐️⭐️⭐️⭐️',
//         text: `Отличное качество резки! Заказывал детали для своего проекта, и они были выполнены точно по
//               размерам. Очень доволен!`
//     },
//     {
//         id: 2,
//         name: 'Мария И.',
//         stars: '⭐️⭐️⭐️⭐️⭐️',
//         text: `Сервис на высшем уровне! Быстрая доставка и внимательное отношение к клиентам. Рекомендую
//               всем!`
//     },
//     {
//         id: 3,
//         name: 'Дмитрий К.',
//         stars: '⭐️⭐️⭐️⭐️',
//         text: `Лазерная резка сделана аккуратно, но сроки выполнения немного затянулись. В целом,
//               результат оправдал ожидания!`
//     },
//     {
//         id: 4,
//         name: 'Ольга С.',
//         stars: '⭐️⭐️⭐️⭐️⭐️',
//         text: `Потрясающее качество! Работаете быстро и профессионально. Теперь я ваш постоянный клиент!`
//     },
//     {
//         id: 5,
//         name: 'Игорь Н.',
//         stars: '⭐️⭐️⭐️⭐️⭐️',
//         text: `Заказывал индивидуальные заготовки для своего хобби. Все детали сделаны идеально. Спасибо
//               за вашу работу!`
//     },
//     {
//         id: 6,
//         name: 'Алексей П.',
//         stars: '⭐️⭐️⭐️⭐️⭐️',
//         text: `Отличное качество резки! Заказывал детали для своего проекта, и они были выполнены точно по
//               размерам. Очень доволен!`
//     },
//     {
//         id: 7,
//         name: 'Мария И.',
//         stars: '⭐️⭐️⭐️⭐️⭐️',
//         text: `Сервис на высшем уровне! Быстрая доставка и внимательное отношение к клиентам. Рекомендую
//               всем!`
//     },
//     {
//         id: 8,
//         name: 'Дмитрий К.',
//         stars: '⭐️⭐️⭐️⭐️',
//         text: `Лазерная резка сделана аккуратно, но сроки выполнения немного затянулись. В целом,
//               результат оправдал ожидания!`
//     },
//     {
//         id: 9,
//         name: 'Ольга С.',
//         stars: '⭐️⭐️⭐️⭐️⭐️',
//         text: `Потрясающее качество! Работаете быстро и профессионально. Теперь я ваш постоянный клиент!`
//     },
//     {
//         id: 10,
//         name: 'Игорь Н.',
//         stars: '⭐️⭐️⭐️⭐️⭐️',
//         text: `Заказывал индивидуальные заготовки для своего хобби. Все детали сделаны идеально. Спасибо
//               за вашу работу!`
//     },
// ]

// Инициализация с пустым массивом
const comments = ref([]);

const loadComments = () => {
    // Пример загрузки комментариев. Замените на вашу логику получения данных.
    comments.value = [
        {
            id: 1,
            name: 'Алексей П.',
            stars: '⭐️⭐️⭐️⭐️⭐️',
            text: `Отличное качество резки! Заказывал детали для своего проекта, и они были выполнены точно по
              размерам. Очень доволен!`
        },
        {
            id: 2,
            name: 'Мария И.',
            stars: '⭐️⭐️⭐️⭐️⭐️',
            text: `Сервис на высшем уровне! Быстрая доставка и внимательное отношение к клиентам. Рекомендую
              всем!`
        },
        {
            id: 3,
            name: 'Дмитрий К.',
            stars: '⭐️⭐️⭐️⭐️',
            text: `Лазерная резка сделана аккуратно, но сроки выполнения немного затянулись. В целом,
              результат оправдал ожидания!`
        },
        {
            id: 4,
            name: 'Ольга С.',
            stars: '⭐️⭐️⭐️⭐️⭐️',
            text: `Потрясающее качество! Работаете быстро и профессионально. Теперь я ваш постоянный клиент!`
        },
        {
            id: 5,
            name: 'Игорь Н.',
            stars: '⭐️⭐️⭐️⭐️⭐️',
            text: `Заказывал индивидуальные заготовки для своего хобби. Все детали сделаны идеально. Спасибо
              за вашу работу!`
        },
        {
            id: 6,
            name: 'Светлана Р.',
            stars: '⭐️⭐️⭐️⭐️⭐️',
            text: `Просто великолепно! Заказывала сложные детали для своей мастерской, и все получилось на 100%!`
        },
        {
            id: 7,
            name: 'Иван Т.',
            stars: '⭐️⭐️⭐️⭐️',
            text: `Обращаюсь не в первый раз. Качество хорошее, но иногда бывают небольшие задержки в выполнении. В целом - доволен!`
        },
        {
            id: 8,
            name: 'Наталья Л.',
            stars: '⭐️⭐️⭐️⭐️⭐️',
            text: `Очень радует скорость обработки заказов! Все детали изготовлены идеально. Рекомендую!`
        },
        {
            id: 9,
            name: 'Татьяна К.',
            stars: '⭐️⭐️⭐️⭐️⭐️',
            text: `Превосходная работа команды! Все детали были выполнены точно и быстро. Обязательно вернусь снова!`
        },
    ];
};
loadComments();

const currentIndex = ref(0);
const commentsContainer = ref(null);

const visibleCommentsCount = ref(3); // По умолчанию 3 комментария

const updateVisibleCommentsCount = () => {
  visibleCommentsCount.value = window.innerWidth < 768 ? 1 : 3; // Меняем на 1 для мобильных устройств
};

const visibleComments = computed(() => {
  return comments.value.slice(currentIndex.value, currentIndex.value + visibleCommentsCount.value);
});

const scrollLeft = () => {
  if (currentIndex.value > 0) {
    currentIndex.value -= 1;
    const width = commentsContainer.value.scrollWidth / comments.value.length; // Расчет ширины элемента
    commentsContainer.value.scrollLeft -= width; // Прокрутка влево
  }
};

const scrollRight = () => {
  if (currentIndex.value < comments.value.length - visibleCommentsCount.value) {
    currentIndex.value += 1;
    const width = commentsContainer.value.scrollWidth / comments.value.length; // Расчет ширины элемента
    commentsContainer.value.scrollLeft += width; // Прокрутка вправо
  }
};

const isAtStart = computed(() => currentIndex.value === 0);
const isAtEnd = computed(() => currentIndex.value >= (comments.value.length - visibleCommentsCount.value));

onMounted(() => {
  updateVisibleCommentsCount(); // Установить количество видимых комментариев при монтировании
  window.addEventListener('resize', updateVisibleCommentsCount); // Обновление при изменении размера окна
});

// Удалять обработчик события при размонтировании
onBeforeUnmount(() => {
  window.removeEventListener('resize', updateVisibleCommentsCount);
})
</script>

<style scoped>
.container {
  position: relative;
  overflow-x: auto; /* Включаем горизонтальную прокрутку */
}

#commentsContainer {
  display: flex;

  width: 100%; /* Убедитесь, что контейнер имеет ширину */
}

/* Для Chrome, Safari и Edge */
#commentsContainer::-webkit-scrollbar {
  height: 10px; /* Высота ползунка для горизонтальной прокрутки */
}

#commentsContainer::-webkit-scrollbar-track {
  background: #e0e0e0; /* Цвет трека */
  border-radius: 10px; /* Закругление трека */
}

#commentsContainer::-webkit-scrollbar-thumb {
  background: #888; /* Цвет ползунка */
  border-radius: 10px; /* Закругление ползунка */
}

#commentsContainer::-webkit-scrollbar-thumb:hover {
  background: #555; /* Цвет ползунка при наведении */
}
</style>