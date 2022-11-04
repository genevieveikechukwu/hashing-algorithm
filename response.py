"""
Writing a function to readlines in a csv.
"""

# Importing the package
import csv
import json

# setting the file path




# storing the data

def read_csv():
    csvFilePath = './csv_input/nft-all-teams.csv'
    jsonpath = './json_output/all-teams.txt'
    data = {}
    with open(csvFilePath,) as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['Serial Number']
            data[key] = rows

# write data into a new json file

    with open(jsonpath, 'w') as jsonFile:
        # adding enugh spaces for readability.
        jsonFile.write(json.dumps(data))

read_csv()

    

