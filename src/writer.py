import csv
from src.vars import CSV_FILE, FIELDNAMES, DELIMITER

# creates new csv file
def create_new(name):
    with open(name, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=DELIMITER)
        writer.writerow(FIELDNAMES)

def insert_data(dictionary):
    with open(str(CSV_FILE), mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writerow(dictionary)
