import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type a To-Do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window('To-Do Application',
                              layout=[[label],
                                      [input_box, add_button]],
                              font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case FreeSimpleGUI.WIN_CLOSED:
            break

window.close()