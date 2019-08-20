<template>
    <div>
        <div class="container">
            <div class="d-flex justify-content-center h-100">
                <div class="card card-login mt-5">
                    <div class="card-header">Login</div>
                    <div class="card-body">
                        <div class="input-group form-group">
                            <div class="form-label-group">
                                <label class="label" for="user-login">Email:</label>
                                <div class="control">
                                    <input type="email" class="form-control" id="user-login" v-model="user_login">
                                </div>
                            </div>
                        </div>
                        <div class="input-group form-group">
                            <div class="form-label-group">
                                <label class="label" for="password">Password:</label>
                                <div class="control">
                                    <input type="password" class="form-control" id="password" v-model="password">
                                </div>
                            </div>
                        </div>
                        <button class="btn btn-primary btn-block" @click="authenticate">Login</button>
                        <a v-bind:href="'/register'" class="mt-2">Don't have an account?</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import {EventBus} from '../utils'

    export default {
        data() {
            return {
                user_login: '',
                password: '',
                errorMsg: ''
            }
        },
        methods: {
            authenticate() {
                console.log('123124')
                this.$store.dispatch('login', {user_login: this.user_login, password: this.password})
                    .then(() => this.$router.push('/'))
            },
        },
        mounted() {
            EventBus.$on('failedAuthentication', (msg) => {
                this.errorMsg = msg
            })
        },
        beforeDestroy() {
            EventBus.$off('failedAuthentication')
        }
    }
</script>