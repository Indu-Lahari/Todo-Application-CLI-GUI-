import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type a To-Do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo")
add_button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window('To-Do Application',
                              layout=[[label],
                                     [input_box, add_button]])
window.read()

window.close()