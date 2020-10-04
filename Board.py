from Slot import Slot, SlotState

class Board:

    def __init__(self):
        self.prevFrame = ""
        self.output = ""
        self.width = 25
        self.height = 25
        self.grid = [[Slot() for y in range(self.width)] for x in range(self.height)]

    def update(self):
        for y in range(self.height):
            for x in range(self.width):
                self.updateSlot(x, y)
        self.render()
        if self.prevFrame == self.output:
            return False
        self.prevFrame = self.output #update prevFrame
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

    def render(self):
        self.output = ""
        for y in range(self.height):
            for x in range(self.width):
                self.output += self.grid[y][x].render()
            self.output += "\n"