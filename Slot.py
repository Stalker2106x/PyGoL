from enum import IntEnum
from random import randint

class SlotState(IntEnum):
    empty = 0
    alive = 1
    dead = 2

class Slot:

    def __init__(self, state = -1):
        if state == -1:
            self.state = (SlotState.empty, SlotState.alive)[randint(0, 2) == 2]
        else:
            self.state = state

    def update(self, aliveNeighbours):
        if self.state == SlotState.empty:
            pass # do nothing
        elif self.state == SlotState.alive and (aliveNeighbours == 2 or aliveNeighbours == 3):
            self.state = SlotState.alive
        elif self.state == SlotState.dead and aliveNeighbours == 3:
            self.state = SlotState.alive
        else:
            self.state = SlotState.dead

    def render(self):
        output = ""
        if self.state == SlotState.empty:
            output += "."
        elif self.state == SlotState.alive:
            output += "O"
        elif self.state == SlotState.dead:
            output += "x"
        return (output)