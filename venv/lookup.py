# read 9 times

path = ".\\src\\inputs\\master_copy.csv"
path_out = ".\\src\\outputs\\addresses.csv"
counter = 1

with (open(path) as file, open(path_out,mode='w') as out):
    for line in file:
        line = line.split(',')
        line = f'{line[0]} {line[1]} {line[2]}'
        if "BROKEN!" in line or len(line) < 6 or line.upper() != line:
            line='26 E PEARSON'
        line = f'{counter},{line},Chicago,IL,60660\n'
        out.write(line)
        counter += 1


# curl --form benchmark=Public_AR_Current --form address="4600 Silver Hill Rd, Washington, DC 20233" https://geocoding.geo.census.gov/geocoder/locations/onlineaddress?parameters
# curl --form addressFile=@addresses.csv --form benchmark=Public_AR_Current https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output geocoderesult.csv