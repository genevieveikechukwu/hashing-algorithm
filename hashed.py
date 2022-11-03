import hashlib
import json





def hash_json():
    filename = input('Enter the path where the appended json will be stored e.g: ./json_output/file.json ')
    with open(filename, 'rb') as f:
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
        json.dump(data, file, indent=4, sort_keys=True)

hash_json()


    






    # print(added_field)
    # print(added_field)