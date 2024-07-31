import csv
import argparse
from datetime import datetime
import subprocess
import pandas as pd

filename = 'hours.csv'

parser = argparse.ArgumentParser(description='Add a project to the hours list.')
parser.add_argument('project', type=str, help='project name')
parser.add_argument('hours', type=int, help='hours to add/set')
project = parser.parse_args().project
hours = parser.parse_args().hours

if hours is None:
    hours = 0

df = pd.read_csv(filename)

if project:
    old_value = df.loc[df['project'] == project, 'hours']

    if not old_value.empty:
        old_hours = old_value.values[0]
        total_hours = old_hours + hours
        df.loc[df['project'] == project, 'hours'] = total_hours
        df.to_csv(filename, index=False)
        print(f"Added {hours} hours to {project}.")

    else:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            writer = csv.writer(file)
            writer.writerow([project, hours])
            print(f"New project: {project} added.")
    
    subprocess.run(["python", "hours.py"])


