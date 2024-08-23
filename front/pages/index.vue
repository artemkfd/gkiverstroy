<template>
  <div class="overflow-hidden">
    <!-- Hero section -->
    <section id="hero" class="w-full lg:h-[100vh] pb-6">

      <div class="container mx-auto px-6 ">
        <div class="pt-8  text-center sm:text-left sm:grid sm:grid-cols-6">
          <div class="col-span-3">
            <span data-aos="fade-right" data-aos-once="true" data-aos-delay="150"
              class="z-10 relative text-base text-gradient font-semibold uppercase">попробуйте онлайн калькулятор</span>
            <h1 data-aos="fade-right" data-aos-once="true"
              class="z-10 relative text-[2.5rem] mt-4 sm:text-5xl xl:text-6xl font-bold leading-tight">
              Идеальная <span data-aos="fade-up" data-aos-once="true"  data-aos-delay="250" class="text-header-gradient">лазерная резка</span> для вашего бизнеса!
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
          class="col-span-2 mt-6 min-h-[300px] bg-neutral-100 p-4 rounded-xl">

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

        <div data-aos="fade-left" data-aos-delay="200" class="mt-8 px-4 text-center self-center">
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
            class=" image-wrapper rounded-md w-[300px] h-[200px] md:hover:w-max-[400px] md:hover:h-max-[300px] duration-700 hover:cursor-pointer">
            <img :src="`img/portfolio/${i}.webp`" :alt="`Project ${i}`"
              class="rounded-sm hover:w-auto hover:h-auto transition-all duration-700 ">
          </div>
        </div>
        <div class="pb-20 mt-20">
          <button v-if="shortList" @click="shortList = !shortList"
            class="w-full bg-neutral-600 text-white font-bold py-2 hover:bg-neutral-500 focus:outline-none focus:ring-2 focus:ring-sky-300 px-4 rounded-xl">Посмотреть
            все</button>
          <button v-else @click="shortList = !shortList"
            class="w-full bg-neutral-600 text-white font-bold py-2 hover:bg-neutral-500 focus:outline-none focus:ring-2 focus:ring-sky-300 px-4 rounded-xl">Закрыть</button>
        </div>
      </div>
    </section>

    <section class="py-12 px-6 text-center">
      <h2 data-aos="fade-up" data-aos-once="true" data-aos-delay="200" class="text-3xl font-bold mb-4">
        Почему выбирают нас?
      </h2>
      <div data-aos="fade-left" data-aos-delay="200" class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">
   
          <svg xmlns="http://www.w3.org/2000/svg" class="text-green-500 h-10 w-10 self-center" viewBox="0 0 24 24"><path fill="currentColor" d="M12,11A1,1 0 0,1 13,12A1,1 0 0,1 12,13A1,1 0 0,1 11,12A1,1 0 0,1 12,11M4.22,4.22C5.65,2.79 8.75,3.43 12,5.56C15.25,3.43 18.35,2.79 19.78,4.22C21.21,5.65 20.57,8.75 18.44,12C20.57,15.25 21.21,18.35 19.78,19.78C18.35,21.21 15.25,20.57 12,18.44C8.75,20.57 5.65,21.21 4.22,19.78C2.79,18.35 3.43,15.25 5.56,12C3.43,8.75 2.79,5.65 4.22,4.22M15.54,8.46C16.15,9.08 16.71,9.71 17.23,10.34C18.61,8.21 19.11,6.38 18.36,5.64C17.62,4.89 15.79,5.39 13.66,6.77C14.29,7.29 14.92,7.85 15.54,8.46M8.46,15.54C7.85,14.92 7.29,14.29 6.77,13.66C5.39,15.79 4.89,17.62 5.64,18.36C6.38,19.11 8.21,18.61 10.34,17.23C9.71,16.71 9.08,16.15 8.46,15.54M5.64,5.64C4.89,6.38 5.39,8.21 6.77,10.34C7.29,9.71 7.85,9.08 8.46,8.46C9.08,7.85 9.71,7.29 10.34,6.77C8.21,5.39 6.38,4.89 5.64,5.64M9.88,14.12C10.58,14.82 11.3,15.46 12,16.03C12.7,15.46 13.42,14.82 14.12,14.12C14.82,13.42 15.46,12.7 16.03,12C15.46,11.3 14.82,10.58 14.12,9.88C13.42,9.18 12.7,8.54 12,7.97C11.3,8.54 10.58,9.18 9.88,9.88C9.18,10.58 8.54,11.3 7.97,12C8.54,12.7 9.18,13.42 9.88,14.12M18.36,18.36C19.11,17.62 18.61,15.79 17.23,13.66C16.71,14.29 16.15,14.92 15.54,15.54C14.92,16.15 14.29,16.71 13.66,17.23C15.79,18.61 17.62,19.11 18.36,18.36Z" /></svg>

          <div class="col-span-5 text-gray-600 text-md leading mb-2 p-2">
            <p><strong> Высокая точность</strong></p>
            Лазерная резка позволяет достичь идеальной точности даже в самых сложных проектах.
          </div>
        </div>
        <div data-aos="fade-right" data-aos-delay="250"
          class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">
          <svg xmlns="http://www.w3.org/2000/svg" class="text-green-500 h-10 w-10 self-center" viewBox="0 0 24 24"><title>shape-outline</title><path fill="currentColor" d="M11,13.5V21.5H3V13.5H11M9,15.5H5V19.5H9V15.5M12,2L17.5,11H6.5L12,2M12,5.86L10.08,9H13.92L12,5.86M17.5,13C20,13 22,15 22,17.5C22,20 20,22 17.5,22C15,22 13,20 13,17.5C13,15 15,13 17.5,13M17.5,15A2.5,2.5 0 0,0 15,17.5A2.5,2.5 0 0,0 17.5,20A2.5,2.5 0 0,0 20,17.5A2.5,2.5 0 0,0 17.5,15Z" /></svg>
          <div class="col-span-5 text-gray-600 text-md leading mb-2 p-2">

            <p><strong>Широкий ассортимент металлов</strong> </p>
            Мы работаем с различными материалами – от стали до алюминия, обрабатываем все
            виды металлов.
          </div>
        </div>
        <div data-aos="fade-left" data-aos-delay="200"
          class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">
          <svg xmlns="http://www.w3.org/2000/svg" class="text-green-500 h-10 w-10 self-center" viewBox="0 0 24 24"><title>speedometer</title><path fill="currentColor" d="M12,16A3,3 0 0,1 9,13C9,11.88 9.61,10.9 10.5,10.39L20.21,4.77L14.68,14.35C14.18,15.33 13.17,16 12,16M12,3C13.81,3 15.5,3.5 16.97,4.32L14.87,5.53C14,5.19 13,5 12,5A8,8 0 0,0 4,13C4,15.21 4.89,17.21 6.34,18.65H6.35C6.74,19.04 6.74,19.67 6.35,20.06C5.96,20.45 5.32,20.45 4.93,20.07V20.07C3.12,18.26 2,15.76 2,13A10,10 0 0,1 12,3M22,13C22,15.76 20.88,18.26 19.07,20.07V20.07C18.68,20.45 18.05,20.45 17.66,20.06C17.27,19.67 17.27,19.04 17.66,18.65V18.65C19.11,17.2 20,15.21 20,13C20,12 19.81,11 19.46,10.1L20.67,8C21.5,9.5 22,11.18 22,13Z" /></svg>
          <div class="col-span-5 text-gray-600 text-md  mb-2 p-2">

            <p><strong>Скорость и эффективность</strong></p> Наша команда обеспечивает быстрое выполнение заказов без
            потери качества.
          </div>
        </div>

        <div data-aos="fade-right" data-aos-delay="200"
          class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">
          <svg xmlns="http://www.w3.org/2000/svg" class="text-green-500 h-10 w-10 self-center" viewBox="0 0 24 24"><title>account</title><path fill="currentColor" d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" /></svg>

          <div class="col-span-5 text-gray-600 text-md leading mb-2 p-2">
            <p><strong>Индивидуальный подход</strong></p>
            Мы разрабатываем решения, полностью соответствующие вашим требованиям.
          </div>
        </div>
        <div data-aos="fade-left" data-aos-delay="200"
          class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">

          <svg xmlns="http://www.w3.org/2000/svg" class="text-green-500 h-10 w-10 self-center" viewBox="0 0 24 24"><title>wrench</title><path fill="currentColor" d="M22.7,19L13.6,9.9C14.5,7.6 14,4.9 12.1,3C10.1,1 7.1,0.6 4.7,1.7L9,6L6,9L1.6,4.7C0.4,7.1 0.9,10.1 2.9,12.1C4.8,14 7.5,14.5 9.8,13.6L18.9,22.7C19.3,23.1 19.9,23.1 20.3,22.7L22.6,20.4C23.1,20 23.1,19.3 22.7,19Z" /></svg>
          <div class="col-span-5 text-gray-600 text-md leading mb-2 p-2">

            <p><strong>Передовые технологии</strong> </p>
            Используем самые новейшие инструменты для достижения максимальных результатов.
          </div>
        </div>
        <div data-aos="fade-up" data-aos-delay="300"
          class=" bg-white shadow-md hover:shadow-xl duration-300 p-4 rounded-lg grid grid-cols-6">

          <svg xmlns="http://www.w3.org/2000/svg" class="text-green-500 h-10 w-10 self-center" viewBox="0 0 24 24"><title>face-agent</title><path fill="currentColor" d="M18.72,14.76C19.07,13.91 19.26,13 19.26,12C19.26,11.28 19.15,10.59 18.96,9.95C18.31,10.1 17.63,10.18 16.92,10.18C13.86,10.18 11.15,8.67 9.5,6.34C8.61,8.5 6.91,10.26 4.77,11.22C4.73,11.47 4.73,11.74 4.73,12A7.27,7.27 0 0,0 12,19.27C13.05,19.27 14.06,19.04 14.97,18.63C15.54,19.72 15.8,20.26 15.78,20.26C14.14,20.81 12.87,21.08 12,21.08C9.58,21.08 7.27,20.13 5.57,18.42C4.53,17.38 3.76,16.11 3.33,14.73H2V10.18H3.09C3.93,6.04 7.6,2.92 12,2.92C14.4,2.92 16.71,3.87 18.42,5.58C19.69,6.84 20.54,8.45 20.89,10.18H22V14.67H22V14.69L22,14.73H21.94L18.38,18L13.08,17.4V15.73H17.91L18.72,14.76M9.27,11.77C9.57,11.77 9.86,11.89 10.07,12.11C10.28,12.32 10.4,12.61 10.4,12.91C10.4,13.21 10.28,13.5 10.07,13.71C9.86,13.92 9.57,14.04 9.27,14.04C8.64,14.04 8.13,13.54 8.13,12.91C8.13,12.28 8.64,11.77 9.27,11.77M14.72,11.77C15.35,11.77 15.85,12.28 15.85,12.91C15.85,13.54 15.35,14.04 14.72,14.04C14.09,14.04 13.58,13.54 13.58,12.91A1.14,1.14 0 0,1 14.72,11.77Z" /></svg>
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
          <div class="avatar absolute -top-8 -left-2">
            <div class="w-12 h-12 p-1 rounded-xl bg-sky-500/80 border-2 border-sky-500">
              <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-100  w-10 h-10 self-center" viewBox="0 0 24 24"><title>chat-question-outline</title><path fill="currentColor" d="M12 3C6.5 3 2 6.6 2 11C2 13.2 3.1 15.2 4.8 16.5C4.8 17.1 4.4 18.7 2 21C4.4 20.9 6.6 20 8.5 18.5C9.6 18.8 10.8 19 12 19C17.5 19 22 15.4 22 11S17.5 3 12 3M12 17C7.6 17 4 14.3 4 11S7.6 5 12 5 20 7.7 20 11 16.4 17 12 17M12.2 6.5C11.3 6.5 10.6 6.7 10.1 7C9.5 7.4 9.2 8 9.3 8.7H11.3C11.3 8.4 11.4 8.2 11.6 8.1C11.8 8 12 7.9 12.3 7.9C12.6 7.9 12.9 8 13.1 8.2C13.3 8.4 13.4 8.6 13.4 8.9C13.4 9.2 13.3 9.4 13.2 9.6C13 9.8 12.8 10 12.6 10.1C12.1 10.4 11.7 10.7 11.5 10.9C11.1 11.2 11 11.5 11 12H13C13 11.7 13.1 11.5 13.1 11.3C13.2 11.1 13.4 11 13.6 10.8C14.1 10.6 14.4 10.3 14.7 9.9C15 9.5 15.1 9.1 15.1 8.7C15.1 8 14.8 7.4 14.3 7C13.9 6.7 13.1 6.5 12.2 6.5M11 13V15H13V13H11Z" /></svg>
            </div>
          </div>
          <div
            class="question-text hover:shadow-xl duration-300 ml-6 pt-4 rounded-tr-xl rounded-br-xl rounded-bl-xl p-4 mr-[30%] bg-blue-200/60">
            {{ f.question }}</div>
          <div data-aos="fade-right" data-aos-delay="300" class="answer mt-4 relative ml-[30%]">
            <div class="avatarLogo absolute -top-4 -right-6">
       
              <div class="w-12 h-12 p-1 rounded-xl bg-green-400/80 border-2 border-green-400">
                <svg xmlns="http://www.w3.org/2000/svg" class="text-gray-100 h-10 w-10 self-center" viewBox="0 0 24 24"><title>face-agent</title><path fill="currentColor" d="M18.72,14.76C19.07,13.91 19.26,13 19.26,12C19.26,11.28 19.15,10.59 18.96,9.95C18.31,10.1 17.63,10.18 16.92,10.18C13.86,10.18 11.15,8.67 9.5,6.34C8.61,8.5 6.91,10.26 4.77,11.22C4.73,11.47 4.73,11.74 4.73,12A7.27,7.27 0 0,0 12,19.27C13.05,19.27 14.06,19.04 14.97,18.63C15.54,19.72 15.8,20.26 15.78,20.26C14.14,20.81 12.87,21.08 12,21.08C9.58,21.08 7.27,20.13 5.57,18.42C4.53,17.38 3.76,16.11 3.33,14.73H2V10.18H3.09C3.93,6.04 7.6,2.92 12,2.92C14.4,2.92 16.71,3.87 18.42,5.58C19.69,6.84 20.54,8.45 20.89,10.18H22V14.67H22V14.69L22,14.73H21.94L18.38,18L13.08,17.4V15.73H17.91L18.72,14.76M9.27,11.77C9.57,11.77 9.86,11.89 10.07,12.11C10.28,12.32 10.4,12.61 10.4,12.91C10.4,13.21 10.28,13.5 10.07,13.71C9.86,13.92 9.57,14.04 9.27,14.04C8.64,14.04 8.13,13.54 8.13,12.91C8.13,12.28 8.64,11.77 9.27,11.77M14.72,11.77C15.35,11.77 15.85,12.28 15.85,12.91C15.85,13.54 15.35,14.04 14.72,14.04C14.09,14.04 13.58,13.54 13.58,12.91A1.14,1.14 0 0,1 14.72,11.77Z" /></svg>
              </div>
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