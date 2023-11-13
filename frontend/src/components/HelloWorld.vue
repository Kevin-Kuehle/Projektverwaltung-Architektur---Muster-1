<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-img height="300" src="@/assets/logo.svg" />

      <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>

      <h1 class="text-h2 font-weight-bold">Vuetify</h1>

      <div class="py-14" />

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            href="https://vuetifyjs.com/components/all/"
            min-width="164"
            rel="noopener noreferrer"
            target="_blank"
            variant="text"
          >
            <v-icon
              icon="mdi-view-dashboard"
              size="large"
              start
            />

            Components
          </v-btn>
        </v-col>

        <v-col cols="auto">
          <v-btn
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            target="_blank"
            variant="flat"
          >
            <v-icon
              icon="mdi-speedometer"
              size="large"
              start
            />

            Get Started
          </v-btn>
        </v-col>
      
        

        <v-col cols="auto">
          <v-btn
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            target="_blank"
            variant="flat"
            @click="clickHandler"
          >
            <v-icon
              icon="mdi-send"
              size="large"
              start
            />

            Ping Backend
          </v-btn>

       
        </v-col>

        <v-col cols="auto">
          <v-btn
            href="https://community.vuetifyjs.com/"
            min-width="164"
            rel="noopener noreferrer"
            target="_blank"
            variant="text"
          >
            <v-icon
              icon="mdi-account-group"
              size="large"
              start
            />

            Community
          </v-btn>
        </v-col>
      </v-row>
      <v-row v-if="responseData">
        {{responseData}}
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue';

  const responseData = ref(null);

  const clickHandler = () => {
    
    const url = "http://localhost:8000/?format=json";
    const options = {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
  },
    }
    
    fetch(url, { ...options }).then( response => {

      if (response.ok) {
        response.json().then( data => {
          responseData.value = data;
            console.log('Devlog: data', data);
        })
      } else {
        responseData.value = response
      }
    })
  }
</script>
