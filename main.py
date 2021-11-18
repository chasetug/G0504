import database

if __name__ == "__main__":

    loop = 1

    # Infinite loop to continuously ask for tasks/edit tasks
    while loop == 1:
        print(database.read_database())

        # Asks the user to select an action
        print('1) Add task  |  2) edit task')
        taskCHOICE = int(input())

        # if statement for if the user chooses to add a task
        if taskCHOICE == 1:

            # asks for the task name and the time due
            taskNAME = input('Enter a task: ')
            dueDATE = database.input_time()

            addTASK = [taskNAME, int(dueDATE.timestamp())]

            # adds the task name (addTASK[0]) and unix timestamp value (addTASK[1]) to the database
            database.add_item(addTASK[0], addTASK[1])

        # if statement for if the user chooses to edit a task
        elif taskCHOICE == 2:

            print('1) Change task name   |   2) Change task due date   |   3) Delete Task   | 4) Return Home')
            editTASK_choice = int(input())

            changeTASK = ''
            editTASK_loop = 0

            while editTASK_loop == 0:

                # if statement for if the user chooses to change task name
                if editTASK_choice == 1:
                    changeTASK = input('Enter the name of a task to change it\'s name: ')
                    newName = input('Enter the new name of the selected task: ')
                    editTASK_loop = database.edit_name(changeTASK, newName)

                    if editTASK_loop == 0:
                        print('Name not found! Please try entering another name!')

                # if statement for if the user chooses to change task due date
                elif editTASK_choice == 2:
                    changeTASK = input('Enter the name of a task to change it\'s due date: ')
                    changeTIME = database.input_time()
                    editTASK_loop = database.edit_time(changeTASK, changeTIME)
                    if editTASK_loop == 0:
                        print('Name not found! Please try entering another name!')

                # if statement for if the user chooses to delete a task
                elif editTASK_choice == 3:
                    # deletes the task that matches the user's input
                    changeTASK = input('Enter the name of a task to delete: ')
                    editTASK_loop = database.del_item(changeTASK)
                    if editTASK_loop == 0:
                        print('Name not found! Please try entering another name!')

                # if statement for if the user chooses to go back to home menu
                elif editTASK_choice == 4:
                    continue

