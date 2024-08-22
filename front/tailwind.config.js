/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      keyframes: {
        scroll: {
          '0%, 100%': { transform: 'translateX(0)' },
          '98%': { transform: 'translateX(-1800%)' },
          '99%': { transform: 'translateX(+100%)' },
        },

      },
      animation: {
        scroll: 'scroll 1s ease-in-out infinite',
        scrollLeft:'scrollLeft 1s ease-in-out infinite',
      },
    },
  },
  plugins: [],
}

