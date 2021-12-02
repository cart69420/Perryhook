import asyncio
import os
import time

import colorama
import requests


async def check_hook(webhook):
    if "\"message\": \"Unknown Webhook\"" in requests.get(webhook).text:
        return False
    return True


async def main(webhook, username, avatar, delay, amount, message, deleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        data = requests.post(webhook,
                             json={"content": str(message), "username": str(username), "avatar_url": str(avatar)})
        if data.status_code == 204:
            print(f"{colorama.Back.MAGENTA} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            # Simple but effective rate limiting system so u can spam forever until they or u delete the webhook.
        elif data.status_code == 429:
            timeout = int(str(data.json()['retry_after']))
            print(
                f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Failed Ratelimited Waiting {timeout / 1000}s{colorama.Back.RESET}")
            time.sleep(timeout / 1000)
            # Checks during sending stuff if the webhook was deleted and if it was it alerts u so u know you're not wasting ur time.
        if "\"message\": \"Unknown Webhook\"" in requests.get(webhook).text:
            print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Skids deleted the webhook.{colorama.Back.RESET}")
            exit()
        time.sleep(float(delay))
        counter += 1
    if deleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.MAGENTA}Webhook deleted.')
    print(f'{colorama.Fore.GREEN}Done...')


async def initialize():
    print(f"""{colorama.Fore.MAGENTA} 
██████╗░███████╗██████╗░██████╗░██╗░░░██╗██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██║░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╔╝█████╗░░██████╔╝██████╔╝░╚████╔╝░███████║██║░░██║██║░░██║█████═╝░
██╔═══╝░██╔══╝░░██╔══██╗██╔══██╗░░╚██╔╝░░██╔══██║██║░░██║██║░░██║██╔═██╗░
██║░░░░░███████╗██║░░██║██║░░██║░░░██║░░░██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝
  I love Perryhook.
     """)
    webhook = input("Enter ur webhook > ")
    username = input("Enter a webhook name > ")
    # Checks the length of the username input and if its over 80 it alerts u because in normal Discord without nitro that wouldn't work and usernames through webhooks can't have nitro, so it limits to 80 characters and simply closes/exits the program.
    if len(username) > 80:
        print(
            f"{colorama.Back.RED}{colorama.Fore.WHITE}Error! Only 80 characters allowed in the username!{colorama.Back.RESET}")
        exit()
    avatar = input("Enter a avatar url > ")
    message = input("Enter a message > ")
    # Checks the length of the message input and if its over 2000 it alerts u because in normal Discord without nitro that wouldn't work and sending messages through webhooks can't have nitro, so it limits to 2000 characters and simply closes/exits the program.
    if len(message) > 2000:
        print(
            f"{colorama.Back.RED}{colorama.Fore.WHITE}Error! Only 2000 characters allowed in the message!{colorama.Back.RESET}")
        exit()
    delay = input("Enter a delay [int/float] > ")
    amount = input("Enter an amount [int/inf] > ")
    deleter = input("Delete webhook after spam? [Y/N] > ")
    try:
        delay = float(delay)
    except ValueError:
        exit()
    if not await check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (
            deleter.lower() != "y" and deleter.lower() != "n"):
        exit()
    else:
        await main(webhook, username, avatar, delay, amount, message, deleter)
        exit()


if __name__ == '__main__':
    os.system('cls')
    os.system('title Perryhook on top.')
    colorama.init()
    asyncio.run(initialize())
