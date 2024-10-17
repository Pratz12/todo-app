# TO DO APP #
from functions import get_todos,write_todos
import time

day_time = time.strftime("%d %b,%Y %I:%M %p")
print(day_time)

while True:

    user_prompt = input("Type Add,Show,Edit,Complete or Exit :")
    user_prompt = user_prompt.strip()                                               # removes spaces --

                                                                 # match case method
    if user_prompt.startswith('Add'):
        todo = user_prompt[4:]


        todos = get_todos()                                                # store with existing list


        todos.append(todo + '\n')

        write_todos(todos)


    elif user_prompt.startswith('Show'):
        todos = get_todos()

        # new_todos = []
        #
        # for item in todos :
        #     new_item = item.strip(\n)
        #     new_todos.append(new_item)
        # new_todos = [item.strip('\n')] for item in todos]                           # to remove extra space in op

        for index,i in enumerate(todos):                                        # prints index
            i = i.strip('\n')                                                      # remmoves \n from op
            row = f"{index +1}.{i}"                                                # to join output
            print(row)

    elif user_prompt.startswith('Edit'):
        try:

            user_edit = int(user_prompt[5:])               # get list index
            user_edit = user_edit - 1                                               # normalize index

            todos = get_todos()


            new_todo = input("Enter new Todo :")
            todos[user_edit] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_prompt.startswith('Complete'):
        try:                                                                        # delete a item
            number = int(user_prompt[9:])
            number = number - 1


            todos = get_todos()

            todos.pop(number)

            write_todos(todos)
        except Exception as e:
            print(f"Error is {e}")
            continue

    elif user_prompt.startswith('Exit'):
        break
                                                                                    # exits loop
    else:
        print("Are kehna kya chahte ho?")

print ("KAL")
