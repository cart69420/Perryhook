import colorama
import os
import requests
import time


def _exit():
    exit()


def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True


def main(webhook, username, avatar, delay, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            data = requests.post(webhook,
                                 json={"content": str(message), "username": str(username), "avatar_url": str(avatar)})
            if data.status_code == 204:
                print(f"{colorama.Back.MAGENTA} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            elif data.status_code == 429:
                timeout = int(str(data.json()['retry_after'])[2:])
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Failed Possible Ratelimiting waiting {timeout / 100}s{colorama.Back.RESET}")
                time.sleep(timeout / 100)
        except:
            print()
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.MAGENTA}Webhook deleted.')
    print(f'{colorama.Fore.GREEN}Done...')


def initialize():
    print(f"""{colorama.Fore.MAGENTA} 
██████╗░███████╗██████╗░██████╗░██╗░░░██╗██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██║░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╔╝█████╗░░██████╔╝██████╔╝░╚████╔╝░███████║██║░░██║██║░░██║█████═╝░
██╔═══╝░██╔══╝░░██╔══██╗██╔══██╗░░╚██╔╝░░██╔══██║██║░░██║██║░░██║██╔═██╗░
██║░░░░░███████╗██║░░██║██║░░██║░░░██║░░░██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝
  By cattyn & edited by le perry <3 cattyn.
     """)
    webhook = input("Enter ur webhook > ")
    username = input("Enter a webhook name > ")
    avatar = input("Enter a avatar url > ")
    message = input("Enter a message > ")
    delay = input("Enter a delay [int/float] > ")
    amount = input("Enter an amount [int/inf] > ")
    hookDeleter = input("Delete webhook after spam? [Y/N] > ")
    if len(message) > 2000:
        print (f"{colorama.Back.RED} {colorama.Fore.WHITE}Error! Only 2000 characters allowed in the message!{colorama.Back.RESET}")
        _exit()
    elif len(username) > 80:
        print (f"{colorama.Back.RED} {colorama.Fore.WHITE}Error! Only 80 characters allowed in the username!{colorama.Back.RESET}")
        _exit()
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (
            hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        _exit()
    else:
        main(webhook, username, avatar, delay, amount, message, hookDeleter)
        _exit()


if __name__ == '__main__':
    os.system('cls')
    os.system('title cutehook on top.')
    colorama.init()
    initialize()
