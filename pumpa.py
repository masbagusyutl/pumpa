import requests
import time
from datetime import datetime, timedelta

# Function to read authorization data from file
def read_auth_data():
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        accounts = [line.strip() for line in lines]
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
    print("\nCountdown complete.")

# Function to process a single account
def process_single_account(account, account_index, num_spins):
    url = 'https://tg.pumpad.io/referral/api/v1/lottery'
    headers = {
        'Authorization': account,
        'Content-Type': 'application/json'
    }
    print(f"Using account {account_index}: {account}")

    for attempt in range(1, num_spins + 1):
        print(f"Attempt {attempt}:")
        spin_lottery(url, headers)
        time.sleep(10)  # Wait 10 seconds between attempts

# Main function to spin lottery
def spin_lottery_custom():
    accounts = read_auth_data()
    num_accounts = len(accounts)
    print(f"Total accounts found in data.txt: {num_accounts}")

    choice = input("Enter '1' to process a single account, '2' to process all accounts: ")

    if choice == '1':
        account_index = int(input(f"Enter the account number to process (1-{num_accounts}): ")) - 1
        num_spins = int(input("Enter the number of spins: "))
        if 0 <= account_index < num_accounts:
            process_single_account(accounts[account_index], account_index + 1, num_spins)
        else:
            print("Invalid account number.")
    elif choice == '2':
        for day in range(1, 11):
            print(f"\nStarting lottery spins for day {day}...\n")
            for account_index, account in enumerate(accounts, start=1):
                process_single_account(account, account_index, 10)
                if account_index < num_accounts:
                    print(f"Switching to the next account in 10 seconds...")
                    time.sleep(10)  # Wait 10 seconds before switching to the next account

            # Calculate next day's time and countdown
            if day < 10:
                next_day = datetime.now() + timedelta(days=1)
                print(f"\nNext spins will start at {next_day.strftime('%Y-%m-%d %H:%M:%S')}")
                time_until_next_day = (next_day - datetime.now()).total_seconds()
                print(f"Countdown until next spins:")
                countdown_timer(int(time_until_next_day))
    else:
        print("Invalid choice.")

    print("All spins completed.")

# Start the process
spin_lottery_custom()
