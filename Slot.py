from enum import IntEnum
from random import randint
import rich

class SlotState(IntEnum):
    empty = 0
    alive = 1
    dead = 2

class Slot:

    character = "\u2588"

    def __init__(self, state = -1):
        if state == -1:
            self.state = (SlotState.empty, SlotState.alive)[randint(0, 5) == 0]
        else:
            self.state = state

    def update(self, aliveNeighbours):
        if self.state == SlotState.empty:
            pass # do nothing
        elif self.state == SlotState.alive and (aliveNeighbours == 2 or aliveNeighbours == 3):
            self.state = SlotState.alive
        elif self.state == SlotState.dead and aliveNeighbours == 3:
            self.state = SlotState.alive
        elif self.state == SlotState.dead:
            self.state = SlotState.empty
        else:
            self.state = SlotState.dead

    def draw(self):
        if self.state == SlotState.empty:
            rich.print("[bold white]"+Slot.character+"[/bold white]", end="")
        elif self.state == SlotState.alive:
            rich.print("[bold green]"+Slot.character+"[/bold green]", end="")
        elif self.state == SlotState.dead:
            rich.print("[bold gray]"+Slot.character+"[/bold gray]", end="")