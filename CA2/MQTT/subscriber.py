import paho.mqtt.client as mqtt
import json

# MQTT broker details
mqtt_broker = "broker.hivemq.com"
mqtt_port = 1883
mqtt_topic = "sensors/data"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(mqtt_topic)

# Callback when a message is received
def on_message(client, userdata, message):
    try:
        payload = message.payload.decode()
        data = json.loads(payload)
        print(f"Received data: {data}")
        
        gas = data.get('gas')
        flame = data.get('flame')
        light = data.get('light')
        print(f"Gas: {gas}, Flame: {flame}, Light: {light}")

    except Exception as e:
        print(f"Error processing message: {e}")

# Create MQTT client and connect
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker, mqtt_port, 60)

# Start the MQTT loop
client.loop_forever()
