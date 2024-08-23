<template>
  <div class="overflow-hidden">
    <!-- Hero section -->
    <section id="hero" class="w-full lg:h-[100vh] pb-6">

      <div class="container mx-auto px-6 ">
        <div class="pt-8  text-center sm:text-left sm:grid sm:grid-cols-6">
          <div class="col-span-3">
            <span data-aos="fade-right" data-aos-once="true"
              class="z-10 relative text-base text-gradient font-semibold uppercase">попробуйте онлайн калькулятор</span>
            <h1 data-aos="fade-right" data-aos-once="true"
              class="z-10 relative text-[2.5rem] mt-4 sm:text-5xl xl:text-6xl font-bold leading-tight">
              Идеальная <span class="text-header-gradient">лазерная резка</span> для вашего бизнеса!
            </h1>
            <div class="sm:hidden z-0 relative scale-120 mt-8 overflow-hidden opacity-90">
              <div class="w-full ">
                <img data-aos="fade-up" data-aos-once="true" src="~/assets/img/steel_3d.webp" class="-mt-4 " alt="" />
              </div>

            </div>
            <p data-aos="fade-down" data-aos-once="true" data-aos-delay="300" class="z-10 relative paragraph mt-8">
              Достигайте точности и эффективности с нашими передовыми технологиями лазерной резки!
            </p>

          </div>
          <div class="hidden sm:block z-0 relative scale-120 mt-8 overflow-hidden opacity-90 col-span-3">
            <div class="w-full ">
              <img data-aos="fade-up" data-aos-once="true" src="~/assets/img/steel_3d.webp" class="-mt-4 " alt="" />
            </div>

          </div>


        </div>
        <div data-aos="fade-up" data-aos-once="true" data-aos-delay="700" class="text-center ">
          <p data-aos="fade-down" data-aos-once="true" data-aos-delay="350" class="mt-8 ">Выберите удобный способ
            связи с нами и получите советы по вашему проекту!</p>
          <button @click="openModal"
            class="z-100 mt-4 p-4  rounded-xl text-white font-bold text-lg hover:cursor-pointer hover:bg-sky-400 bg-sky-500">Запросить
            консультацию</button>

        </div>
      </div>
      <div class="absolute z-0 top-1 left-1 w-[98%] h-[80%] overflow-hidden">
        <div data-aos="fade-up" data-aos-delay="300"
          class="z-0 absolute top-4 sm:top-10 right-64 sm:right-96 xl:right-[3rem] w-6 -rotate-12 ">
          <svg width="40" height="40" class="animate-arrows-h rotate-45 z-0">
            <polyline points="0,40 20,0 40,40 0,40" style="fill:none;stroke:rgba(172, 175, 176, 0.71);stroke-width:2">
            </polyline>
          </svg>
        </div>
        <div data-aos="fade-up" data-aos-delay="900"
          class=" sm:block absolute top-14 sm:top-10 right-4 sm:right-96 xl:right-[10rem] w-6">

          <svg width="80" height="80" class="animate-arrows-rl">
            <polyline points="0,40 20,0 40,40 10,40" style="fill:none;stroke:rgba(180,180,180,0.5);stroke-width:2">
            </polyline>
          </svg>
        </div>
        <div data-aos="fade-up" data-aos-delay="250" class=" hidden sm:block absolute bottom-56 right-24 w-6">

          <svg width="80" height="80" class="animate-arrows-lr -rotate-45">
            <polyline points="30,60 30,0 60,60 30,60" style="fill:none;stroke:rgba(172, 175, 176, 0.71);stroke-width:1">
            </polyline>
          </svg>
        </div>
        <div data-aos="fade-up" data-aos-delay="550" class=" hidden sm:block absolute bottom-22 left-64 w-6">

          <svg width="60" height="60" class="animate-arrows-h ">
            <polyline points="30,40 30,0 60,30 0,20 60,0"
              style="fill:none;stroke:rgba(250, 175, 176, 0.71);stroke-width:2">
            </polyline>
          </svg>
        </div>
        <div data-aos="fade-up" data-aos-delay="200"
          class="hidden sm:block absolute bottom-2 xl:bottom-26 left-[0%] xl:left-2 w-6">
          <svg width="80" height="80" class="animate-arrows-left">
            <polyline points="0,40 20,0 40,40 0,40" style="fill:none;stroke:rgba(0,0,250,0.5);stroke-width:1">
            </polyline>
          </svg>
        </div>

      </div>


    </section>

    <!-- Calculator -->
    <section id="calculator" class="mt-8 container mx-auto ">
      <div data-aos="fade-up" data-aos-once="true" data-aos-delay="200"
        class="text-center text-[2.5rem] sm:text-5xl xl:text-6xl font-bold leading-tight  sm:pr-8 xl:pr-10">
        Рассчитайте свою выгоду!
      </div>
      <p class="p-4">
        Введите параметры вашего проекта, и мы покажем, как наша лазерная резка может сэкономить ваши средства и время.
        Просто заполните несколько полей и получите мгновенный расчет стоимости и сроков выполнения!
      </p>

      <div class="sm:grid sm:grid-cols-5 gap-4">
        <div data-aos="fade-right" data-aos-once="true" data-aos-delay="200"
          class="col-span-2 mt-6 bg-neutral-100 p-4 rounded-xl">

          <div class="dropdown mt-8">
            <p class="dropbtn rounded-xl font-bold text-lg">Материал</p>
            <p>для расчета стоимости укажите материал</p>
            <div class="grid grid-cols-2 p-2 gap-2">
              <p v-for="mat in materials_data" :key="mat.id" @click="material_thickness = 1, material = mat.slug"
                :class="{ 'bg-neutral-200 font-bold': material == mat.slug }"
                class="p-2 mt-2 bg-neutral-300 hover:bg-neutral-200 hover:cursor-pointer border text-center rounded-xl">
                {{ mat.name }}</p>

            </div>
          </div>
          <div class="mt-8">
            <p class="text-lg font-bold">Толщина материала</p>
            <div class="mt-6 flex gap-2">
              <div class="text-lg">{{ material_thickness }} мм</div>
              <div class="">
                <svg width="250" height="30" class="">
                  <polyline points="0,15 400,15" style="fill:none;stroke:rgba(60,60,60,0.5);"
                    :style="{ 'stroke-width': material_thickness }">
                  </polyline>
                </svg>
              </div>
            </div>

            <div class="grid grid-cols-3 p-1 gap-2">
              <p v-for="material in filtred_material_thickness_data" :key="material.id"
                @click="material_thickness = material.thickness"
                :class="{ 'bg-neutral-200 font-bold': material_thickness == material.thickness }"
                class="hover:cursor-pointer bg-neutral-300 hover:bg-neutral-200 sm:ml-6 mt-2 p-2 border rounded-xl text-center">
                {{ material.thickness }}мм
              </p>
            </div>
            <div>
              <p class="text-lg font-bold mt-8">Длина реза(метр погонный)</p>

              <div class="slider-cont">
                <CustomSlider :min="1" :max="5000" v-model="сuttingLength" />
              </div>
            </div>

            <div>
              <p class="text-lg font-bold mt-8">Колличество врезов</p>
              <div class="p-4">
                <p>Когда вырезаем из металла деталь(любой формы) делается один сплошной рез. Если в детали нужны
                  вырезы(перфорация), тогда нужно указать количество врезов</p>
              </div>

              <div class="slider-cont">
                <CustomSlider :min="0" :max="100" v-model="installationCount" />
              </div>
            </div>
          </div>


        </div>

        <div data-aos="fade-left" data-aos-delay="200" class="sticky top-1 mt-8 px-4 text-center self-start">
          <p>стоимость производства будет</p>
          <p class="p-4 text-5xl font-bold">{{ resultPrice }} ₽</p>
          <p>Ориентировочный срок выполнения будет</p>
          <p>
          <p class="p-4 text-5xl font-bold">1 день</p>
          </p>
        </div>
      </div>

    </section>
    <!-- Visual elements -->
    <section id="gallery" class="mt-8  px-4 overflow-hidden">
      <div class="container mx-auto snap-x">
        <div data-aos="fade-up" data-aos-once="true" data-aos-delay="200"
          class="text-center text-[2.0rem] leading-tight">
          <h3 class="pt-8 text-3xl font-bold mb-4 text-neutral-800">Убедитесь сами в нашем качестве!</h3>
        </div>

        <p data-aos="fade-down" data-aos-once="true" data-aos-delay="200" class="mt-4 pb-4 leading text-neutral-800">
          Посмотрите работы,
          выполненные с помощью нашей лазерной резки.
          Здесь вы найдете фотографии и примеры проектов, которые демонстрируют высокую точность и идеальные края,
          обеспеченные нашим оборудованием!</p>


        <div data-aos="fade-left" data-aos-once="true" data-aos-delay="200" v-if="shortList"
          class="relative mx-auto grid grid-flow-col auto-cols-max overflow-x-scroll  align-center mb-4 snap-mandatory snap-x  ">
          <div v-for="i in 25" :key="i" :class='{
            "image-wrapper rounded-sm w-[300px] h-[200px] animate-[scroll_65s_ease-in_infinite] ": isScrolling,
            "image-wrapper rounded-sm snap-center   w-[300px] h-[200px] ": !isScrolling
          }'>
            <img :src="`img/portfolio/${i}.webp`" :alt="`Project ${i}`"
              class="hover:w-auto hover:h-auto hover:cursor-pointer">
          </div>

          <div v-for="i in 25" :key="i" :class='{
            "image-wrapper rounded-sm w-[300px] h-[200px] md:animate-[scroll_65s_ease-in_infinite] ": isScrolling,
            "image-wrapper rounded-sm snap-center w-[300px] h-[200px] ": !isScrolling
          }'>
            <img :src="`img/portfolio/${i}.webp`" :alt="`Project ${i}`"
              class="hover:w-auto hover:h-auto hover:cursor-pointer" @click="">
          </div>
        </div>
        <div v-else class="grid grid-cols-2 gap-2  md:grid-cols-4 align-center mb-4">

          <!-- Генерация изображений -->
          <div v-for="i in 25" :key="i"
            class=" image-wrapper rounded-md w-[300px] h-[200px] md:hover:w-auto md:hover:h-auto duration-700 hover:cursor-pointer">
            <img :src="`img/portfolio/${i}.webp`" :alt="`Project ${i}`"
              class="rounded-sm hover:w-auto hover:h-auto transition-all duration-700 ">
          </div>
        </div>
        <div class="pb-20 mt-20">
          <button v-if="shortList" @click="shortList = !shortList"
            class="w-full bg-neutral-600 text-white font-bold py-2 hover:bg-neutral-500 focus:outline-none focus:ring-2 focus:ring-sky-300 px-4 rounded-xl">Посмотреть
            все</button>
          <button v-else @click="shortList = !shortList"
            class="w-full bg-sky-500 text-white font-bold py-2 hover:bg-sky-600 focus:outline-none focus:ring-2 focus:ring-sky-300 px-4 rounded-xl">Закрыть</button>
        </div>
      </div>
    </section>

    <section class="py-12 px-6 text-center">
      <h2 data-aos="fade-up" data-aos-once="true" data-aos-delay="200" class="text-3xl font-bold mb-4">
        Почему выбирают нас?
      </h2>
      <div data-aos="fade-left" data-aos-delay="200" class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">
          <MdiIcon icon="mdiAtom" :size="'2.5rem'" class="text-green-500 self-center" />

          <div class="col-span-5 text-gray-600 text-md leading mb-2 p-2">
            <p><strong> Высокая точность</strong></p>
            Лазерная резка позволяет достичь идеальной точности даже в самых сложных проектах.
          </div>
        </div>
        <div data-aos="fade-right" data-aos-delay="250"
          class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">
          <MdiIcon icon="mdiShapeOutline" :size="'2.5rem'" class="text-green-500 self-center" />
          <div class="col-span-5 text-gray-600 text-md leading mb-2 p-2">

            <p><strong>Широкий ассортимент металлов</strong> </p>
            Мы работаем с различными материалами – от стали до алюминия, обрабатываем все
            виды металлов.
          </div>
        </div>
        <div data-aos="fade-left" data-aos-delay="200"
          class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">
          <MdiIcon icon="mdiSpeedometer" :size="'2.5rem'" class="text-green-500 self-center" />
          <div class="col-span-5 text-gray-600 text-md  mb-2 p-2">

            <p><strong>Скорость и эффективность</strong></p> Наша команда обеспечивает быстрое выполнение заказов без
            потери качества.
          </div>
        </div>

        <div data-aos="fade-right" data-aos-delay="200"
          class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">
          <MdiIcon icon="mdiAccount" :size="'2.5rem'" class="text-green-500 self-center" />

          <div class="col-span-5 text-gray-600 text-md leading mb-2 p-2">
            <p><strong>Индивидуальный подход</strong></p>
            Мы разрабатываем решения, полностью соответствующие вашим требованиям.
          </div>
        </div>
        <div data-aos="fade-left" data-aos-delay="200"
          class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">
          <MdiIcon icon="mdiWrench" :size="'2.5rem'" class="text-green-500 self-center" />
          <div class="col-span-5 text-gray-600 text-md leading mb-2 p-2">

            <p><strong>Передовые технологии</strong> </p>
            Используем самые новейшие инструменты для достижения максимальных результатов.
          </div>
        </div>
        <div data-aos="fade-up" data-aos-delay="300"
          class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">
          <MdiIcon icon="mdiFaceAgent" :size="'2.5rem'" class="text-green-500 self-center" />
          <div class="col-span-5 text-gray-600 text-md  mb-2 p-2">

            <p><strong>Гарантированная поддержка</strong></p> Наша команда всегда готова помочь вам на каждом этапе.
          </div>
        </div>
      </div>

    </section>
    <section class="py-12 bg-gray-100">
      <div class="container mx-auto">
        <h2 class="text-3xl font-bold text-center mb-8 text-gray-800">Отзывы наших клиентов</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 px-4">
          <div data-aos="fade-right" data-aos-delay="200"
            class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl duration-300">
            <p class="font-semibold">Алексей П.</p>
            <p class="text-yellow-500">⭐️⭐️⭐️⭐️⭐️</p>
            <p class="mt-2">"Отличное качество резки! Заказывал детали для своего проекта, и они были выполнены точно по
              размерам. Очень доволен!"</p>
          </div>
          <div data-aos="fade-up" data-aos-delay="250"
            class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl duration-300">
            <p class="font-semibold">Мария И.</p>
            <p class="text-yellow-500">⭐️⭐️⭐️⭐️⭐️</p>
            <p class="mt-2">"Сервис на высшем уровне! Быстрая доставка и внимательное отношение к клиентам. Рекомендую
              всем!"</p>
          </div>
          <div data-aos="fade-left" data-aos-delay="300"
            class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl duration-300">
            <p class="font-semibold">Дмитрий К.</p>
            <p class="text-yellow-500">⭐️⭐️⭐️⭐️</p>
            <p class="mt-2">"Лазерная резка сделана аккуратно, но сроки выполнения немного затянулись. В целом,
              результат оправдал ожидания!"</p>
          </div>
          <div v-show="showComments" class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl duration-300">
            <p class="font-semibold">Ольга С.</p>
            <p class="text-yellow-500">⭐️⭐️⭐️⭐️⭐️</p>
            <p class="mt-2">"Потрясающее качество! Работаете быстро и профессионально. Теперь я ваш постоянный клиент!"
            </p>
          </div>
          <div v-show="showComments" class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl duration-300">
            <p class="font-semibold">Игорь Н.</p>
            <p class="text-yellow-500">⭐️⭐️⭐️⭐️⭐️</p>
            <p class="mt-2">"Заказывал индивидуальные заготовки для своего хобби. Все детали сделаны идеально. Спасибо
              за вашу работу!"</p>
          </div>
        </div>
        <div class="text-center mt-8 text-gray-400 hover:text-gray-600">
          <button v-if="showComments" @click="showComments = !showComments">Скрыть</button>
          <button v-else @click="showComments = !showComments">Посмотреть ещё</button>
        </div>
      </div>
    </section>
    <section class="flex flex-col items-center justify-center px-8 bg-gray-100">
      <h2 data-aos="fade-up" data-aos-once="true" data-aos-delay="300"
        class="text-2xl font-semibold  mb-4 text-gray-800">Готовы начать?</h2>
      <p data-aos="fade-right" data-aos-delay="300" class="mb-6 text-gray-800">
        Нажмите на кнопку ниже и получите бесплатную консультацию по вашим проектам лазерной резки!
      </p>
      <div class="flex space-x-4">
        <button @click="openModal"
          class="px-6 py-3 w-full bg-sky-500 text-white font-bold  rounded-xl hover:bg-sky-600 focus:outline-none focus:ring-2 focus:ring-sky-300">
          Получить расчет
        </button>
      </div>
    </section>
    <ContactForm />
    <section>
      <div class="my-8 p-6 mx-4 bg-gray-100 rounded-lg shadow-lg">
        <h3 class="text-lg font-semibold  text-gray-800">Интересно узнать больше?</h3>
        <p class="mt-2 text-gray-800">
          <span class="italic">Скачайте наше бесплатное руководство: "10 преимуществ лазерной резки металла". Узнайте,
            как наши технологии могут изменить вашу эффективность и качество производства!</span>
        </p>
      </div>

      <div class="my-8 p-6 mx-4 bg-gray-100 rounded-lg shadow-lg">
        <h3 class="text-lg font-semibold text-gray-800">Мы на вашей стороне!</h3>
        <p class="mt-2 text-gray-800">

          <span class="italic">Мы уверены в качестве наших услуг. Если вас что-то не устраивает, мы обязательно найдем
            решение!</span>
        </p>
      </div>
    </section>
    <!-- FAQ section -->
    <section class="flex flex-col items-center justify-center px-8 py-8 bg-gray-100">
      <h2 data-aos="fade-up" data-aos-once="true" data-aos-delay="300"
        class="text-2xl font-semibold  mb-4 text-gray-800">Частые вопросы</h2>
      <div v-for="f in faq" :key="f.id">
        <div data-aos="fade-left" data-aos-delay="200" class="question container mt-4 relative">
          <div class="avatar absolute -top-4 -left-2">
            <MdiIcon icon="mdiAccountCircle" :size="'2.5rem'" class="text-blue-900 self-center" />
          </div>
          <div
            class="question-text hover:shadow-xl duration-300 ml-6 pt-4 rounded-tr-xl rounded-br-xl rounded-bl-xl p-4 w-[40%] bg-blue-200/60">
            {{ f.question }}</div>
          <div data-aos="fade-right" data-aos-delay="300" class="answer mt-4 relative ml-[30%]">
            <div class="avatarLogo absolute -top-4 -right-6">
              <MdiIcon icon="mdiAccountCircle" :size="'2.5rem'" class="text-green-900 self-center" />
            </div>
            <div
              class="answer-text hover:shadow-xl duration-300 rounded-tl-xl rounded-br-xl rounded-bl-xl p-4  bg-green-200/60">
              {{ f.answer }}
            </div>

          </div>
        </div>
      </div>

    </section>
    <footer class="relative  bg-neutral-600 p-6 pt-32">
      <div class="container mx-auto">
        <div data-aos="fade-up" data-aos-once="true" data-aos-delay="700" class="text-center ">
          <p data-aos="fade-down" data-aos-once="true" data-aos-delay="350" class="text-neutral-100 ">Выберите удобный
            способ
            связи с нами и получите советы по вашему проекту!</p>
          <button @click="openModal"
            class="z-100 mt-4 p-4  rounded-xl text-white font-bold text-lg hover:cursor-pointer hover:bg-sky-400 bg-sky-500">Запросить
            консультацию</button>

        </div>

      </div>
      <div class="footer-content container mx-auto grid sm:grid-cols-2 p-4 mb-4 mt-12 text-sm text-neutral-200">
        <div class="p-4">
          <h3>Группа компаний Иверстрой (ГК Иверстрой)</h3>
          <p>© 2024 ООО "Иверстрой". Все права защищены.</p>
          <h4>Контактные данные</h4>
          <p>Телефон: <a href="tel:+79169662390">8-916-966-23-90</a></p>
        </div>
       <div class="p-4">
        <h4>Юридическая информация</h4>
        <p>Юридический адрес: 129345, Москва, Осташковская ул, дом 14, строение 5, этаж 3, помещение I, комната 15</p>
        <h4>Реквизиты</h4>
        <p>ИНН: 7716751561</p>
        <p>КПП: 771601001</p>
        <p>ОГРН: 1137746705832</p>
        <p>ОКПО: 17969219</p>
        <h4>Генеральный директор</h4>
        <p>Парамонов Сергей Николаевич</p>
       </div>
      </div>
    </footer>

    <ContactModal :isOpen="isModalOpen" @close="closeModal" />



  </div>
