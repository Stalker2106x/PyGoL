from enum import IntEnum
from random import randint

class CellState(IntEnum):
    empty = 0
    living = 1
    dead = 2

class Board:

    def __init__(self):
        self.width = 25
        self.height = 25
        self.grid = [[(CellState.empty, CellState.living)[randint(0, 2) == 2] for y in range(self.width)] for x in range(self.height)]

    def update(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == CellState.living:
                    self.updateCell(x, y)

    def updateCell(self, x, y):
        state = self.grid[y][x]
        neighbours = []
        try:
            for ry in range(y-1, y+1):
                neighbours.append(self.grid[ry-1][x])
                if ry != y:
                    neighbours.append(self.grid[ry][x])
                neighbours.append(self.grid[ry+1][x])
        except IndexError:
            a=0
            #Do nothing
        aliveNeighbours = 0
        deadNeighbours = 0
        for i in range(len(neighbours)):
            if neighbours[i] == CellState.living:
                aliveNeighbours += 1
            if neighbours[i] == CellState.dead:
                deadNeighbours += 1
        if state == CellState.living:
            if aliveNeighbours == 2 or aliveNeighbours == 3:
                self.grid[y][x] = CellState.living
            else:
                self.grid[y][x] = CellState.dead
        elif state == CellState.dead:
            if aliveNeighbours == 3:
                self.grid[y][x] = CellState.living
            else:
                self.grid[y][x] = CellState.empty


    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == CellState.empty:
                    print(".", end="")
                if self.grid[y][x] == CellState.living:
                    print("O", end="")
            print("") #newline