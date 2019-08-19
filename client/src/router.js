import Vue from 'vue'
import Router from 'vue-router'
import List from './components/List'
import Login from './components/Login'
import Register from './components/Register'
import Logout from './components/Logout'
import {store} from './store'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/list',
            name: 'List',
            component: List,
            beforeEnter(to, from, next) {
                if (!store.getters.isAuthenticated) {
                    next('/login')
                } else {
                    next()
                }
            }
        },
        {
            path: '/login',
            name: 'Login',
            component: Login,
        },
        {
            path: '/register',
            name: 'Register',
            component: Register,
        },
        {
            path: '/logout',
            name: 'Logout',
            component: Logout,
        }
    ],
})