</template>

<script setup>
onMounted(() => {
  // Устанавливаем плавный скролл
  document.documentElement.style.scrollBehavior = 'smooth';
})

const material = ref('steel')
const material_thickness = ref(1)
const installationCount = ref(0)
const сuttingLength = ref(1);
const showComments = ref(false)
const isScrolling = ref(true)
const isModalOpen = ref(false);

const openModal = () => {
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
};
// a computed ref
const resultPrice = computed(() => {
  return calculatePrice()
  // return material_thickness.value * installationCount.value > 0 ? 'Yes' : '?'
})
const filtred_material_thickness_data = computed(() => {
  if (material.value) {
    let filtred_data = material_thickness_data.filter(data => data.material.includes(material.value))
    // console.log(filtred_data)
    return filtred_data

  }
  return material_thickness_data

})
const shortList = ref(true)

const imagesCount = 4; // Начальное количество изображений
const imageArrayLength = ref(4);
const imageArray = computed(() => Array.from({ length: imageArrayLength.value }, (_, i) => i + 1));

const materials_data = [
  { id: 1, name: 'сталь', slug: 'steel' },
  { id: 2, name: 'нержавека', slug: 'stainless_steel' },
  { id: 3, name: 'алюминий', slug: 'aluminum' },
  { id: 4, name: 'дюраль', slug: 'duralumin' },
  { id: 5, name: 'титан', slug: 'titanium' },
  { id: 6, name: 'медь', slug: 'copper' },
  { id: 7, name: 'латунь', slug: 'brass' },
]
const material_thickness_data =
  [
    { id: 1, thickness: 0.8, material: ['steel', 'stainless_steel'] },
    { id: 2, thickness: 1, material: ['steel', 'aluminum', 'duralumin', 'titanium', 'copper', 'brass', 'stainless_steel'] },
    { id: 3, thickness: 1.5, material: ['steel', 'aluminum', 'duralumin', 'titanium', 'copper', 'brass', 'stainless_steel'] },
    { id: 4, thickness: 2, material: ['steel', 'aluminum', 'duralumin', 'titanium', 'copper', 'brass', 'stainless_steel'] },
    { id: 5, thickness: 2.5, material: ['steel',] },
    { id: 6, thickness: 3, material: ['steel', 'aluminum', 'duralumin', 'titanium', 'copper', 'brass', 'stainless_steel'] },
    { id: 7, thickness: 4, material: ['steel', 'aluminum', 'duralumin', 'titanium', 'copper', 'brass', 'stainless_steel'] },
    { id: 8, thickness: 5, material: ['steel', 'aluminum', 'duralumin', 'copper', 'brass', 'stainless_steel'] },
    { id: 9, thickness: 6, material: ['steel', 'aluminum', 'duralumin', 'stainless_steel'] },
    { id: 10, thickness: 8, material: ['steel'] },
    { id: 11, thickness: 10, material: ['steel'] },
    { id: 12, thickness: 12, material: ['steel'] },
    { id: 14, thickness: 16, material: ['steel'] },

  ]


