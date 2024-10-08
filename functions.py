def get_todos(filepath='todos.txt'):
    """Read a text file and return a list of
       to-do items.
       :param filepath: filepath of the text file
       :return: list of todos
    """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath='todos.txt'):
    """Opens or creates a text file
       and writes the to-do item list into the text file
       :param filepath: filepath of the text file
       :param todos_arg: list of todos
    """
    with open(filepath,'w') as file:
        file.writelines(todos_arg)