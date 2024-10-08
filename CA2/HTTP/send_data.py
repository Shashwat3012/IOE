import requests
import json

# Define the server URL
server_url = 'http://localhost:5000/predict'

# Function to send sensor data
def send_sensor_data(gas, flame, light):
    payload = {
        'gas': gas,
        'flame': flame,
        'light': light
    }
    response = requests.post(server_url, json=payload)
    if response.status_code == 200:
        print("Data sent successfully!")
        print(f"Prediction: {response.json()}")
    else:
        print(f"Failed to send data: {response.status_code} - {response.text}")

# Example usage
send_sensor_data(150, 20, 800)  # Simulated values
