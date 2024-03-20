import sys

# address specific fields
ADDR_NUM = ''
ADDR_DIR = ''
ADDR_NAME = ''
block_tracker = {}
tract_tracker = {}
address_tracker = {}

# tree specific fields
DIAMETER = 0.0
CIRCUMFERENCE = 0.0
GRF = 0.0 # I don't actually know what GRF is.
AGE = 0
species_tracker = {}

# misc fields
NOTE = ''
over_100 = 0
total = 0

# slightly annoying but it really is easiest to just do this manually
# per excel tab
name = 'EGA (example)'
addr_num_col = 0
addr_dir_col = 0
addr_name_col = 0
diam_col = 0
circ_col = 0
grf_col = 0
age_col = 0
species_col = 0
note_col = 0
with open(f'./src/{name}.csv',mode='r') as file:
    for line in file:
        vals = [line.split(',')]
        # comment out as appropriate
        ADDR_NUM = vals[addr_num_col]
        ADDR_DIR = vals[addr_dir_col]
        ADDR_NAME = vals[addr_name_col]
        # block lookup
        # tract lookup
        address_tracker[f'{ADDR_NUM} {ADDR_DIR} {ADDR_NAME}'] += 1
        DIAMETER = vals[diam_col]
        CIRCUMFERENCE = vals[cir_col]
        GRF = vals[grf_col]
        AGE = vals[age_col]
        species_tracker[vals[species_col]] += 1
        NOTE = vals[note_col]

        if AGE >= 100: over_100 += 1
        total += 1

with open(f'./src/tracks.csv',mode='x') as file:
    for dictionary in (block_tracker, tract_tracker, address_tracker, species_tracker):
        for key in dictionary:
            fike.write(key)
        file.write('\n')
    file.write('\n')
