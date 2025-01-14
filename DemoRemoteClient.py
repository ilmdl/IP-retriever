import paho.mqtt.client as paho
import time

mqttClient = paho.Client(paho.CallbackAPIVersion.VERSION2)

def on_message(client, userdata, message):
    print("[RECIEVED] received message: ", str(message.payload.decode("utf-8")))
    print("")
    time.sleep(5)
    print("[REQUESTING] requesting ip address")
    mqttClient.publish("getIP","requesting ip")

while mqttClient.connect("broker.emqx.io",1883,60) != 0:
    print("[FAILD] could not connect to MQTT Broker! retrying in 5 seconds")
    time.sleep(5)

print("[SUBSCRIBING] subscribing to WIFI")
mqttClient.subscribe("WIFI")

print("[REQUESTING] requesting ip address")
mqttClient.publish("getIP","requesting ip")

mqttClient.on_message = on_message
mqttClient.loop_forever()
print("[DISCONNECT] disconnecting from mqtt")
mqttClient.disconnect()