todos = []

while True:
    user_action = input("Type add, show, display, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                print(index, '.', item)
        case 'edit':
            number = int(input("Numer of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")