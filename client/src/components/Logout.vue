<template></template>
<script>
    import {mapActions} from 'vuex'

    export default {
        mounted() {
            this.logout()
            this.$router.push('/login')
        },
        methods: mapActions([
            'logout'
        ])
    }
</script>
