import paho.mqtt.client as mqtt
import random
import time
import json

# MQTT broker details
mqtt_broker = "broker.hivemq.com"
mqtt_port = 1883
mqtt_topic = "sensors/data"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")

# Function to simulate and publish sensor data
def publish_data(client):
    while True:
        gas = random.uniform(100, 500)  # Simulated MQ2 gas sensor value
        flame = random.uniform(0, 100)  # Simulated flame sensor value
        light = random.uniform(0, 1023)  # Simulated LDR sensor value

        # Create JSON payload
        data = {
            "gas": gas,
            "flame": flame,
            "light": light
        }
        data_json = json.dumps(data)

        # Publish data to MQTT broker
        client.publish(mqtt_topic, data_json)
        print(f"Published data: {data_json}")

        # Wait before publishing the next data point
        time.sleep(5)

# Create MQTT client and connect
client = mqtt.Client()
client.on_connect = on_connect
client.connect(mqtt_broker, mqtt_port, 60)

# Start the MQTT loop in a separate thread
client.loop_start()

# Start publishing data
publish_data(client)
