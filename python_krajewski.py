import requests
import csv

def import_journals(url1):
    response = requests.get(url1)
    response.raise_for_status()  # Check if the request was successful
    content = response.content.decode('utf-8').splitlines()
    csv_reader = csv.reader(content, delimiter=';')
    data = [row for row in csv_reader]
    return data

#Fundinf APC data
Elsevier_vouchers=26
Wiley_deposit=3990

# Define URLs
url1 = 'https://raw.githubusercontent.com/gammaro85/2.6assigmnment/b8cf083dad02dbb8f018f2b9e6e655efd94a89ac/journaldata.csv'

# Import data from URLs
journal_data = import_journals(url1)

# Prompt user to check journal title
journal_title = input("Check journal title: ")
for row in journal_data:
    if row[0] == journal_title:
        publisher = row[1]  # Assuming publisher is in the second column
        if publisher == 'elsevier':
            if Elsevier_vouchers == 0:
                print("check Oxygenium program")
            else:
                print("You can pay APC from national Elsevier license")
    else:
        print("Journal not found.")