function calculatePrice() {
  if (material.value && material_thickness.value && сuttingLength.value) {

    let materialCutPrice = calculateMaterialThuckness()

    let installationPrice = 0
    if (installationCount.value > 0) {
      switch (material_thickness.value) {
        case 0.8: installationPrice = 2 * installationCount.value; break
        case 1: installationPrice = 2 * installationCount.value; break
        case 1.5: installationPrice = 2 * installationCount.value; break
        case 2: installationPrice = 2 * installationCount.value; break
        case 2.5: installationPrice = 2 * installationCount.value; break
        case 3: installationPrice = 2 * installationCount.value; break
        case 4: installationPrice = 2 * installationCount.value; break
        case 5: installationPrice = 3 * installationCount.value; break
        case 6: installationPrice = 3 * installationCount.value; break
        case 8: installationPrice = 3 * installationCount.value; break
        case 10: installationPrice = 3 * installationCount.value; break
        case 12: installationPrice = 6 * installationCount.value; break
        case 16: installationPrice = 6 * installationCount.value; break
      }
    }

    return installationPrice + (сuttingLength.value * materialCutPrice)
  }
  return 200
}
function calculateMaterialThuckness() {
  if (material.value && material_thickness.value) {
    let tempPrice = 0
    if (material.value == 'steel') {
      switch (material_thickness.value) {
        case 0.8: tempPrice = 20; break
        case 1: tempPrice = 20; break
        case 1.5: tempPrice = 25; break
        case 2: tempPrice = 30; break
        case 2.5: tempPrice = 35; break
        case 3: tempPrice = 46; break
        case 4: tempPrice = 51; break
        case 5: tempPrice = 61; break
        case 6: tempPrice = 69; break
        case 8: tempPrice = 89; break
        case 10: tempPrice = 128; break
        case 12: tempPrice = 160; break
        case 16: tempPrice = 295; break
      }
    }
    if (material.value == 'aluminum' || material.value == 'duralumin') {
      switch (material_thickness.value) {
        case 1: tempPrice = 35; break
        case 1.5: tempPrice = 45; break
        case 2: tempPrice = 65; break
        case 3: tempPrice = 85; break
        case 4: tempPrice = 110; break
        case 5: tempPrice = 144; break
        case 6: tempPrice = 220; break
      }
    }
    if (material.value == 'titanium') {
      switch (material_thickness.value) {
        case 1: tempPrice = 42; break
        case 1.5: tempPrice = 57; break
        case 2: tempPrice = 67; break
        case 3: tempPrice = 77; break
        case 4: tempPrice = 87; break
      }
    }
    if (material.value == 'copper') {
      switch (material_thickness.value) {
        case 1: tempPrice = 45; break
        case 1.5: tempPrice = 70; break
        case 2: tempPrice = 98; break
        case 3: tempPrice = 165; break
        case 4: tempPrice = 180; break
        case 5: tempPrice = 240; break
      }
    }
    if (material.value == 'brass') {
      switch (material_thickness.value) {
        case 1: tempPrice = 32; break
        case 1.5: tempPrice = 55; break
        case 2: tempPrice = 70; break
        case 3: tempPrice = 85; break
        case 4: tempPrice = 104; break
        case 5: tempPrice = 144; break
        case 6: tempPrice = 215; break
        case 8: tempPrice = 335; break
        case 10: tempPrice = 443; break
      }
    }
    if (material.value == 'stainless_steel') {
      switch (material_thickness.value) {
        case 0.8: tempPrice = 35; break
        case 1: tempPrice = 35; break
        case 1.5: tempPrice = 45; break
        case 2: tempPrice = 65; break
        case 3: tempPrice = 85; break
        case 4: tempPrice = 110; break
        case 5: tempPrice = 144; break
        case 6: tempPrice = 220; break
      }
    }

    return tempPrice
  }
}

