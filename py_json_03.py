import json


contacts = [
    {
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
    },
    {
        'first_name': 'Ana',
        'last_name': 'Anic',
        'phone': [
            '+385 9_ 9876 654',
            '+385 0_ 9876 654'
        ],
        'email': 'ana@email.hr',
        'address': {
            'street': 'Ulica 321',
            'postal_code': '10290',
            'city': "Zapresic",
            'country': 'Hrvatska'
        },
        'age': 25
    }
]

def save_to_json_file(data_to_save, file_name = 'contacts.json', writing_mode = 'w'):
    try:
        with open(file_name, writing_mode) as file_writer:
            json.dump(data_to_save, file_writer, indent=4)
        
    except Exception as ex:
        print(f'Dogodila se greska: {ex}')



save_to_json_file(contacts)


new_contact = {
        'first_name': 'Iva',
        'last_name': 'Ivic',
        'phone': [
            '+385 9_ 6548 123',
            '+385 0_ 6548 123'
        ],
        'email': 'iva@email.hr',
        'address': {
            'street': 'Ulica 987',
            'postal_code': '10290',
            'city': "Zapresic",
            'country': 'Hrvatska'
        },
        'age': 27
    }

contacts.append(new_contact)

save_to_json_file(contacts)
