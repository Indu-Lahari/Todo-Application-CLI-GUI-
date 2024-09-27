while True:
    user_action = input("Type add, show/display, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index + 1}.{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'complete':
            number = int(input("Number of the todo i.e; completed: "))
            todos.pop(number - 1)

        case 'exit':
            break

        case _:
            print("Hey, you entered an unknown command")

print("Bye!")