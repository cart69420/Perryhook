import colorama
import os
import requests
import time


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
                timeout = int(str(data.json()['retry_after']))
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Failed Ratelimited Waiting {timeout / 1000}s{colorama.Back.RESET}")
                time.sleep(timeout / 1000)
            info = requests.get(hook).text
            if "\"message\": \"Unknown Webhook\"" in info:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Skids deleted the webhook.{colorama.Back.RESET}")
                exit()
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
    if len(username) > 80:
        print (f"{colorama.Back.RED}{colorama.Fore.WHITE}Error! Only 80 characters allowed in the username!{colorama.Back.RESET}")
        exit()
    avatar = input("Enter a avatar url > ")
    message = input("Enter a message > ")
    if len(message) > 2000:
        print (f"{colorama.Back.RED}{colorama.Fore.WHITE}Error! Only 2000 characters allowed in the message!{colorama.Back.RESET}")
        exit()
    delay = input("Enter a delay [int/float] > ")
    amount = input("Enter an amount [int/inf] > ")
    hookDeleter = input("Delete webhook after spam? [Y/N] > ")
    try:
        delay = float(delay)
    except ValueError:
        exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (
            hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        exit()
    else:
        main(webhook, username, avatar, delay, amount, message, hookDeleter)
        exit()


if __name__ == '__main__':
    os.system('cls')
    os.system('title cutehook on top.')
    colorama.init()
    initialize()
