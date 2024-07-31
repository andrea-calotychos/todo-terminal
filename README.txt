WELCOME TO todo-terminal

This is a very simple Python application that I use to save and keep track of current tasks. I will update this repository whenever I need to add new features.



HOW TO RUN

You must have Python installed on your computer. You can run the application by executing the shortcut todo-terminal.bat or directly the file run.bat



AVAILABLE COMMANDS

view: Views all tasks in the terminal.
add {{message}}: Adds a new task to the TODO list. Replace {{message}} with the description of the task.
up {{id}}: Updates the task by ID. Replace {{id}} with the ID of the task you want to upgrade (e.g., TODO -> TOTEST, TOTEST -> DONE).
down {{id}}: Downgrades the task by ID. Replace {{id}} with the ID of the task you want to downgrade (e.g., TOTEST -> TODO, DONE -> TOTEST).
del {{id}}: Deletes the task by ID. Replace {{id}} with the ID of the task you want to delete.
delList {{ids}}: Deletes multiple tasks by ID. Replace {{ids}} with all the IDs you want to delete (e.g., delList 1 2 3).



HOW IT WORKS

The application reads a CSV file (data.csv) and performs operations (read, update, delete) based on the command given.