import csv
import argparse
from datetime import datetime
import subprocess

filename = 'data.csv'
id = None  

parser = argparse.ArgumentParser(description='Aggiungi qualcosa da fare alla lista.')
parser.add_argument('message', type=str, help='messaggio')
message = parser.parse_args().message

if message:
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)
        if len(rows) < 1:
            id = 1
        else:
            id = int(rows[-1]["id"]) + 1

if id is not None:  
    date = datetime.now().strftime('%Y-%m-%d')
    new_row = [id, date, "TODO", message]
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(new_row)
        print(f"New file written with ID: {new_row[0]}")
    
    subprocess.run(["python", "main.py"])


