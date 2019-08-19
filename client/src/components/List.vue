<template>
    <div class="container">
        <table class="table table-hover mt-5">
            <thead class="thead-dark">
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Surname</th>
            <th scope="col">Birthday</th>
            <th scope="col">Login</th>
            <th></th>
            </thead>
            <tbody>
            <tr v-for="(user, index) in users" :key="index">
                <td>{{ index + 1 }}</td>
                <td>{{ user.name }}</td>
                <td>{{ user.surname }}</td>
                <td>{{ user.birthday_date | formatDate }}</td>
                <td>{{ user.user_login }}</td>
                <td>
                    <div class="btn-group" role="group">
                        <button type="button" class="btn btn-warning btn-sm" v-b-modal.book-edit-modal @click="openEdit(user)">Edit
                        </button>
                        <button type="button" class="btn btn-danger btn-sm" @click="deleteUser(user.id)">Delete</button>
                    </div>
                </td>
            </tr>
            </tbody>
        </table>
        <b-modal id="book-edit-modal"
                 title="Edit user"
                 ref="userModal"
                 hide-footer>
            <b-form class="w-100" @submit="localEditForm">
                <b-form-group id="form-title-group"
                              label="Title:"
                              label-for="form-title-input">
                    <b-form-input id="form-title-input"
                                  type="text"
                                  v-model="editForm.name"
                                  required
                                  placeholder="Name">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-title-group"
                              label="Title:"
                              label-for="form-title-input">
                    <b-form-input id="form-title-input"
                                  type="text"
                                  v-model="editForm.surname"
                                  required
                                  placeholder="Surname">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-title-group"
                              label="Title:"
                              label-for="form-title-input">
                    <b-form-input id="form-title-input"
                                  type="date"
                                  v-model="editForm.birthday_date"
                                  required
                                  placeholder="Birthday">
                    </b-form-input>
                </b-form-group>
                <b-button type="submit" variant="primary">Confirm</b-button>
                <b-button type="reset" variant="danger">Cancel</b-button>
            </b-form>
        </b-modal>
    </div>
</template>
<script>
    import * as moment from 'moment/moment'
    import Vue from 'vue'
    import {mapActions, mapState} from 'vuex'

    export default {
        name: 'List',
        data() {
            return {
                editForm: {
                    id: '',
                    name: '',
                    surname: '',
                    birthday_date: '',
                },
                error: ''
            }
        },
        computed: mapState({
            users: 'users',
        }),
        methods: {
            ...mapActions([
                'getUsers',
                'deleteUser',
                'editUser'
            ]),
            localEditForm(event) {
                event.preventDefault()
                this.$refs.userModal.hide()
                this.editUser(this.editForm)
            },
            openEdit(user) {
                this.editForm.id = user.id
                this.editForm.name = user.name
                this.editForm.surname = user.surname
                this.editForm.birthday_date = user.birthday_date
            }
        },
        created() {
            this.getUsers()
        },

    }
    Vue.filter('formatDate', function (value) {
        if (value) {
            return moment(String(value)).format('MM/DD/YYYY')
        }
    })
</script>