import Vue from 'vue'
import Vuex from 'vuex'

// imports of AJAX functions will go here
import {
    fetchSurveys,
    fetchSurvey,
    saveSurveyResponse,
    postNewSurvey,
    authenticate,
    register,
    getUserList,
    deleteUser, editUser
} from '../api'
import {isValidJwt, EventBus} from '../utils'

Vue.use(Vuex)

const state = {
    // single source of data
    user: {},
    users: [],
    jwt: ''
}

const actions = {
    login(context, userData) {
        context.commit('setUserData', {userData})

        return authenticate(userData)
            .then(response => {
                console.log(response.data)
                context.commit('setJwtToken', {jwt: response.data})
            })
            .catch(error => {
                console.log('Error Authenticating: ', error)
                EventBus.$emit('failedAuthentication', error)
            })
    },
    register(context, userData) {
        context.commit('setUserData', {userData})
        return register(userData)
            .then(context.dispatch('login', userData))
            .catch(error => {
                console.log('Error Registering: ', error)
                EventBus.$emit('failedRegistering: ', error)
            })
    },
    isJwtTokenExist(context) {
        console.log('Call jwttocken')
        console.log(localStorage.token)
        if (localStorage.token) {
            context.commit('setJwtToken', {jwt: {token: localStorage.token}})
        }
    },
    getUsers(context) {
        console.log(context.state.jwt)
        getUserList(context.state.jwt)
            .then((res) => context.commit('setUsers', res.data.data.users))
    },
    logout(context) {
        context.commit('logout')
        localStorage.removeItem('token')
    },
    async editUser(context, userData) {
        await editUser(userData, context.state.jwt)
        //context.commit('editUser', {userData})
    },
    async deleteUser(context, userId) {
        await deleteUser(userId, context.state.jwt)
        context.commit('deleteUser', {userId})
    }
}

const mutations = {
    logout(state) {
        state.jwt = ''
    },
    deleteUser(state, payload) {
        state.users = state.users.filter((user) => user.id !== payload.userId)
    },
    setUserData(state, payload) {
        console.log('setUserData payload = ', payload)
        state.userData = payload.userData
    },
    setJwtToken(state, payload) {
        console.log('setJwtToken payload = ', payload)
        if (payload) {
            localStorage.token = payload.jwt.token
            state.jwt = payload.jwt.token
        } else {
            console.error('Payload error')
            console.trace('Payload undefined')
        }
    },

    setUsers(state, payload) {
        state.users = payload
    }
}

const getters = {
    // reusable data accessors

    isAuthenticated(state) {
        return isValidJwt(state.jwt)
    }
}

export const store = new Vuex.Store({
    state,
    actions,
    mutations,
    getters
})

export default store