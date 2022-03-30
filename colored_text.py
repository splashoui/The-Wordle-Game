import colorama
from colorama import init, Fore, Back, Style # To output the letters colorful.

class ColoredText(object):

    """ 
    
    Highlights the letters with 3 different color options such as Green/Yellow/White  

    """
    
    colorama.init()  # That line is doing the magic!
    
    def __init__(self, letter: str):
        self.letter = letter

    def in_spot(self):
        return print(Back.GREEN + Fore.BLACK + f"{self.letter.upper()}" + Style.RESET_ALL,end='')

    def not_in_spot(self):
        return print(Back.YELLOW + Fore.BLACK + f"{self.letter.upper()}" + Style.RESET_ALL,end='')

    def not_in_word(self):
        return print(Back.WHITE + Fore.BLACK + f"{self.letter.upper()}" + Style.RESET_ALL,end='')
