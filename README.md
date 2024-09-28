# To-Do List Application (CLI and GUI)

## Project Description
This project is a simple command-line and GUI-based To-Do List application that allows users to manage tasks effectively. Users can add, edit, complete, and display their to-do tasks either through the terminal or a graphical interface. The app saves the tasks in a text file, ensuring persistence across sessions.

### Features:
- **Add Tasks**: Add new tasks to your to-do list.
- **Edit Tasks**: Modify existing tasks.
- **Complete Tasks**: Mark tasks as completed and remove them from the list.
- **Display Tasks**: View all the tasks in a clean format.
- **Graphical Interface**: Intuitive and user-friendly GUI using FreeSimpleGUI.

## Packages Used
- **time**: For fetching and displaying the current date and time.
- **FreeSimpleGUI**: To create the graphical user interface for the to-do application.
- **functions.py**: Custom module for reading and writing tasks from a text file.

## Project Files
### 1. `cli.py`
This file contains the command-line interface for the to-do list application. It allows users to interact with the application using simple commands.

#### What I learned:
- **`import` statements**: How to import modules like `time` and custom functions from `functions.py`.
- **`time.strftime()`**: How to format and display the current date and time.
- **User inputs and stripping strings**: Using `.strip()` to clean user input.
- **List slicing**: Extracting relevant parts of a string (e.g., extracting task names from commands).
- **List operations**: Adding, editing, and removing items from lists.
- **Handling exceptions**: Implementing `try-except` blocks for error handling to deal with invalid user input.

### 2. `functions.py`
This file contains helper functions to interact with the `todos.txt` file. It provides functionality for reading and writing tasks.

#### What I learned:
- **File handling**: Reading from and writing to files using `with open()`.
- **Function parameters**: How to use default arguments for function parameters.
- **Returning values**: Returning lists of tasks from files.

### 3. `gui.py`
This file provides a graphical user interface for the To-Do List application using `FreeSimpleGUI`. The user can add, edit, and complete tasks in a user-friendly way.

#### What I learned:
- **Creating a GUI**: Building interfaces with `FreeSimpleGUI`.
- **GUI widgets**: Working with text inputs, buttons, and list boxes.
- **Event-driven programming**: Using event loops and handling GUI events such as button clicks.
- **Error handling in GUI**: Using `try-except` blocks to handle empty selections in the GUI.
- **Updating GUI elements**: Dynamically updating list boxes and text fields based on user interactions.

## Applications and Future Use Cases
This simple to-do list application can be expanded and used in a variety of future applications:
1. **Task Management**: Integrate this app into a larger task or project management system, with added features like deadlines, priorities, and categories.
2. **Mobile or Web Apps**: Adapt the GUI for mobile or web platforms using frameworks like React or Flutter.
3. **Notification System**: Add a reminder feature to notify users about pending tasks.
4. **Data Persistence**: Switch from file-based storage to a database system like SQLite or MongoDB for more robust task storage.

## Future Enhancements
- **User Authentication**: Allow multiple users to manage their own tasks.
- **Priority and Deadlines**: Add task priority levels and deadlines.
- **Task History**: Keep a history of completed tasks.
- **Sync Across Devices**: Implement cloud sync for accessing tasks on multiple devices.

## Conclusion
This project helped me understand the basics of file handling, working with lists, and handling user input effectively. On the GUI side, I learned how to build interactive and responsive applications. The use of `FreeSimpleGUI` made the process simple yet powerful, and I plan to use it in future projects requiring quick prototyping of graphical interfaces.
