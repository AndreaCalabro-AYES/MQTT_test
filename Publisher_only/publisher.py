import paho.mqtt.client as mqtt
import os
import time


# MQTT Config
MQTT_BROKER_PORT = int(os.getenv(key="MQTT_BROKER_PORT", default=1883))
MQTT_BROKER_HOST = os.getenv(key="MQTT_BROKER_HOST", default="mqtt_broker")
MQTT_TOPIC = "test_topic"

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

time.sleep(10)

publisher.connect(
    host = MQTT_BROKER_HOST,
    port = MQTT_BROKER_PORT,
    keepalive = 60
)

print(f"Connected to broker at {MQTT_BROKER_HOST}: {MQTT_BROKER_PORT}", flush=True)

while True:
    msg_body = "Mustard on the beat"
    publisher.publish(
        topic = MQTT_TOPIC,
        payload= msg_body,
    )
    print(f"Published {msg_body}, to {MQTT_TOPIC}", flush=True)
    time.sleep(10)




