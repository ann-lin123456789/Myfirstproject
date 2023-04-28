"""
File: Steeplechase.py
Name: Ann Lin
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(12):
        if front_is_clear():
            move()
        else:
            jump()



def jump():
    """
    pre_condition:Karel is on the left,facing east
    post_condition:Karel is on the right,facing east
    """
    up()
    cross()
    down()

def up():
    while not front_is_clear():
        turn_left()
        move()
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def cross():
    move()
    turn_right()

def down():
    while front_is_clear():
        move()
    turn_left()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
