import requests
import csv
import matplotlib.pyplot as plt

def import_journals(url1):
    response = requests.get(url1)
    response.raise_for_status()  # Check if the request was successful
    content = response.content.decode('utf-8').splitlines()
    csv_reader = csv.reader(content, delimiter=';')
    headers = next(csv_reader)
    data = [row for row in csv_reader]
    return headers, data

# Funding APC data
Elsevier_vouchers = 26
Wiley_deposit = 3990

# Define URLs
url1 = 'https://raw.githubusercontent.com/gammaro85/2.6assigmnment/b8cf083dad02dbb8f018f2b9e6e655efd94a89ac/journaldata.csv'

# Import data from URLs
headers, journal_data = import_journals(url1)

# Map columns
columns = {header: index for index, header in enumerate(headers)}
print(columns)

# Prompt user to check journal title
journal_title = input("Check journal title: ")
found = False
searched_apc = None
for row in journal_data:
    if row[columns['journal_title']].lower() == journal_title.lower():
        print(f"Journal found: {row}")
        found = True
        publisher = row[columns['publisher']]
        research_area = row[columns['research area']]
        if publisher.lower() == 'elsevier':
            if Elsevier_vouchers > 0:
                print("You can pay APC from national Elsevier license")
            else:
                print("Check Oxygenium program")
        elif publisher.lower() == 'wiley':
            try:
                apc_value = float(row[columns['APC']])
                searched_apc = apc_value
                if Wiley_deposit > apc_value:
                    print("You can pay APC from consortium Wiley license")
                else:
                    print("Check Oxygenium program")
                    # Search for another Wiley title with APC lower than Wiley_deposit and same research area
                    for other_row in journal_data:
                        if other_row[columns['publisher']].lower() == 'wiley' and other_row[columns['research area']].lower() == research_area.lower():
                            try:
                                other_apc_value = float(other_row[columns['APC']])
                                if Wiley_deposit > other_apc_value:
                                    print(f"Another Wiley journal found: {other_row}")
                                    print("You can pay APC from consortium Wiley license")
                                    break
                            except ValueError:
                                continue
            except ValueError:
                print("Invalid APC value in the data.")
        break

if not found:
    print("Journal not found.")

# Plotting the APC values
apc_values = [float(row[columns['APC']]) for row in journal_data if row[columns['APC']].replace('.', '', 1).isdigit()]
journal_titles = [row[columns['journal_title']] for row in journal_data if row[columns['APC']].replace('.', '', 1).isdigit()]

plt.figure(figsize=(10, 5))
bars = plt.bar(journal_titles, apc_values, color='blue')

# Highlight the searched APC
if searched_apc is not None:
    for bar, apc in zip(bars, apc_values):
        if apc == searched_apc:
            bar.set_color('red')

plt.xlabel('Journal Titles')
plt.ylabel('APC Values')
plt.title('APC Values of Journals with Searched APC Highlighted')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()