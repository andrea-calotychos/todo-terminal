import csv
import argparse

# Nome del file CSV
filename = 'data.csv'

# Apri il file CSV
with open(filename, mode='r', newline='', encoding='utf-8') as file:
    # Crea un oggetto DictReader
    csv_reader = csv.DictReader(file)
    todo = []
    totest = []
    done = []
    
    # Leggi e stampa ogni riga del file CSV come dizionario
    for row in csv_reader:
        if row['state'] == 'TODO':
            todo.append(row)
        elif row['state'] == 'TOTEST':
            totest.append(row)
        elif row['state'] == 'DONE':
            done.append(row)

    print("")

    if len(todo) > 0:
        print("TODO")
        print("")
        for row in todo:
            print(f"ID: {row['id']}, Date: {row['date']}, Message: {row['message']}")

        print("_____________________________________________________________________________________________________________")
        print("")

    if len(totest) > 0:
        print("TOTEST")
        print("")

        for row in totest:
            print(f"ID: {row['id']}, Date: {row['date']}, Message: {row['message']}")

        print("_____________________________________________________________________________________________________________")
        print("")

    if len(done) > 0:
        print("DONE")
        print("")
        for row in done:
            print(f"ID: {row['id']}, Date: {row['date']}, Message: {row['message']}")

        print("_____________________________________________________________________________________________________________")

