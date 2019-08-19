import 'bootstrap/dist/css/bootstrap.css'
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue';
import router from './router'
import store from './store'
import App from './App.vue'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
store.dispatch('isJwtTokenExist')

new Vue({
    render: h => h(App),
    router,
    store,
}).$mount('#app')
