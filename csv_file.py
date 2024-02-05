import csv

list_contacts = [{'last_name': 'Иванов', 'first_name': 'Иван', 'patronymic': 'Иванович', 'phone_number': '123',},
                 {'last_name': 'Петров', 'first_name': 'Иван', 'patronymic': 'Сергеевич', 'phone_number': '555',}]

with open('examle_file.csv', 'w', newline='', encoding='utf-8') as csv_file:
    # fieldnames = ['last_name', 'first_name', 'patronymic', 'phone_number']
    fieldnames = list_contacts[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_contacts)
