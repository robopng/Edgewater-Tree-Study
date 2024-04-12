path = "C:\\Users\\robop\\PycharmProjects\\edgewater tree data\\venv\\src\\inputs\\Copy of Edgewater Heritage Tree Data - EPIC.csv"
path2 = "C:\\Users\\robop\\PycharmProjects\\edgewater tree data\\venv\\src\\outputs\\Copy of Edgewater Heritage Tree Data - EPIC.csv"
with (open(path,mode='r') as input_file,
      open(path2,mode='w') as output_file):
    input_file.readline()
    i = 0
    for line in input_file:
        i += 1
        line = line.upper()
        addr = line[:line.index(',')]
        addr = addr.split(' ')
        print(addr)
        addr[1] = 'N' if int(addr[0]) > 3000 else 'W'
        output_file.write(f'{i},{addr[0]} {addr[1]} {addr[2]},CHICAGO,IL,60660\n')

