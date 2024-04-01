import csv

file = []
path_in = ".\\src\\inputs\\result3.csv"
path_out = ".\\src\\outputs\\tracts_and_blocks.csv"

with (open(path_in) as input_file,
      open(path_out,mode='w') as output_file):
    for line in input_file:
        split = [item for item in csv.reader([line], skipinitialspace=True)][0]
        file.append(split)

    file = sorted(file,key=lambda l: int(l[0]))

    for line in file:
        output_file.write(f'{line[-2]},{line[-1]}\n')
