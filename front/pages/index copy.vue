<template>
    <div class="w-full ">
      <!-- Hero section -->
      <section id="hero" class="w-full lg:p-12 lg:pb-24 flex overflow-hidden">
      
          <div class="container overflow-hidden">
            <div class="col-span-12 lg:col-span-6 pt-24 mt-12 xl:mt-10 space-y-4 sm:space-y-6 px-6 text-center sm:text-left">
              <span data-aos="fade-right" data-aos-once="true" class="text-base text-gradient font-semibold uppercase"
                >попробуй онлайн калькулятор</span
              >
              <h1
                data-aos="fade-right"
                data-aos-once="true"
                class="text-[2.5rem] sm:text-5xl xl:text-6xl font-bold leading-tight  sm:pr-8 xl:pr-10"
              >
              Идеальная <span class="text-header-gradient">лазерная резка</span> для вашего бизнеса!
              </h1>
              <p data-aos="fade-down" data-aos-once="true" data-aos-delay="300" class="paragraph hidden sm:block">
                Узнай сколько будет стоить вырезать деталь быстро
              </p>
              <div
                data-aos="fade-up"
                data-aos-once="true"
                data-aos-delay="700"
                class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4 mt-2"
              >
              <button class="z-100 p-4 rounded-full text-white font-bold text-lg hover:cursor-pointer hover:bg-sky-400 bg-sky-500">Начать </button>
        
              </div>
            </div>
          </div>
          <div class="z-10 hidden sm:block col-span-12 lg:col-span-6 opacity-100">
            <div class="w-full ">
              <img
                data-aos="fade-up"
                data-aos-once="true"
                src="~/assets/img/steel_3d.webp"
                class="-mt-4 "
                alt=""
              />
            </div>
            
          </div>

      </section>
      <div class="absolute top-1 left-1 w-[99.5%] h-[80%] overflow-hidden">
            <div  
              data-aos="fade-up"
              data-aos-delay="300"
              class="z-0 absolute top-4 sm:top-10 right-64 sm:right-96 xl:right-[3rem] w-6 -rotate-12 "
              >
                <svg width="40" height="40" class="animate-arrows-h rotate-45 ">
                  <polyline 
                      points="0,40 20,0 40,40 0,40"
                      style="fill:none;stroke:rgba(172, 175, 176, 0.71);stroke-width:2">
                  </polyline>
                </svg>
            </div>
            <div
              data-aos="fade-up"
              data-aos-delay="900"
              class="hidden sm:block absolute top-24 sm:top-10 right-24 sm:right-96 xl:right-[10rem] w-6"
              >

              <svg width="80" height="80" class="animate-arrows-rl">
              <polyline 
                  points="0,40 20,0 40,40 10,40"
                  style="fill:none;stroke:rgba(250,60,60,0.5);stroke-width:2">
              </polyline>
              </svg>
            </div>
            <div
              data-aos="fade-up"
              data-aos-delay="250"
              class=" hidden sm:block absolute bottom-56 right-24 w-6"
              >

              <svg width="80" height="80" class="animate-arrows-lr -rotate-45">
                <polyline 
                    points="30,60 30,0 60,60 30,60"
                    style="fill:none;stroke:rgba(172, 175, 176, 0.71);stroke-width:1">
                </polyline>
              </svg>
            </div>
            <div
              data-aos="fade-up"
              data-aos-delay="550"
              class=" hidden sm:block absolute bottom-22 left-64 w-6"
              >

              <svg width="60" height="60" class="animate-arrows-h ">
                <polyline 
                    points="30,40 30,0 60,30 0,20 60,0"
                    style="fill:none;stroke:rgba(250, 175, 176, 0.71);stroke-width:2">
                </polyline>
              </svg>
            </div>
            <div
              data-aos="fade-up"
              data-aos-delay="200"
              class="hidden sm:block absolute bottom-2 xl:bottom-26 left-[0%] xl:left-2 w-6"
              >
              <svg width="80" height="80" class="animate-arrows-left">
                <polyline 
                    points="0,40 20,0 40,40 0,40"
                    style="fill:none;stroke:rgba(0,0,250,0.5);stroke-width:1">
                </polyline>
              </svg>
            </div>
          </div>
      <!-- Calculator -->
      <section id="calculator" class="w-full p-12 ">
        <div
          data-aos="fade-up"
          data-aos-once="true"
          data-aos-delay="200"
          class="text-center text-[2.5rem] sm:text-5xl xl:text-6xl font-bold leading-tight  sm:pr-8 xl:pr-10">
              Расчет стоимости
          </div>
          <div class="flex gap-6">
            <div 
            data-aos="fade-right"
            data-aos-once="true"
            data-aos-delay="200"
            class="mt-12 bg-neutral-100 p-8 rounded-xl">
                
                <div class="dropdown mt-8">
                    <p class="dropbtn rounded-xl font-bold text-lg">Материал</p><p>для расчета стоимости укажите материал</p>
                    <div class="grid grid-cols-3 p-2   gap-2"">
                      
                        <p v-for="mat in materials_data" :key="mat.id" 
                        @click="material_thickness=1, material=mat.slug"
                        :class="{'bg-neutral-200 font-bold': material==mat.slug}" 
                        class="p-2 mt-2 bg-neutral-300 hover:bg-neutral-200 hover:cursor-pointer border text-center rounded-xl">{{ mat.name }}</p>
                        
                    </div>
                </div>
                <div class="mt-8">
                  <p class="text-lg font-bold">Толщина материала</p>
                  <div class="mt-6 flex gap-2">
                    <div class="text-lg">{{ material_thickness }} мм</div>
                    <div class="">
                      <svg width="400" height="30" class="">
                      <polyline 
                          points="0,15 400,15"
                          style="fill:none;stroke:rgba(60,60,60,0.5);"
                          :style="{'stroke-width': material_thickness}">
                      </polyline>
                      </svg>
                    </div>
                  </div>
                  
                  <div class="grid grid-cols-3 p-2   gap-2">
                      <p 
                        v-for="material in filtred_material_thickness_data" 
                        :key="material.id" 
                        @click="material_thickness=material.thickness"
                        :class="{'bg-neutral-200 font-bold': material_thickness==material.thickness}"
                        class="hover:cursor-pointer bg-neutral-300 hover:bg-neutral-200 ml-6 mt-2 p-2 border rounded-xl text-center"
                        >
                        {{material.thickness}}мм
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

                    <div class="slider-cont">
                      <CustomSlider :min="0" :max="100" v-model="installationCount" />
                    </div>
                  </div>
                </div>
                
            
            </div>
            
            <div class="mt-8 text-center self-center">
              <p class="p-8 text-8xl font-bold">{{ resultPrice }} ₽</p>
            </div>
        </div>

      </section>
  
      <!-- FAQ section -->
    </div>
  </template>
  
  <script setup>
  const show_material_dropdown = ref(false)
  const material = ref('steel')
  const material_thickness = ref(1)
  const installationCount = ref(0)
  const сuttingLength = ref(1);
  // a computed ref
  const resultPrice = computed(() => {
    return calculatePrice()
    // return material_thickness.value * installationCount.value > 0 ? 'Yes' : '?'
  })
  const filtred_material_thickness_data = computed(() => {
    if (material.value){
      let filtred_data = material_thickness_data.filter(data => data.material.includes(material.value))
      // console.log(filtred_data)
      return filtred_data
      
    }
    return material_thickness_data
    
  })
  const materials_data = [
    {id:1, name:'сталь', slug:'steel'},
    {id:2, name:'нержавеющая сталь', slug:'stainless_steel'},
    {id:3, name:'алюминий', slug:'aluminum'},
    {id:4, name:'дюраль', slug:'duralumin'},
    {id:5, name:'титан', slug:'titanium'},
    {id:6, name:'медь', slug:'copper'},
    {id:7, name:'латунь', slug:'brass'},
  ]
  const material_thickness_data = 
    [
      {id:1, thickness:0.8, material:['steel','stainless_steel']},
      {id:2, thickness:1, material:['steel','aluminum','duralumin','titanium','copper','brass','stainless_steel']},
      {id:3, thickness:1.5, material:['steel','aluminum', 'duralumin','titanium','copper','brass','stainless_steel']},
      {id:4, thickness:2, material:['steel','aluminum','duralumin','titanium','copper','brass','stainless_steel']},
      {id:5, thickness:2.5, material:['steel',]},
      {id:6, thickness:3, material:['steel','aluminum','duralumin','titanium','copper','brass','stainless_steel']},
      {id:7, thickness:4, material:['steel','aluminum','duralumin','titanium','copper','brass','stainless_steel']},
      {id:8, thickness:5, material:['steel','aluminum','duralumin','copper','brass','stainless_steel']},
      {id:9, thickness:6, material:['steel','aluminum','duralumin','stainless_steel']},
      {id:10, thickness:8, material:['steel']},
      {id:11, thickness:10, material:['steel']},
      {id:12, thickness:12, material:['steel']},
      {id:14, thickness:16, material:['steel']},

    ]


