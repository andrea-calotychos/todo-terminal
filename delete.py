import pandas as pd
import argparse
import subprocess

parser = argparse.ArgumentParser(description="Elimina una riga dato l'id.")
parser.add_argument('id', type=int, help='id')
id = parser.parse_args().id


if(id):    
    df = pd.read_csv('data.csv')
    df_filtrato = df[df["id"] != id]
    df_filtrato.to_csv('data.csv', index=False)
    print(f"Riga con id:" + str(id) + " eliminata e file salvato.")
    subprocess.run(["python", "main.py"])

