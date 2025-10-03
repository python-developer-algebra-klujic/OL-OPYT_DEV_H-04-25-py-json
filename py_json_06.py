import json


def load_from_json_file(file_name='users.json'):
    try:
        with open(file_name, 'r') as file_reader:
            return json.load(file_reader)
        
    except Exception as ex:
        print(f'Dogodila se greska: {ex}')


data_from_file = load_from_json_file()
print(data_from_file)

for user in data_from_file:
    print(user['name'], user['email'])
