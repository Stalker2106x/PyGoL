from Slot import Slot, SlotState
from enum import Enum
import hashlib

class Border(Enum):
    Top = 0
    Right = 1
    Bottom = 2
    Left = 3
    

class Board:

    horizontalBorder = "\u2550"
    verticalBorder = "\u2551"
    cornerTL = "\u2554"
    cornerTR = "\u2557"
    cornerBL = "\u255A"
    cornerBR = "\u255D"

    def __init__(self):
        self.prevFrame = ""
        self.width = 25
        self.height = 25
        #stats
        self.generation = 0
        self.aliveCells = 0
        self.deadCells = 0

        self.grid = [[Slot() for y in range(self.width)] for x in range(self.height)]

    def update(self):
        for y in range(self.height):
            for x in range(self.width):
                self.updateSlot(x, y)
        frame = self.dump()
        if self.prevFrame == frame:
            return False
        self.prevFrame = frame #update prevFrame
        self.generation += 1
        return True

    def updateSlot(self, x, y):
        aliveNeighbours = 0
        xMin = x - 1
        if xMin < 0:
            xMin = 0
        xMax = x + 2
        if xMax > self.width:
            xMax = self.width
        yMin = y - 1
        if yMin < 0:
            yMin = 0
        yMax = y + 2
        if yMax > self.height:
            yMax = self.height
        for y in range(yMin, yMax):
            for x in range(xMin, xMax):
                if self.grid[y][x].state == SlotState.alive:
                    aliveNeighbours += 1
        self.grid[y][x].update(aliveNeighbours)

    def dump(self):
        output = ""
        for y in range(self.height):
            for x in range(self.width):
                output += str(self.grid[y][x].state)
        return hashlib.md5(output.encode())

    def drawBorder(self, border, y=-1):
        if border == Border.Left:
            print(Board.verticalBorder+" ", end="")
        elif border == Border.Right:
            if y == 0:
                print(" Generation:  "+str(self.generation).zfill(4), end="")
            elif y == 2:
                print(" Alive Cells: "+str(self.aliveCells).zfill(4), end="")
            elif y == 4:
                print(" Dead Cells:  "+str(self.deadCells).zfill(4), end="")
            else:
                print("                  ", end="")
            print(" "+Board.verticalBorder)
        elif border == Border.Top:
            print(Board.cornerTL, end="")
            for x in range(self.width+20):
                print(Board.horizontalBorder, end="")
            print(Board.cornerTR)
        elif border == Border.Bottom:
            print(Board.cornerBL, end="")
            for x in range(self.width+20):
                print(Board.horizontalBorder, end="")
            print(Board.cornerBR)


    def draw(self):
        self.aliveCells = 0
        self.deadCells = 0
        self.drawBorder(Border.Top)
        for y in range(self.height):
            self.drawBorder(Border.Left)
            for x in range(self.width):
                cell = self.grid[y][x]
                cell.draw()
                if cell.state == SlotState.alive:
                    self.aliveCells += 1
                elif cell.state == SlotState.dead:
                    self.deadCells += 1
            self.drawBorder(Border.Right, y)
        self.drawBorder(Border.Bottom)