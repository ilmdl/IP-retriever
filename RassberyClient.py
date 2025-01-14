import paho.mqtt.client as paho
import time
import socket

topic="WIFI"

mqttClient = paho.Client(paho.CallbackAPIVersion.VERSION2)

while mqttClient.connect("broker.emqx.io",1883,60)!=0:
    print("[FAILD] could not connect to MQTT Broker! retrying in 5 seconds")
    time.sleep(5)

def on_message(client, userdata, message):  
    print("[RECIEVED] message recieved ", str(message.payload.decode("utf-8")))
    currentIP = socket.gethostbyname(socket.gethostname())
    currentIP = "1.2.3.4.5.6"
    print(f"[PUBLISHING] Publishing to topic {topic}")
    print("")
    mqttClient.publish(topic, currentIP)

print("[SUBSCRIBING] subscribing to getIP")
mqttClient.subscribe("getIP")

mqttClient.on_message = on_message

mqttClient.loop_forever()