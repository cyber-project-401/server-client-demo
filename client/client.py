import time
import requests
import urllib3
# Suppress InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
SERVER_URL = "https://server:8443"
while True:
    try:
        print("Sending request to server...")
        response = requests.get(SERVER_URL, verify=False)  # Ignore SSL verification for simplicity
        print(f"Response from server: {response.json()}")
    except Exception as e:
        print(f"Error connecting to server: {e}")
    time.sleep(10)  # Wait 10 seconds before the next request