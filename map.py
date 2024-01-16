from settings import *

text_map = [
    '111111111111',
    '1.....2....1',
    '1.22.....2.1',
    '1..........1',
    '1.22.......1',
    '1.2......2.1',
    '1.....2....1',
    '111111111111'
]

world_map = {}
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            if char == '2':
                world_map[(i * TILE, j * TILE)] = '2'