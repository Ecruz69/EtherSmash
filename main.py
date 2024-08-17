import requests
from colorama import Fore
import random


URL = "https://api.etherscan.io/api?module=account&action=balance"
#ETHERSCAN API KEYS
API_KEYS = []
API_KEY = random.choice(API_KEYS)


def get_balance(address):
    req = requests.get(f"{URL}&address={address}&tag=latest&apikey={API_KEY}")
    balance = int(req.json()['result']) / 10**18
    return balance

with open("@.txt", "r") as addresses:
    ether_addr = [i.strip() for i in addresses.readlines()]

    for i in ether_addr:
        balance_check = get_balance(i)

        if balance_check == 0:
            print(f'{Fore.RED} {i} --> {balance_check} Ether')

        elif balance_check != 0:
            print(f'{Fore.GREEN} {i} --> {balance_check} Ether , Saving ...')
            with open('balanced.txt','a') as save_wallet:
                save_wallet.write(f'{i} --> {balance_check} Ether \n')

        else:
            exit(0)
