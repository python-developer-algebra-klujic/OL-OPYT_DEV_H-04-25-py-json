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
print(person)

person_json = json.dumps(person)
print(person_json)

person_json = json.dumps(person, indent=4)
print(person_json)
