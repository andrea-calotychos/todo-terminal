- WELCOME TO todo-terminal

this is a very simple python application that I'm using to save and keep track of current tasks I need to solve.
I will update this repository whenever I'll need new stuff to add


- HOW TO RUN

you must have installed python in your computer
you can run the application by running the file 'run.bat'

- AVAILABLE COMMANDS

 - view: views all tasks in terminal
 - add {{message}}: adds a new task into the TODO list replace {{message}} with the description of the task
 - up {{id}}: updates the task by id, replace {{id}} with the id of the task you want to upgrade (TODO -> TOTEST, TOTEST -> DONE)
 - down {{id}}: downgrades the task by id, replace {{id}} with the id of the task you want to downgrade (TOTEST -> TODO, DONE -> TOTEST)
 - del {{id}}: deletes the task by id, replace {{id}} with the id of the task you want to delete
 - delList {{ids}}: deletes the task list by id, replace {{id}} with all the ids you want to delete (example delList 1 2 3)