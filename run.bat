@echo off
:: Controlla se il file data.csv esiste e, se non esiste, crealo e aggiungi l'intestazione


set "first_run=false"

if not exist "data.csv" (
    echo Primo avvio dell'applicazione, installazione dei pacchetti in corso...
    (
        echo id,date,state,message
    ) > data.csv
    (
        echo project,hours
    ) > hours.csv
    python -m venv env
	set "first_run=true"
)

echo Attivando l'ambiente virtuale e mantenendo il terminale aperto...
cd env\Scripts
call activate
cd ..\..\

if "%first_run%" == "true" (
    pip install pandas
)
doskey view=python main.py
doskey del=python delete.py $*
doskey delList=python deleteList.py $*
doskey up=python update.py $*
doskey down=python downgrade.py $*
doskey add=python add.py $*
doskey hours=python hours.py
doskey addHours=python addHours.py $*
cmd /K python main.py
