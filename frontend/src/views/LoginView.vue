<template>
  <div class="login">
    <h1>Please Login in</h1>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="username">
      <input v-model="password" placeholder="password" type="password">
      <input type="submit" value="log in">
    </form>
    <div v-if="message">
        {{message}}
    </div>
    <button @click="publicMess">Get Public Message</button>
    <div v-if="publicMessage">
        {{publicMessage}}
    </div>
  </div>
  
</template>

<script>
import axios from 'axios'

export default {
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
            message: '',
            publicMessage: ''
        }
    },
    mounted() {
        if(localStorage.getItem('token')){
            this.secret();
        }
    },
    methods: {
        async login() {
            await axios
            .post(`/api-token-auth/`, {
                username: this.username,
                password: this.password,
            },
            {
                headers: {
                    'content-type': 'application/json'
                }
            })
            .then(response => {
                localStorage.setItem('token', response.data.token)
                // that.$store.commit('LOGIN_SUCCESS', response.data)
                this.secret();
            })
            // .then(response => {
            //     token = localStorage.getItem('token')
            //     // if (token) {
            //     //     router.push({ name: 'secret', params: { Token: token } })
            //     // }
                
            // })
            .catch(error => {
                console.log(error)
            })
        },
        async secret() {
            await axios
            .get(`/vocab/secret/`, {
                headers: {
                    'Authorization': `Token ${localStorage.getItem('token')}`,
                    'content-type': 'application/json'
                }
            })
            .then(response => {
                this.publicMessage = response.data.message
            })
            .catch(error => {
                console.log(error)
            })
        },
        async publicMess() {
            await axios
            .get(`/vocab/public/`, {
                headers: {
                    'Authorization': `Token ${localStorage.getItem('token')}`,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                this.message = response.data.message
            })
            .catch(error => {
                console.log(error)
            })
        },
    }
}
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
