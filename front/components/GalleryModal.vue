<template>
    <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50" @click.self="closeModal">
      <div class=" p-6 w-[80%]  lg:w-[65%] xl:w-[65%] text-center ">
        <button @click="closeModal" class="absolute top-2 right-2 p-2 scale-150  text-white hover:text-gray-700">
          &times;
        </button>
        <div class="">
            <div class="flex relative gap-2 justify-center items-center  ">
                <div @click="emit('openNextPhoto', photoUndo)" class=" lg:hidden absolute -left-10 p-5 py-10 bg-gray-200/80 duration-150 rounded-xl text-white font-bold text-2xl hover:cursor-pointer hover:translate-x-[-30%]"><</div>
                <img v-if="photoUndo" @click="emit('openNextPhoto', photoUndo)" :src="`/img/portfolio/${photoUndo}.webp`" alt="" class="z-20 hidden lg:block  rounded-xl relative translate-x-[50%] duration-300 filter grayscale hover:translate-x-[0] hover:cursor-pointer hover:-rotate-2 hover:grayscale-0 w-[50%] h-[60vh]">
              
                    <img v-if="photoItem" @click="emit('close')" :src="`/img/portfolio/${photoItem}.webp`" alt="" class="z-40 relative  rounded-xl  h-[95vh] h-max-[20vh]">
              
                <img v-if="photoNext" @click="emit('openNextPhoto', photoNext)" :src="`/img/portfolio/${photoNext}.webp`" alt="" class="z-20 hidden lg:block rounded-xl relative translate-x-[-50%] duration-300 filter grayscale hover:translate-x-[0] hover:cursor-pointer hover:rotate-2  hover:grayscale-0 w-[50%] h-[60vh]">
                <div @click="emit('openNextPhoto', photoNext)" class="lg:hidden absolute -right-10 p-5 py-10 bg-gray-200/80 duration-150 rounded-xl text-white font-bold text-2xl hover:cursor-pointer hover:translate-x-[30%]">></div>
            </div>
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
    photoItem: {
      type: Number,
    },
    photoUndo: {
      type: Number,
    },
    photoNext: {
      type: Number,
    }
  });
  
  const emit = defineEmits(['close', 'openNextPhoto']);
  
  const closeModal = () => {
    emit('close');
  };


  </script>
  <style scoped>
img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  /* Сохраняет пропорции изображения */
}
</style>