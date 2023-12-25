
class ColorPalette:
    WHITE = "\033[37m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"

autoReset = True

def init(autoReset:bool):
    try:
        autoReset = autoReset
    except Exception as e:
        print(f"\033[31m{e}\033[0m")

def log(color=ColorPalette.WHITE, text="returned None"):
    try:
        def autoResetCheck():
            if autoReset:
                return("\033[0m")
            else:
                return ""
        return(f"{str(color)}{str(text)}{autoResetCheck()}")
    
    except Exception as e:
        print(f"\033[31m{e}\033[0m")