import requests
import csv

def import_journals(url1):
    response = requests.get(url1)
    response.raise_for_status()  # Check if the request was successful
    content = response.content.decode('utf-8').splitlines()
    csv_reader = csv.reader(content, delimiter=';')
    data = [row for row in csv_reader]
    return data

def import_funds(url2):
    response = requests.get(url2)
    response.raise_for_status()  # Check if the request was successful
    content = response.content.decode('utf-8').splitlines()
    csv_reader = csv.reader(content, delimiter=';')
    data = [row for row in csv_reader]
    return data

# Define URLs
url1 = 'https://raw.githubusercontent.com/gammaro85/2.6assigmnment/b8cf083dad02dbb8f018f2b9e6e655efd94a89ac/journaldata.csv'
url2 = 'https://raw.githubusercontent.com/gammaro85/2.6assigmnment/refs/heads/main/money.csv'

# Import data from URLs
journal_data = import_journals(url1)
fund_data = import_funds(url2)
print(journal_data)
print(fund_data)

# Prompt user to check journal title
journal_title = input("Check journal title: ")
for row in journal_data:
    if row[0] == journal_title:
        print("Journal found")
        print(oxygenium)
        break
else:
    print("Journal not found.")