from colorama import Fore, init

# Colors
init()
class color:
    colors = {
        "reset": Fore.RESET,
        "red": Fore.RED,
        "yellow": Fore.YELLOW,
        "black": Fore.BLACK,
        "blue": Fore.BLUE,
        "cyan": Fore.CYAN,
        "green": Fore.GREEN,
        "magenta": Fore.MAGENTA
    }

    @classmethod
    def place(cls, color: str):
        """
        :usage: print(color.place("cyan"))
        :param color: string of the color
        :return: Color Value
        """
        return cls.colors[color.lower()]
# Colors