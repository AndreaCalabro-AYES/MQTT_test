import paho.mqtt.client as mqtt
import os
import time


# MQTT Config
MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", 1883))
MQTT_BROKER_HOST = os.getenv("MQTT_BROKER_HOST", "mqtt_broker")
MQTT_TOPIC = "test_topic"


# Added properties=None
# https://github.com/marceloleitner/mqtt2rrd/issues/1#issuecomment-608970156
def on_connect(client, userdata, flags, reasonCode, properties=None):
  if reasonCode == 0:
      print("Connection established!", flush=True)
      client.subscribe(MQTT_TOPIC)
      print(f"Subscribed to topic: {MQTT_TOPIC}", flush=True)
  else:
    print("Connection failed with code  " + str(int(reasonCode)), flush=True)


def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}", flush=True)
    if "Mustard on the beat" == msg.payload.decode():
      print("They not like us\nThey not like us", flush=True)
    
  
# Initialize Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

time.sleep(10)



client.on_connect = on_connect
client.on_message = on_message


client.connect(host = MQTT_BROKER_HOST, 
               port = MQTT_BROKER_PORT,
               keepalive = 60)



print("Starting loop to process network traffic and dispatch callbacks", flush=True)
client.loop_forever()

