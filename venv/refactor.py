import os

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
addr_col = 0
addr_num_col = 0
addr_dir_col = 1
addr_name_col = 2
diam_col = 4
cir_col = 2
grf_col = 5
age_col = 6
species_col = 3
note_col = 1

name = 'EBNA.csv'
with (open(f'./src/inputs/{name}',mode='r') as input,
      open(f'./src/outputs/{name}',mode='w') as output,
      open(f'./src/outputs/tracker_{name}', mode='w') as tracker):
    # skip the header
    input.readline()
    output.write('ADDR_NUM,ADDR_DIR,ADDR_NAME,TRACT,BLOCK,'
                 + 'CIRCUMFERENCE,SPECIES,DIAMETER,GRF,AGE,NOTE\n')
    for line in input:
        # rstrip mainly for trailing newline
        vals = line.rstrip().split(',')

        # address specific fields
        addr = (vals[addr_col]).split(' ')
        ADDR_NUM = addr[0]
        ADDR_DIR = 'W' if int(ADDR_NUM) <= 3000 else 'N'
        # ADDR_DIR = addr[addr_dir_col].upper()
        ADDR_NAME = addr[len(addr) - 1].upper()
        BLOCK = ''
        TRACT = ''
        addr = f'{ADDR_NUM} {ADDR_DIR} {ADDR_NAME}'
        if addr not in address_tracker:
            address_tracker[addr] = 0
        address_tracker[addr] += 1

        # tree specific fields
        DIAMETER = vals[diam_col]
        CIRCUMFERENCE = vals[cir_col]
        GRF = vals[grf_col]
        AGE = vals[age_col]
        SPECIES = vals[species_col].upper()
        if SPECIES not in species_tracker:
            species_tracker[SPECIES] = 0
        species_tracker[SPECIES] += 1

        # misc fields
        NOTE = vals[note_col] if vals[note_col] != '' else ' '
        if float(AGE) >= 100: over_100 += 1
        total += 1

        output.write(f'{ADDR_NUM},{ADDR_DIR},{ADDR_NAME},{TRACT},{BLOCK},{CIRCUMFERENCE}'
                     + f',{SPECIES},{DIAMETER},{GRF},{AGE},{NOTE}\n')
    output.write('\n')

    for dictionary in (block_tracker, tract_tracker, address_tracker, species_tracker):
        for key in dictionary:
            tracker.write(f'{key}:{dictionary[key]}\n')
        tracker.write('\n')
    tracker.write(f'{over_100}\n')
    tracker.write(f'{total}\n')
    tracker.write('\n')
