import requests
import time
from datetime import datetime, timedelta

# Function to read authorization data from file
def read_auth_data():
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        accounts = []
        for line in lines:
            accounts.append(line.strip())
        return accounts

# Function to spin the lottery
def spin_lottery(url, headers):
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(f"[{datetime.now()}] Lottery spun successfully. Response: {response.json()}")
    else:
        print(f"[{datetime.now()}] Failed to spin lottery. Status Code: {response.status_code}")

# Function to display countdown timer
def countdown_timer(seconds):
    while seconds > 0:
        print(f"Countdown: {str(timedelta(seconds=seconds))} remaining", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Countdown complete.")

# Main function to spin lottery 10 times daily
def spin_lottery_daily():
    accounts = read_auth_data()
    num_accounts = len(accounts)
    print(f"Total accounts found in data.txt: {num_accounts}")

    for account_index, account in enumerate(accounts, start=1):
        url = 'https://tg.pumpad.io/referral/api/v1/lottery'
        headers = {
            'Authorization': account,
            'Content-Type': 'application/json'
        }

        print(f"Using account {account_index} of {num_accounts}: {account}")
        
        for day in range(1, 11):
            print(f"Starting lottery spins for day {day}...")

            for attempt in range(1, 11):
                print(f"Attempt {attempt}:")
                spin_lottery(url, headers)
                time.sleep(10)  # Wait 10 seconds between attempts
            
            # Calculate next day's time and countdown
            if day < 10:
                next_day = datetime.now() + timedelta(days=1)
                print(f"Next spins will start at {next_day.strftime('%Y-%m-%d %H:%M:%S')}")
                time_until_next_day = (next_day - datetime.now()).total_seconds()
                print(f"Countdown until next spins:")
                countdown_timer(int(time_until_next_day))

    print("All daily spins completed.")

# Start spinning the lottery daily
spin_lottery_daily()
