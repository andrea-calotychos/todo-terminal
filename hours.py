import csv
import argparse

filename = 'hours.csv'

with open(filename, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print()
        print(f"Project: {row['project']}, Hours: {row['hours']}")
