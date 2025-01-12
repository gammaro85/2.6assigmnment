import csv
import requests

def import_csv_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    content = response.content.decode('utf-8').splitlines()
    csv_reader = csv.reader(content, delimiter=';')
    data = [row for row in csv_reader]
    return data

url = 'https://raw.githubusercontent.com/gammaro85/2.6assigmnment/main/journaldata.csv'

# Import data from URL
url_data = import_csv_from_url(url)
print(url_data)

# Prompt user to check journal title
journal_title = input("Check journal title: ")
for row in url_data:
    if row[0] == journal_title:
        print("Journal found:", row)
        break
else:
    print("Journal not found.")