from Board import Board
import time
import sys
import os

delay = 2 # Delay between frames in seconds

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)
sys.stdout = Unbuffered(sys.stdout)

clr()
board = Board()
board.draw()
while board.update():
    time.sleep(delay)
    clr()
    board.draw()