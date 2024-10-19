import time

def print_lbl(string: str) -> None:
    """print letter by letter

    Args:
        string (str): string to print letter by letter
    """
    for character in string:
        print(character, end='') # end='' to avoid new line at each character
        time.sleep(0.01) # adds a cooldown between each character printed