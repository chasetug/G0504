import csv


def read_database():
    with open('database.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        items = {}

        for row in csv_reader:
            items[row[0]] = row[1]

        return items


def add_item(name, timestamp):
    lines = list()
    with open('database.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            lines.append(row)

    lines.append([name, timestamp])

    with open('database.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(lines)


def del_item(name):
    lines = list()
    with open('database.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] != name:
                lines.append(row)

    with open('database.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(lines)


def edit_time(name, new_time):
    lines = list()
    with open('database.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == name:
                row[1] = new_time
            lines.append(row)

    with open('database.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(lines)