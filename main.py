import database

if __name__ == "__main__":

    print(database.read_database())

    loop = 1

    # Infinite loop to continuously ask for tasks/edit tasks
    while loop == 1:
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
            # loops if the user enters an invalid character
            editTASK_loop = 1
            editTASK_choice = 0
            changeTASK = ''
            while editTASK_loop == 1:

                if editTASK_choice == 0:
                    print('1) Change task name   |   2) Change task due date   |   3) Delete Task   | 4) Return Home')
                    editTASK_choice = int(input())

                if editTASK_choice == 1:
                    print('choice 1')
                elif editTASK_choice == 2:
                    print('choice 2')
                elif editTASK_choice == 3:
                    # deletes the task that matches the user's input
                    changeTASK = input('Enter the name of a task to delete: ')
                    database.del_item(changeTASK)

                elif editTASK_choice == 4:
                    continue
                else:
                    print('Invalid entry! Please enter \'1\', \'2\', \'3\', or \'4\'')

        else:
            print('Invalid entry! Please enter \'1\' or \'2\'')
