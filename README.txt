welcome to todo-terminal

you can run the application by running the file 'run.bat'

you must have installed python in your computer

use these terminal commands in the project directory

python -m venv env
pip install -r requirements.txt

available commands
- view: views all tasks in terminal
- add {{message}}: adds a new task into the TODO list replace {{message}} with the description of the task
- up {{id}}: updates the task by id, replace {{id}} with the id of the task you want to upgrade (TODO -> TOTEST, TOTEST -> DONE)
- down {{id}}: downgrades the task by id, replace {{id}} with the id of the task you want to downgrade (TOTEST -> TODO, DONE -> TOTEST)
- del {{id}}: deletes the task by id, replace {{id}} with the id of the task you want to delete
- delList {{ids}}: deletes the task list by id, replace {{id}} with all the ids you want to delete (example delList 1 2 3)