const faq = [
  {
    id: 1,
    question: "Что такое лазерная резка?",
    answer: "Лазерная резка — это процесс использования концентрированного лазерного луча для резки материалов. Он обеспечивает высокую точность и чистые края, что делает его идеальным для различных промышленных приложений."
  },
  {
    id: 2,
    question: "Какие материалы можно резать с помощью лазера?",
    answer: "Лазерная резка подходит для многих материалов, включая дерево, акрил, металл, кожу и картоон. Однако важно учитывать специфику каждого материала для достижения лучших результатов."
  },
  {
    id: 3,
    question: "Каковы преимущества лазерной резки?",
    answer: "Лазерная резка предлагает несколько преимуществ, включая высокую точность, минимальное тепловое воздействие на материал, возможность создания сложных форм и быстрое выполнение заказов."
  },
  {
    id: 4,
    question: "Каковы ограничения лазерной резки?",
    answer: "Некоторые ограничения включают толщину материала, тип и свойства используемых материалов. Например, очень толстые металлы могут быть сложнее в обработке."
  },
  {
    id: 5,
    question: "Какой минимальный объем заказа необходим для лазерной резки?",
    answer: "Объем заказа может варьироваться в зависимости от компании. В нашей практике мы принимаем как крупные, так и малые заказы, включая единичные изделия."
  },
  {
    id: 6,
    question: "Как долго длится процесс резки?",
    answer: "Время обработки зависит от сложности заказа, материала и его толщины. Однако лазерная резка обычно происходит достаточно быстро, позволяя выполнить заказы в короткие сроки."
  },
  {
    id: 7,
    question: "Как подготовить файл для лазерной резки?",
    answer: "Для оптимальной обработки файл должен быть в формате векторной графики (например, .SVG или .DXF). Убедитесь, что размеры ваших элементов соответствуют необходимым параметрам."
  },
  {
    id: 8,
    question: "Какие у вас политики по возвратам и обменам?",
    answer: "Мы стремимся к удовлетворенности клиентов. Возвраты и обмены возможны в случае производственного брака или неверного исполнения заказа, при условии, что вы уведомите нас в течение 7 дней после получения."
  }
];


