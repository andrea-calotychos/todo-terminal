import pandas as pd
import argparse
import subprocess

# Configura l'argomento della riga di comando
parser = argparse.ArgumentParser(description="porta la riga allo step successivo.")
parser.add_argument('id', type=int, help='id della riga da modificare')
id = parser.parse_args().id

# Leggi il DataFrame dal file CSV
df = pd.read_csv('data.csv')

# Verifica se l'id esiste e modifica l'attributo 'state'
if id in df['id'].values:
    oldState = df.loc[df['id'] == id, 'state'].values[0]

    if(oldState == "TOTEST"):
        newState = "TODO"
    elif(oldState == "DONE"):
        newState = "TOTEST"
    else:
        print("invalid state")

    df.loc[df['id'] == id, 'state'] = newState
    df.to_csv('data.csv', index=False)
    print(f"Attributo 'state' della riga con id {id} modificato in '{newState}' e file salvato.")
    subprocess.run(["python", "main.py"])

else:
    print(f"Nessuna riga trovata con id {id}.")
