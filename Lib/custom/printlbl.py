from time import sleep

def print_lbl(string: str) -> None:
    """print letter by letter

    Args:
        string (str): string to print letter by letter
    """
    for character in string:
        print(character, end='', flush=True)
        sleep(0.02) # cooldown entre chaque caractère
    print() # nouvelle ligne entre chaque string
    sleep(0.7) # cooldown entre chaque string