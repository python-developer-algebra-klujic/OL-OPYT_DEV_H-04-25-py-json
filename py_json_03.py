import json


person = {
    'first_name': 'Pero',
    'last_name': 'Peric',
    'phone': [
        '+385 9_ 1234 567',
        '+385 0_ 1234 567'
    ],
    'email': 'pero@email.hr',
    'address': {
        'street': 'Ulica 123',
        'postal_code': '10290',
        'city': "Zapresic",
        'country': 'Hrvatska'
    },
    'age': 35
}

try:
    with open('person.json', 'w') as file_writer:
        json.dump(person, file_writer, indent=4)
    
except Exception as ex:
    print(f'Dogodila se greska: {ex}')
