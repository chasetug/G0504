from datetime import datetime, timezone, timedelta
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
            timeDUE = []
            addTASK = []
            taskNAME = input('Enter a task: ')
            print('When is the task due?')
            timeDUE.append(int(input('Enter the year: ')))
            timeDUE.append(int(input('Enter the month: ')))
            timeDUE.append(int(input('Enter the day: ')))
            timeDUE.append(int(input('Enter the hour: ')))
            timeDUE.append(int(input('Enter the minute: ')))

            # converts the time entered into the unix timestamp value for the CENTRAL TIME ZONE (Auburn's time zone)
            # I would like to be able to automatically change the timestamp to the user's local time but idk how
            dueDATE = datetime(timeDUE[0], timeDUE[1], timeDUE[2], timeDUE[3], timeDUE[4], 0,
                               tzinfo=timezone(timedelta(hours=6)))
            addTASK.append(taskNAME)
            addTASK.append(int(dueDATE.timestamp()))

            # adds the task name and timezone into the database (NEED DATABASE NAME)
            # databasename(addTASK[0], addTASK[1])
