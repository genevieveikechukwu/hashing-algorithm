"""
Writing a function to readlines in a csv.
"""

# Importing the package
import csv
import json

# setting the file path




# storing the data
data = {}
def read_csv():
    csvFilePath = input('Enter the file path to your csv, e.g: ./csv_input/t_csv_file_csv.csv ')
    jsonpath = input('Enter the path where the generated json will be stored e.g: ./json_output/file.json ')
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['Name']
            data[key] = rows

# write data into a new json file

    with open(jsonpath, 'w',  encoding='utf-8') as jsonFile:
        # adding enugh spaces for readability.
        jsonFile.write(json.dumps(data, indent=4))

read_csv()

    

