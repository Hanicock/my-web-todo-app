FILEPATH = "todos.txt"

def get_todos():
    '''
    Takes no args, pulls from a predefined file a list of to-dos.
    File is backend in order to save to-dos the user inputs in the program.
    This function allows to pull from the file.
    :return: todos_local -> Has all of the todos from the to-do text file.
    '''
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def push_todos(todo_args):
    '''
    this function takes one param, which tells what information to write into the to-dos.txt file.
    Allows us to save our information into the backend which is a text file.
    :param todo_args:
    :return: Doesn't return any items.
    '''
    with open('todos.txt', 'w') as file_local:
        file_local.writelines(todo_args)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())

