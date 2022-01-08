import json


def read_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
    
''' data = read_json_file('pets.json');

print(data) '''