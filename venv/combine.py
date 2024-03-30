import os
import csv
directory = os.fsencode("src\\csvs\\")
output = "C:\\Users\\robop\\PycharmProjects\\edgewater tree data\\venv\\src\\outputs\\combined.csv"
unique_items = {}

with open(output,mode='w') as output_file:
    for file in os.listdir(directory):
        with open(file, mode='r') as input_file:
            for line in input_file:
                split = csv.reader([line], skipinitialspace=true)
                print(split)