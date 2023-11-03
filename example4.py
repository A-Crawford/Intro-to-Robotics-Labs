import csv

name = input("Please enter a name: ")
phone = input("Please enter a phone number: ")
email = input("Please enter an email adddress: ")

with open('names.csv', 'w') as csvfile:
    headers = ['name', 'phone', 'email']
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerow({'name': name, 'phone': phone, 'email': email})

