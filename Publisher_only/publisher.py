import paho.mqtt.client as mqtt
import os
import time


# MQTT Config
MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", 1883))
MQTT_BROKER_HOST = os.getenv("MQTT_BROKER_HOST", "mqtt_broker")
MQTT_TOPIC = "test_topic"

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

publisher.connect(
    host = MQTT_BROKER_HOST,
    port = MQTT_BROKER_PORT,
    keepalive = 60
)

while True:
    msg_body = "Mustard on the beat"
    publisher.publish(
        topic = MQTT_TOPIC,
        payload= msg_body
    )
    print(f"Published {msg_body} in {MQTT_TOPIC}")
    time.sleep(1)




