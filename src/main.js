import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { createApp } from 'vue'
import App from './App.vue'
import ElementPlusComplex from './ElementPlusComplex.vue'

const app = createApp(App)
app.component('ElementPlusComplex', ElementPlusComplex)
app.use(ElementPlus)
app.mount('#app')
