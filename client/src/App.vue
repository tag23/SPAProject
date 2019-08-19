<template>
    <div id="app">
        <nav class="nav navbar-nav navbar-dark bg-light">
            <div class="row justify" style="margin: 0;">
                <router-link class="nav-link nav-item btn btn-dark col-1 mr-3" to="/list">List</router-link>
                <router-link class="nav-link nav-item btn btn-dark col-1 mr-3" to="/logout" v-if="this.isAuthenticated">Logout</router-link>
                <router-link class="nav-link nav-item btn btn-dark col-1 mr-3" to="/register" v-else>Register</router-link>
            </div>
        </nav>
        <router-view/>
    </div>
</template>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }
</style>
<script>
    import { mapGetters } from 'vuex';
    export default {
        computed: mapGetters([
            'isAuthenticated'
        ])
    }
</script>