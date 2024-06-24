import paho.mqtt.client as mqtt
import os
import time
import threading


# MQTT Config
MQTT_BROKER_PORT = int(os.getenv(key="MQTT_BROKER_PORT", default=1883))
MQTT_BROKER_HOST = os.getenv(key="MQTT_BROKER_HOST", default="mqtt_broker")
MQTT_TOPIC = "test_topic"


def on_connect(client, userdata, flags, reasonCode, properties=None):
    if reasonCode == 0:
        print("Connected!", flush=True)
        client.subscribe(MQTT_TOPIC)
        print(f"Subscribed to topic: {MQTT_TOPIC}", flush=True)
    else:
        print("Connection failed with code " + str(reasonCode), flush=True)


def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}", flush=True)


def publish_message(client, message):
    """Publishes a message to the specified topic."""
    client.publish(topic=MQTT_TOPIC, payload=message)
    print(f"Published: {message} to {MQTT_TOPIC}", flush=True)

def background_task():
    client.loop_forever()


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect(host=MQTT_BROKER_HOST, port=MQTT_BROKER_PORT, keepalive=60)

background_thread = threading.Thread(target=background_task)
background_thread.start()

while True:
    publish_message(client, "JOLLY")
    time.sleep(10)

background_thread.join()

