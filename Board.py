class Board:

    def __init__(self):
        self.width = 25
        self.height = 25
        self.grid = []
        for y in range(self.height):
            self.grid.append([])


    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                print(".", end='')
            print("") #newline