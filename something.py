#Tin NGuyen
from madison_axi.axi import *


def spiky_circle():
    initialize()

    move_to(100, 0)
    point_in_direction(260)
    pen_down()

    for i in range(50):
        move_forward(127)
        turn_right(127)

        cleanup()

if __name__ == "__main__":
    spiky_circle()
