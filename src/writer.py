import csv
from src.vars import CSV_FILE, FIELDNAMES, DELIMITER

# creates new csv file
def create_new(name):
    with open(name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=DELIMITER)
        writer.writerow(FIELDNAMES)

def insert_data(dict):
    with open(str(CSV_FILE), mode='a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writerow(dict)
