import sys

# address specific fields
# tracked: addr, tract, block
ADDR, TRACT, BLOCK = {},{},{}
ADDR_NUM, ADDR_DIR, ADDR_NAME = '','',''
# tree specific fields
# tracked: species
DIAMETER, CIRCUMFERENCE, AGE, SPECIES, GRF = {},{},{},{},{}
# misc fields
NOTE = {}

name = 'EGA (example)'
with open(f'./src/{name}.csv',mode='r') as file:
    pass

with open(f'./src/tracks.csv',mode='x') as file:
    pass
