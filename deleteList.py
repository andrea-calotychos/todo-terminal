import argparse
import subprocess
import pandas as pd

parser = argparse.ArgumentParser(description="Porta la riga allo step successivo.")
parser.add_argument('ids', type=int, nargs='+', help='Lista di ID delle righe da modificare')

args = parser.parse_args()
ids = args.ids

df = pd.read_csv('data.csv')


for id in ids:
    df = df[df["id"] != id]

df.to_csv('data.csv', index=False)
subprocess.run(["python", "main.py"])