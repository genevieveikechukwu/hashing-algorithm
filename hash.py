import hashlib
import json


filename = './json_output/file.json'


def hash_json():
    with open('./json_output/file.json', 'rb') as f:
        for line in f:
            hashed_line ={ 'hash': hashlib.sha256(line.rstrip()).hexdigest() }
            # print(hashed_line)

    entry = hashed_line 
# entry = [hashed_line]
# print(entry)

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data.update(entry)
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

hash_json()


    






    # print(added_field)
    # print(added_field)