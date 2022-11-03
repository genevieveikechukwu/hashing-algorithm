"""
Creating a programme to generate a json file and a sha256 and output.csv

Algirithm

1. Prompt user to enter a csv input. (not specified in question...skipping.)
2. Scan and sort through the csv collecting data.
3. Use the collected data to generate a json file.
4. Create your sha256 hash from the json file.
5. Append it to another line in the csv (for each rows).
6. Return a new csv file titled originalfilename.output.csv with the new line containing the sha256.

"""
import json
import csv
import ast

# importing modules from other scripts.....



from response import read_csv
from hashed import hash_json


filename = input('Enter the path to the appended json, e.g: ./json_output/file.json ')
output = input('Enter the path where you want your csv to be stored e.g: ./csv_output/filename.output.csv ')



def output_csv():
    read_csv()
    hash_json()

    with open(filename) as json_file:
        json_data = json.load(json_file)
    data_file = open(output, 'w', newline='')
    csv_writer = csv.writer(data_file)
    count = 0

    for data in json_data:
        if count == 0:
            json_data = ast.literal_eval(json_data)
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
            csv_writer.writerow(data.values())
            data_file.close()
            break
output_csv()

