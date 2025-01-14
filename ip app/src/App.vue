<template >
  <div class="d-flex align-center justify-center flex-column h-100">
    <VCard class="pa-10 d-flex flex-column align-center">
      <p>curret ip</p>
      <h1>{{ theIP }}</h1>
      <v-snackbar
      :timeout="2000"
      color="success"
      variant="outlined"
      >
        <template v-slot:activator="{ props }">
          <VBtn v-bind="props" color="success" @click="getIP" icon="mdi-reload"></VBtn>
        </template>
        <p>IP updated</p>
      </v-snackbar>
    </VCard>
  </div>
</template>

<script setup>
import mqtt from 'mqtt'
import {ref, onMounted} from 'vue'

var theIP = ref("None")
var oldIP = ref("None")
function getIP(client) {
  client.on("message", (topic, message) => {
    theIP.value = message
    console.log(`received message: ${message} from topic: ${topic}`);
  });
  client.subscribe("WIFI")
  client.publish("getIP","requesting ip")
}
onMounted(() => {
  const client = mqtt.connect("ws://broker.emqx.io:8083/mqtt");
  getIP(client);
})
</script>