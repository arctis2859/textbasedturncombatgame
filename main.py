import random
import math
import time
import sys
global playerHP
global opponentHP
global x
global y


def playerTurn():
    global playerHP
    if playerHP < 0:
        playerDeath()
    else:
        a = input("\033[0;37;48mAttack(a) or heal(h): ")
        if a == "a":
            playerAttack()
        elif a == "h":
            playerHealCounter()
        else:
            print("\033[0;31;50mEnter 'a' or 'h'.")
            playerTurn()


def opponentTurn():
    global opponentHP
    if opponentHP < 0:
        opponentDeath()
    else:
        b = random.randint(1, 2)
        if b == 2:
            opponentHealCounter()
        else:
            opponentAttack()


def playerAttack():
    global opponentHP
    global x
    global y
    x = x - 1
    y = y - 1
    playerDmg = random.randint(50, 100)
    playerCritchance = random.randint(1, 3)
    playerCritint = random.randint(1, 3)
    playerCritmultiplier = random.randint(120, 200)
    if playerCritint == playerCritchance:
        playerDmg = 100
        playerNetdmg = playerDmg * (playerCritmultiplier * 0.01)
        playerNetdmg = math.ceil(playerNetdmg)
        opponentHP = opponentHP - playerNetdmg
        print("\033[0;37;48mYou land a critical hit, dealing", playerNetdmg, "damage to the enemy. The enemy has",
              opponentHP, "health remaining.")
        opponentTurn()
    else:
        opponentHP = opponentHP - playerDmg
        print("\033[0;37;48mYou strike the enemy, dealing", playerDmg, "damage. The enemy has", opponentHP,
              "health remaining.")
        opponentTurn()


def playerHealCounter():
    global x
    if x > 1:
        print("\033[0;31;50mYou cannot heal for another", x, "turns.")
        playerTurn()
    else:
        playerHeal()


def playerHeal():
    global playerHP
    global x
    global y
    x = 8
    y = y - 1
    c = random.randint(100, 200)
    playerHP = playerHP + c
    if playerHP > 1000:
        playerHP = 1000
        print("\033[0;37;48mHealed", c, "health")
        opponentTurn()
    else:
        print("\033[0;37;48mHealed", c, "health.")
        opponentTurn()


def playerDeath():
    print("YOU DIED!")
    sys.exit()


def opponentAttack():
    time.sleep(1)
    global playerHP
    global x
    global y
    x = x - 1
    y = y - 1
    opponentDmg = random.randint(50, 100)
    opponentCritchance = random.randint(1, 3)
    opponentCritint = random.randint(1, 3)
    opponentCritmultiplier = random.randint(120, 200)
    if opponentCritint == opponentCritchance:
        opponentDmg = 100
        opponentNetdmg = opponentDmg * (opponentCritmultiplier * 0.01)
        opponentNetdmg = math.ceil(opponentNetdmg)
        playerHP = playerHP - opponentNetdmg
        print("\033[0;37;48mThe enemy lands a critical hit, dealing", opponentNetdmg, "damage. You have", playerHP,
              "health remaining.")
        playerTurn()
    else:
        playerHP = playerHP - opponentDmg
        print("\033[0;37;48mThe enemy strikes you, dealing", opponentDmg, "damage. You have", playerHP,
              "healh remaining.")
        playerTurn()


def opponentHealCounter():
    global y
    if y > 1:
        opponentAttack()
    else:
        opponentHeal()


def opponentHeal():
    time.sleep(1)
    global opponentHP
    global x
    global y
    y = 8
    x = x - 1
    d = random.randint(100, 200)
    opponentHP = opponentHP + d
    if opponentHP > 1000:
        opponentHP = 1000
        print("\033[0;37;58mThe enemy healed", d, "health.")
        playerTurn()
    else:
        print("\033[0;37;48mThe enemy healed", d, "health.")
        playerTurn()


def opponentDeath():
    print("YOU WIN!")
    sys.exit()


def reset():
    global playerHP
    global opponentHP
    global x
    global y
    playerHP = 1000
    opponentHP = 1000
    x = 1
    y = 1
    playerTurn()


reset()
