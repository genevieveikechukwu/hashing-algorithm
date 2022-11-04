# """
# Creating a programme to generate a json file and a sha256 and output.csv

# Algirithm

# 1. Prompt user to enter a csv input. (not specified in question...skipping.)
# 2. Scan and sort through the csv collecting data.
# 3. Use the collected data to generate a json file.
# 4. Create your sha256 hash from the json file.
# 5. Append it to another line in the csv (for each rows).
# 6. Return a new csv file titled originalfilename.output.csv with the new line containing the sha256.

# """
import json
import csv
import ast

# # importing modules from other scripts.....



from response import read_csv
from hashed import hash_json


# using pandas library
import pandas as pd
read_csv() 
hash_json()

# path to json file
df = pd.read_json (r'./json_output/all-teams.txt')

# path where it will be saved
df.to_csv (r'./csv_output/nft-all-teams.csv', index = 1)