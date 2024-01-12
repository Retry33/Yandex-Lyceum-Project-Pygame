from settings import *

text_map = [
    '1111111111111',
    '1...........1',
    '1.1.1.1.1.1.1',
    '1...........1',
    '1.1.1.1.1.1.1',
    '1...........1',
    '1.1.1.1.1.1.1',
    '1...........1',
    '1111111111111',
]

world_map = {}
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            if char == '2':
                world_map[(i * TILE, j * TILE)] = '2'