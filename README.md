# PyGOL

![GoL Demo](/docs/demo.png?raw=true)

Python implementation of Conway's Game of Life

## Dependencies

GoL uses standard python3, with (https://github.com/willmcgugan/rich)[Rich] library for coloring

## Basic rules:

+ Any live cell with two or three live neighbours survives.
+ Any dead cell with three live neighbours becomes a live cell.
+ All other live cells die in the next generation. Similarly, all other dead cells stay dead.