</script>
<style scoped>
@import url(https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200);


.text-header-gradient {
  background: rgb(57, 132, 244);
  background: linear-gradient(169.4deg, #3984f4 -6.01%, #0cd3ff 36.87%, #2f7cf0 78.04%, #0e65e8 103.77%);
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.bg-partner {
  background: url('../assets/img/partner/background.png');
  background-size: cover;
  background-position: center;
}

.bg-trading-tools {
  background: url('../assets/img/bg-trading-tools.webp');
  background-size: cover;
  background-position: center;
}

#hero {
  background-color: #E6FAFF;
  /* color: #acafb0b6; */
}

#gallery {
  background-color: #D4D4D4;
}

.animate-arrows-rl {
  animation: arrows-rl 30s ease-in-out infinite;
}

.animate-arrows-left {
  animation: arrows-left 20s ease-in-out infinite;
}

.animate-arrows-lr {
  animation: arrows-lr 40s ease-in-out infinite;
}

.animate-arrows-h {
  animation: arrows-h 40s ease-in-out infinite;
}


@keyframes arrows-rl {
  0% {
    transform: rotate(0deg) translateX(0rem) translateY(0rem);
  }

  40% {
    transform: rotate(180deg) translateX(-10rem) translateY(10rem);
  }

  50% {
    transform: rotate(0deg) translateX(-2rem) translateY(3rem);
  }

  80% {
    transform: rotate(360deg) translateX(2rem) translateY(7rem);
    ;
  }

  100% {
    transform: rotate(0deg) translateX(0rem) translateY(0rem);
  }
}

