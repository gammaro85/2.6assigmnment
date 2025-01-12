import csv

def import_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data

file_path = 'https://github.com/gammaro85/2.6assigmnment/blob/main/journaldata.csv'
data = import_csv(file_path)
print(data)