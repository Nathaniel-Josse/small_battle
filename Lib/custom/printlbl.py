from time import sleep

def print_lbl(string: str) -> None:
    """print letter by letter

    Args:
        string (str): string to print letter by letter
    """
    for character in string:
        print(character, end='', flush=True)
        sleep(0.02) # adds a cooldown between each character printed
    print() # new line at the end of the string
    sleep(0.7) # adds a cooldown between each string printed