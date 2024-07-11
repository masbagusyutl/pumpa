import requests
import time
from datetime import datetime, timedelta

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
        print(f"[{datetime.now()}] Lottery spun successfully. Response: {response.json()}")
    else:
        print(f"[{datetime.now()}] Failed to spin lottery. Status Code: {response.status_code}")

# Spin the lottery 10 times, once per day
for i in range(1, 11):
    print(f"Spinning lottery attempt {i}...")
    spin_lottery()
    
    # Calculate the time for next spin
    next_day = datetime.now() + timedelta(days=1)
    print(f"Next spin will be at {next_day.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Sleep for 1 day (86400 seconds)
    time.sleep(86400)

print("All spins completed.")
