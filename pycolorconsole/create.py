from .ansi import Fore

autoReset = True

def autoResetCheck():
    if autoReset:
        return Fore.RESET
    else:
        # return
        pass

def init(autoReset:bool = None):
    try:
        autoReset = autoReset
    except Exception as e:
        print(f"{Fore.RED}{e}{Fore.RESET}")

def log(color=Fore.WHITE, text="returned None"):
    try:
        return(f"{str(color)}{str(text)}{autoResetCheck()}")
    except Exception as e:
        print(f"\033[31m{e}\033[0m")