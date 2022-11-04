import hashlib
import json





def hash_json():
    filename = './json_output/all-teams.txt'
    with open(filename, 'rb') as f:
        for line in f:
            hashed_line ={ 'hash': hashlib.sha256(line.rstrip()).hexdigest() }
            # print(hashed_line)

    # entry = hashed_line 
# entry = [hashed_line]
# print(entry)

    with open(filename, 'r') as file:
        data = json.load(file)
        data.update(hashed_line)
    with open(filename, 'w') as file:
        json.dump(data, file)

hash_json()


    






    # print(added_field)
    # print(added_field)