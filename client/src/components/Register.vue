<template>
    <div>
        <div class="container">
            <div class="d-flex justify-content-center h-100">
                <div class="card card-register mx-auto mt-5">
                    <div class="card-header text-center">Registration</div>
                    <div class="card-body">
                        <div class="form-group">
                            <div class="form-row">
                                <div class="col-md-6">
                                    <div class="form-label-group">
                                        <input type="text" class="form-control" id="name" placeholder="Name"
                                               v-model="name">
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-label-group">

                                        <input type="text" class="form-control" id="surname" placeholder="Surname"
                                               v-model="surname">
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="form-group">
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <label class="input-group-text" for="birthday_date">Birthday:</label>
                                </div>
                                <input type="date" class="form-control" id="birthday_date"
                                       v-model="birthday_date">

                            </div>
                        </div>
                        <div class="form-group">
                            <div class="input-group">
                                <input type="email" class="form-control" id="user-login" placeholder="Email" v-model="user_login">
                            </div>
                        </div>

                    <div class="form-group">
                        <div class="input-group">
                            <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
                        </div>
                    </div>
                        <div class="form-group">
                        <div class="input-group">
                            <input type="password" class="form-control" id="confirm" placeholder="Password" v-model="confirm">
                        </div>
                    </div>
                    <button class="btn btn-primary form-control" @click="register">Register</button>
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
                name: '',
                surname: '',
                birthday_date: '',
                user_login: '',
                password: '',
                confirm: '',
                errorMsg: ''
            }
        },
        methods: {
            register() {
                this.$store.dispatch('register', {
                    name: this.name,
                    surname: this.surname,
                    birthday_date: this.birthday_date,
                    user_login: this.user_login,
                    password: this.password,
                    confirm: this.confirm,
                })
                    .then(() => this.$router.push('/'))
            }
        },
        mounted() {
            EventBus.$on('failedRegistering', (msg) => {
                this.errorMsg = msg
            })
        },
        beforeDestroy() {
            EventBus.$off('failedRegistering')
        }
    }
</script>