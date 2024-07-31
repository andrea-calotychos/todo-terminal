@echo off
echo Attivando l'ambiente virtuale e mantenendo il terminale aperto...
cd C:\Users\AndreaCalotychos\Desktop\todo app\env\Scripts
call activate
cd ..\..\
doskey view=python main.py
doskey del=python delete.py $*
doskey delList=python deleteList.py $*
doskey up=python update.py $*
doskey down=python downgrade.py $*
doskey add=python add.py $*
cmd /K python main.py
