import paho.mqtt.client as mqtt
import os
import time


# MQTT Config
MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", 1883))
MQTT_BROKER_HOST = os.getenv("MQTT_BROKER_HOST", "mqtt_broker")
MQTT_TOPIC = "test_topic"


def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    
    
# Initialize Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

time.sleep(5)

client.on_connect = on_connect
client.on_message = on_message

client.connect(host = MQTT_BROKER_HOST, 
               port = MQTT_BROKER_PORT,
               keepalive = 60)

client.loop_forever()

