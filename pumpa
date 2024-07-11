import requests
import time

# Function to read authorization data from file
def read_auth_data():
    with open('data.txt', 'r') as file:
        return file.read().strip()

# URL and headers
url = 'https://tg.pumpad.io/referral/api/v1/lottery'
headers = {
    'Authorization': read_auth_data(),
    'Content-Type': 'application/json'
}

# Function to spin the lottery
def spin_lottery():
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(f"Lottery spun successfully. Response: {response.json()}")
    else:
        print(f"Failed to spin lottery. Status Code: {response.status_code}")

# Spin the lottery 10 times, once per day
for _ in range(10):
    spin_lottery()
    time.sleep(86400)  # Sleep for 1 day (86400 seconds)
