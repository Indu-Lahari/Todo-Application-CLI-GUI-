import functions
import FreeSimpleGUI
import time

FreeSimpleGUI.theme("GreenTan")

clock = FreeSimpleGUI.Text('', key='clock')

label = FreeSimpleGUI.Text("Type a To-Do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo", key="todo")
box = FreeSimpleGUI.Listbox(values=functions.get_todos(), key="list_of_todos",
                            enable_events=True, size=[45,10])

add_button = FreeSimpleGUI.Button("Add")
edit_button = FreeSimpleGUI.Button("Edit")
complete_button = FreeSimpleGUI.Button("Complete")
exit_button = FreeSimpleGUI.Button("Exit")

window = FreeSimpleGUI.Window('To-Do Application',
                              layout=[[clock],
                                      [label],
                                      [input_box, add_button],
                                      [box, edit_button, complete_button],
                                      [exit_button]],
                              font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['list_of_todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['list_of_todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['list_of_todos'].update(values=todos)
            except IndexError:
                FreeSimpleGUI.popup("Please select an item first!", font=("Helvetica", 10))

        case "Complete":
            try:
                todo_to_complete = values['list_of_todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['list_of_todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                FreeSimpleGUI.popup("Please select an item first!", font=("Helvetica", 10))


        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case FreeSimpleGUI.WIN_CLOSED:
            break

window.close()