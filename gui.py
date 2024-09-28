import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type a To-Do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo", key="todo")
box = FreeSimpleGUI.Listbox(values=functions.get_todos(), key="list_of_todos",
                            enable_events=True, size=[35,10])

add_button = FreeSimpleGUI.Button("Add")
edit_button = FreeSimpleGUI.Button("Edit")
complete_button = FreeSimpleGUI.Button("Complete")

window = FreeSimpleGUI.Window('To-Do Application',
                              layout=[[label],
                                      [input_box, add_button],
                                      [box, edit_button]],
                              font=('Helvetica', 10))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['list_of_todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['list_of_todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['list_of_todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case FreeSimpleGUI.WIN_CLOSED:
            break

window.close()