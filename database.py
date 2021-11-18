import csv
from datetime import datetime, timezone, timedelta


def read_database():
    with open('database.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        items = {}

        for row in csv_reader:
            items[row[0]] = row[1]

        return items


def add_item(name, timestamp):
    lines = list()
    name_found = 0
    with open('database.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == name:
                return 0
            lines.append(row)
            if row[0] == name:
                name_found += 1

    lines.append([name, timestamp])

    with open('database.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, lineterminator="\n")
        csv_writer.writerows(lines)

    return name_found


def del_item(name):
    lines = list()
    name_found = 0
    with open('database.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == name:
                name_found += 1
            else:
                lines.append(row)

    with open('database.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, lineterminator="\n")
        csv_writer.writerows(lines)

    return name_found


def edit_time(name, new_time):
    lines = list()
    name_found = 0
    with open('database.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == name:
                row[1] = new_time
                name_found += 1
            lines.append(row)

    with open('database.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, lineterminator="\n")
        csv_writer.writerows(lines)

    return name_found


def edit_name(name, new_name):
    new_list = list()
    name_found = 0
    with open('database.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == name:
                temp_row = [new_name, row[1]]
                new_list.append(temp_row)
                name_found += 1
            else:
                new_list.append(row)
    with open('database.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, lineterminator="\n")
        csv_writer.writerows(new_list)

    return name_found


def input_time():
    # Asks the user to input the due date
    time_due = []
    print('When is the task due?')
    time_due.append(int(input('Enter the year: ')))
    time_due.append(int(input('Enter the month: ')))
    time_due.append(int(input('Enter the day: ')))
    time_due.append(int(input('Enter the hour: ')))
    time_due.append(int(input('Enter the minute: ')))

    # converts the time entered into the unix timestamp value for the CENTRAL TIME ZONE (Auburn's time zone)
    due_date = datetime(time_due[0], time_due[1], time_due[2], time_due[3], time_due[4], 0,
                        tzinfo=timezone(timedelta(hours=-6)))
    return due_date