function calculatePrice(){
  if (material.value && material_thickness.value && сuttingLength.value){

    let materialCutPrice = calculateMaterialThuckness()
    
    let installationPrice = 0
    if (installationCount.value > 0){
      switch(material_thickness.value){
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
        case 10: installationPrice = 3* installationCount.value; break
        case 12: installationPrice = 6 * installationCount.value; break
        case 16: installationPrice = 6 * installationCount.value; break
      }
    }
    console.log(installationPrice, materialCutPrice)
    return installationPrice + (сuttingLength.value * materialCutPrice)
  }
    return 200
}
function calculateMaterialThuckness(){
  if (material.value && material_thickness.value){
    let tempPrice = 0
    if (material.value == 'steel'){
      switch(material_thickness.value){
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
    if (material.value == 'aluminum' ||  material.value == 'duralumin' ){
      switch(material_thickness.value){
        case 1: tempPrice = 35; break
        case 1.5: tempPrice = 45; break
        case 2: tempPrice = 65; break
        case 3: tempPrice = 85; break
        case 4: tempPrice = 110; break
        case 5: tempPrice = 144; break
        case 6: tempPrice = 220; break
        }
      }
    if (material.value == 'titanium'){
      switch(material_thickness.value){
        case 1: tempPrice = 42; break
        case 1.5: tempPrice = 57; break
        case 2: tempPrice = 67; break
        case 3: tempPrice = 77; break
        case 4: tempPrice = 87; break
        }
    }
    if (material.value == 'copper'){
      switch(material_thickness.value){
        case 1: tempPrice = 45; break
        case 1.5: tempPrice = 70; break
        case 2: tempPrice = 98; break
        case 3: tempPrice = 165; break
        case 4: tempPrice = 180; break
        case 5: tempPrice = 240; break
      }
    }
    if (material.value == 'brass'){
      switch(material_thickness.value){
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
    if (material.value == 'stainless_steel'){
      switch(material_thickness.value){
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
    console.log(tempPrice)
    return tempPrice
  }
}
  </script>
  <style scoped>
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
  #hero{
    background-color: #E6FAFF;
    /* color: #acafb0b6; */
  }
  



.animate-arrows-rl{
  animation: arrows-rl 30s ease-in-out infinite;
}
.animate-arrows-left{
  animation: arrows-left 20s ease-in-out infinite;
}
.animate-arrows-lr{
  animation: arrows-lr 40s ease-in-out infinite;
}

.animate-arrows-h{
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
    transform: rotate(360deg) translateX(2rem) translateY(7rem);;
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
    transform: rotate(0deg) translateX(1rem) translateY(3rem);;
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
    transform: rotate(0deg) translateX(4rem) translateY(5rem);;
  }
  100% {
    transform: rotate(60deg) translateX(0rem) translateY(0rem);
  }
}
/* Dropdown Content (Hidden by Default) */
/* .dropdown-content {
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
} */





  </style>
  