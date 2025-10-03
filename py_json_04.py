import json


contact = '''
    {
        "first_name": "Pero",
        "last_name": "Peric",
        "phone": [
            "+385 9_ 1234 567",
            "+385 0_ 1234 567"
        ],
        "email": "pero@email.hr",
        "address": {
            "street": "Ulica 123",
            "postal_code": "10290",
            "city": "Zapresic",
            "country": "Hrvatska"
        },
        "age": 35
    }
'''

contact_from_str = json.loads(contact)
print(contact_from_str)
print(contact_from_str['phone'][0])
