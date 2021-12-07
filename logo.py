import time
import colorama
from tabulate import tabulate
letters = [
"""
██████╗░
██╔══██╗
██████╔╝
██╔═══╝░
██║░░░░░
╚═╝░░░░░
""",
"""
███████╗
██╔════╝
█████╗░░
██╔══╝░░
███████╗
╚══════╝
""",
"""
██████╗░
██╔══██╗
██████╔╝
██╔══██╗
██║░░██║
╚═╝░░╚═╝""",
"""
██████╗░
██╔══██╗
██████╔╝
██╔══██╗
██║░░██║
╚═╝░░╚═╝""",
"""
██╗░░░██╗
╚██╗░██╔╝
░╚████╔╝░
░░╚██╔╝░░
░░░██║░░░
░░░╚═╝░░░""",
"""
██╗░░██░
██║░░██║
███████║
██╔══██║
██║░░██║
╚═╝░░╚═╝""",
"""
╗█████╗░
██╔══██╗
██║░░██║
██║░░██║
╚█████╔╝
░╚════╝░""",
"""
╗█████╗░
██╔══██╗
██║░░██║
██║░░██║
╚█████╔╝
░╚════╝░""",
"""
██╗░░██╗
██║░██╔╝
█████═╝░
██╔═██╗░
██║░╚██╗
╚═╝░░╚═╝"""
]

def getLine(line):
    list = []
    for i in letters:
        lines = i.split('\n')
        if line < len(lines):
            list.append(lines[line])
    return list

def __init__():
    for i in range(7):
        i = i + 1
        time.sleep(0.5)
        print(f"""{colorama.Fore.MAGENTA} {''.join(getLine(i))}""")
    print(f"{colorama.Fore.MAGENTA} the perry hook(real)\n{colorama.Fore.RESET}")
    time.sleep(0.4)
    print(tabulate([[f"{colorama.Fore.YELLOW}1{colorama.Fore.RESET}", f"{colorama.Fore.GREEN}Webhook Nuker{colorama.Fore.RESET}", "sends the funny packet to discord hooks"]], [f"{colorama.Fore.LIGHTRED_EX}ID{colorama.Fore.RESET}", f"{colorama.Fore.LIGHTRED_EX}Name{colorama.Fore.RESET}", f"{colorama.Fore.LIGHTRED_EX}Description{colorama.Fore.RESET}"], tablefmt="fancy_grid"))