@keyframes arrows-left {
  from {
    transform: rotate(360deg);
  }

  to {
    transform: rotate(0deg);
  }
}

@keyframes arrows-lr {
  0% {
    transform: rotate(360deg) translateX(0rem) translateY(0rem);
  }

  40% {
    transform: rotate(180deg) translateX(5rem) translateY(5rem);
  }

  50% {
    transform: rotate(360deg) translateX(-2rem) translateY(-5rem);
  }

  80% {
    transform: rotate(0deg) translateX(1rem) translateY(3rem);
    ;
  }

  100% {
    transform: rotate(360deg) translateX(0rem) translateY(0rem);
  }
}

@keyframes arrows-h {
  0% {
    transform: rotate(60deg) translateX(0rem) translateY(0rem);
  }

  40% {
    transform: rotate(0deg) translateX(7rem) translateY(4rem);
  }

  50% {
    transform: rotate(360deg) translateX(-6rem) translateY(-5rem);
  }

  80% {
    transform: rotate(0deg) translateX(4rem) translateY(5rem);
    ;
  }

  100% {
    transform: rotate(60deg) translateX(0rem) translateY(0rem);
  }
}

/* Стили для эффекта наведения */
.image-wrapper {
  display: flex;
  justify-content: center;
  /* Центрирование по горизонтали */
  align-items: center;
  /* Центрирование по вертикали */
  /* max-width: 300px; */
  /* Укажите нужную ширину */
  /* max-height: 200px; */
  /* Укажите нужную высоту */
  overflow: hidden;
  /* background-color: #f0f0f0; Цвет фона для наглядности */
}

.image-wrapper img {
  transition: transform 0.3s ease;
  filter: grayscale(100%);
}

.image-wrapper:hover img {
  transform: scale(1.1);
  filter: none;
  /* Убираем градацию серого при наведении */
}

.image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  /* Сохраняет пропорции изображения */
}

.carousel {
  overflow: hidden;
  width: 300px;
  /* Ширина контейнера */
  height: 200px;
  /* Высота контейнера */
  position: relative;
}

.carousel-inner {

  overflow: hidden;
  animation: scroll 15s linear infinite;
  /* Длительность скролла */
}

.carousel-inner img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  /* Сохраняет пропорции изображения */
}

@keyframes scroll {
  0% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(-100%);
    /* Перемещение на ширину всего содержимого */
  }
}

/* Изменение стиля полосы прокрутки для WebKit */
::-webkit-scrollbar {
  height: 10px;
  /* Измените высоту полосы прокрутки */
}

::-webkit-scrollbar-thumb {
  background: #888;
  /* Цвет ползунка */
  border-radius: 5px;
  /* Скругление углов */
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
  /* Цвет ползунка при наведении */
}
</style>