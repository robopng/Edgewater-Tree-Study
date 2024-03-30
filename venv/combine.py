import os
import csv
import unicodedata
directory = os.fsencode("src\\csvs\\")
output = "src\\outputs\\combined.csv"
tracker = "src\\outputs\\tracker.csv"
unique_items = {}

addr_num_col = 0
addr_dir_col = 1
addr_name_col = 2
tract_col = 3
block_col = 4
cir_col = 5
spec_col = 6
diam_col = 7
grf_col = 8
age_col = 9
note_col = 10
misc_col = 11
header = 'ADDR_NUM,ADDR_DIR,ADDR_NAME,TRACT,BLOCK,CIRCUMFERENCE,SPECIES,DIAMETER,GRF,AGE,NOTE,'

with (open(output,mode='w') as output_file,
      open(tracker,mode='w') as tracker_file):
    output_file.write(header)
    for file in os.listdir(directory):
        file = file.decode('utf-8')
        with open(f'src\\csvs\\{file}', mode='r') as input_file:
            output_file.write('\n')
            # clear top line of csv
            input_file.readline()
            for line in input_file:
                line = line.upper()
                split = [item for item in csv.reader([line], skipinitialspace=True)][0]

                if split[addr_num_col] == '0' or split[addr_num_col] == ''\
                   or split[age_col] == '0' or split[spec_col] == '':
                    output_file.write(f'BROKEN! NEEDS FIXING: {line}')
                    continue

                addr = f'{split[addr_num_col]} {split[addr_dir_col]} {split[addr_name_col]}'
                for tracker in ('TOTAL COMPLETE', split[spec_col]):
                    if tracker not in unique_items:
                        unique_items[tracker] = 0
                    unique_items[tracker] += 1

                output_file.write(line)

    for key in unique_items:
        tracker_file.write(f'{key}:{unique_items[key]}\n')
    tracker_file.write('\n')