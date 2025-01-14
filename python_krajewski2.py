import requests
import csv
import matplotlib.pyplot as plt

def import_journals(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    content = response.content.decode('utf-8-sig').splitlines()  # Use 'utf-8-sig' to handle BOM
    csv_reader = csv.reader(content, delimiter=';')
    headers = next(csv_reader)
    data = [row for row in csv_reader]
    return headers, data

def main():
    # Funding APC data
    Elsevier_vouchers = 26
    Wiley_deposit = 3990
    url = 'https://raw.githubusercontent.com/gammaro85/2.6assigmnment/b8cf083dad02dbb8f018f2b9e6e655efd94a89ac/journaldata.csv'
    
    # Import data from URLs
    headers, journal_data = import_journals(url)

    # Map columns
    columns = {header.strip().lower(): index for index, header in enumerate(headers)}
    # print("Headers:", headers)
    # print("Columns mapping:", columns)

    # Prompt user to check journal title
    journal_title = input("Check journal title: ").strip().lower()
    found = False
    searched_apc = None
    for row in journal_data:
        if row[columns['journaltitle']].strip().lower() == journal_title:
            print("Title is on the list")
            found = True
            publisher = row[columns['publisher']].strip().lower()
            research_area = row[columns['research area']].strip().lower()
            if publisher == 'elsevier':
                if Elsevier_vouchers > 0:
                    print("You can pay APC from national Elsevier license")
                else:
                    print("Check Oxygenium program")
                searched_apc = float(row[columns['apc']])  # Set searched_apc for Elsevier
            elif publisher == 'wiley':
                try:
                    apc_value = float(row[columns['apc']])
                    searched_apc = apc_value
                    if Wiley_deposit > apc_value:
                        print("You can pay APC from consortium Wiley license")
                    else:
                        print("Not enough money in the deposit")
                        # Search for another Wiley title with APC lower than Wiley_deposit and same research area
                        for other_row in journal_data:
                            if other_row[columns['publisher']].strip().lower() == 'wiley' and other_row[columns['research area']].strip().lower() == research_area:
                                try:
                                    other_apc_value = float(other_row[columns['apc']])
                                    if Wiley_deposit > other_apc_value:
                                        print(f"Another journal in your research area found: {other_row[columns['journaltitle']]}")
                                        print("You can pay APC in this journal from consortium Wiley license")
                                        break
                                except ValueError:
                                    continue
                except ValueError:
                    print("Invalid APC value in the data.")
            break

    if not found:
        print("Journal not found.")

    # Plotting the APC values
    apc_values = [float(row[columns['apc']]) for row in journal_data if row[columns['apc']].replace('.', '', 1).isdigit()]
    journal_titles = [row[columns['journaltitle']] for row in journal_data if row[columns['apc']].replace('.', '', 1).isdigit()]

    # print("APC Values:", apc_values)
    # print("Journal Titles:", journal_titles)
    # print("Searched APC:", searched_apc)

    plt.figure(figsize=(10, 5))
    bars = plt.bar(journal_titles, apc_values, color='blue')

    # Highlight the searched APC
    if searched_apc is not None:
        for bar, apc in zip(bars, apc_values):
            if apc == searched_apc:
                bar.set_color('red')
                # print(f"Highlighted APC: {apc} for journal: {row[columns['journaltitle']]}")

    plt.xlabel('Journal Titles')
    plt.ylabel('APC Values')
    plt.title('APC Values of Journals with Searched APC Highlighted')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()