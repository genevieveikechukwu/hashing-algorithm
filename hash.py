import hashlib
import json


jsonpath = './output/file.json'

with open('./output/file.json', 'rb') as f:
    for line in f:
        hashed_line ={ 'hash': hashlib.sha256(line.rstrip()).hexdigest() }
        # print(hashed_line)
with open('./output/file.json','r+') as file:
    z = json.load(file)
    z.update(hashed_line)
    added_field = json.dumps(z, indent = 4)

with open(jsonpath, 'w',  encoding='utf-8') as jsonFile:
#     # adding enugh spaces for readability.
    jsonFile.write(json.dumps(added_field))

    # print(added_field)
    # print(added_field)