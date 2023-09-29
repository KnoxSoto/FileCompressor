import functions
# Module Library creating instance
import PySimpleGUI as sg # Importing third-party code (Package)
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
add_button2 = sg.Button("Edit")



window = sg.Window('To-Do App',
                   layout=[[label],[input_box,add_button,add_button2]],
                   font=('Helvetica', 20))
while True:
        event, values = window.read()  # Display the window on the screen
        print(event)
        print(values)
        match event:
            case "Add":
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
            case sg.WIN_CLOSED:  # Allows to close out the program
                break

window.close()


