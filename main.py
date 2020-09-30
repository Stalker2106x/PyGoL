from Board import Board
import time
import sys

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

#  Any live cell with two or three live neighbours survives.
#  Any dead cell with three live neighbours becomes a live cell.
#  All other live cells die in the next generation. Similarly, all other dead cells stay dead.

board = Board()
board.draw()
while 1:
  time.sleep(1)
  print("") #Skip line
  board.update()
  board.draw()