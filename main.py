"""
File:    main.py
Author1:  Arctis   (https://github.com/XxArcticAssassinxX)
Author2:  M0RGANZ  (https://github.com/morganzwest) [https://morganz.co.uk]
"""

import random
import math
import time
import sys
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

dev = True


def print_type(array, speed=0.02):
    """
    This function takes an array of values then flushes each
    character "one by one" outputs them instead of default print()

    :param array: Array of values to be printed
    :param speed: The partition between each character being printed
    :return: None
    """

    a = []
    for node in array:
        a.append(str(node))

    a.append("\n")
    if not dev:  # Within the PyCharm Environment outputting characters at this speed can cause issues

        for string in a:
            for char in string:
                time.sleep(speed)
                sys.stdout.write(char)
                sys.stdout.flush()

    else:
        print(a)


# This will store the BOT and PLAYER so they are easily accessible
characters = []


class Character:
    def __init__(self, health: int, bot=False):
        self.hp = health
        self.heal_cooldown = 1
        self.bot = bot
        self.opponent = None

    def set_op(self):
        """
        This function assigns the other instance as the opponent
        :return: None
        """

        if self.bot:
            self.opponent = characters[0]
        else:
            self.opponent = characters[1]

    def __check_helth(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def turn(self):
        """
        This function will be run every single loop
        It checks which move the player wants to play
        and then runs the other functions within the class

        :return: Sub Formative's
        """
        if self.__check_helth():  # Null Move Check
            if self.bot:
                c = random.randint(1, 2)
                if c == 2:
                    self.heal_check()
                else:
                    self.attack()
            else:
                print_type(["Attack(A) or heal(H): "])
                answer = input("> ")
                # answer.lower() just so the player cannot break the script as easily
                if answer.lower() == "a":
                    self.attack()
                elif answer.lower() == "h":
                    self.heal_check()
                else:
                    print_type([color.place("red"), "Enter 'a' or 'h'.", color.place("reset")])
                    self.turn()

    def attack(self):
        """
        This function conditions all the damage onto the other instance
        :return: None
        """
        self.heal_cooldown -= 1
        self.opponent.heal_cooldown -= 1
        player_dmg = random.randint(50, 100)
        player_critical_chance = random.randint(1, 3)
        player_critical_int = random.randint(1, 3)
        player_net_dmg = random.randint(120, 200)

        if player_critical_int == player_critical_chance:

            player_net_dmg = math.ceil(player_net_dmg)
            self.opponent.hp -= player_net_dmg

            # Different outputs depending if it is the BOT instance
            if not self.bot:
                print_type(["You land a critical hit, dealing ", player_net_dmg, " damage to the enemy. The enemy has ",
                            self.opponent.hp, " health remaining."])
            else:
                print_type(["Opponent hit a critical hit, dealing ", player_net_dmg, " damage to you. You have ",
                            self.opponent.hp, " health remaining."])
        else:
            self.opponent.hp -= player_dmg
            if not self.bot:
                print_type(["You strike the enemy, dealing ", player_dmg, " damage. The enemy has ", self.opponent.hp,
                            " health remaining."])
            else:
                print_type(["The enemy strikes, dealing ", player_dmg, " damage. You now have ", self.opponent.hp,
                            " health remaining."])

    def heal_check(self):
        """
        Check if the cooldown is at zero to allow for healing
        :return: None
        """
        if self.heal_cooldown > 0:
            if not self.bot:
                print_type(["You cannot heal for another ", self.heal_cooldown, " turns."])
                self.turn()
            else:
                self.attack()
        else:
            self.heal()

    def heal(self):
        """
        Reset the cooldown to default and output the random health change
        :return: None
        """
        self.heal_cooldown = 8
        self.opponent.heal_cooldown -= 1
        c = random.randint(100, 200)
        self.hp += c
        if self.hp > 1000:
            self.hp = 1000

        # Different output depending on if the instance is a BOT
        if not self.bot:
            print_type(["Healed ", c, " health."])
        else:
            print_type(["Opponent Healed ", c, " health"])

    def death(self):
        if not self.bot:
            print_type(["You DIED"])
        else:
            print_type(["YOU KILLED THE BOT"])


def reset():
    """
    Setup the game
    :return: None
    """
    player = Character(1000)
    bot = Character(1000, bot=True)
    characters.append(player)
    characters.append(bot)

    player.set_op()
    bot.set_op()

    run = True
    while run:

        if dev:
            for c in characters:
                print(c.bot, c.hp, c.heal_cooldown)

        # Check the array of characters in-case one of them is dead
        for character in characters:
            if character.hp <= 0:

                character.death()
                # Break the game loop
                run = False

            else:
                character.turn()

    # When the game ends this will run
    else:
        print_type(["A GAME BY:\n"])
        time.sleep(.5)
        print("Arctis:   https://github.com/XxArcticAssassinxX")
        print("M0RGANZ:  https://github.com/morganzwest - https://morganz.co.uk")
        time.sleep(15)  # Hold the window open


if __name__ == "__main__":
    reset()
