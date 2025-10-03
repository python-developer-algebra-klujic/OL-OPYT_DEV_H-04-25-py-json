import requests


def load_from_json_web():
    URL = 'https://jsonplaceholder.typicode.com/users'
    try:
        return requests.get(URL).json()
        
    except Exception as ex:
        print(f'Dogodila se greska: {ex}')


data_from_web = load_from_json_web()


for user in data_from_web:
    print(user['name'], user['email'])
