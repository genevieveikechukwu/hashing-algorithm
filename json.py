"""
Writing a function to readlines in a csv.
"""

# Importing the package
import csv, json

# setting the file path

csvFilePath = 't_csv_file_csv.csv'
jsonpath = './output/'


# storing the data
data = {}

with open(csvFilePath) as csvfile:
    csvReader = csv.DictReader(csvfile)
    for rows in csvReader:
        id = rows['id']
        data[id] = rows

# write data into a new json file

with open(jsonpath, 'w') as jsonFile:
    # adding enugh spaces for readability.
    jsonFile.write(json.dumps(data, indent=4))

