import tkinter as tk
from tkinter import *
from datetime import datetime, timezone, timedelta

if __name__ == "__main__":
    task_list = []
    selected_task = ''
    edit_btn_frame = ''
    confirm_edit_btn = ''
    cancel_edit_btn = ''
    year_label = ''
    year_entry = ''
    month_label = ''
    month_entry = ''
    day_label = ''
    day_entry = ''
    hour_label = ''
    hour_entry = ''
    minute_label = ''
    minute_entry = ''
    task_name_label = ''
    time_instr_label = ''
    current_action = ''
    add_time_btn_frame = ''
    confirm_time_btn = ''
    edited_task = ''


    def insert_due_date(task):
        global year_label, year_entry, month_label, month_entry, day_label, day_entry, hour_label, hour_entry
        global minute_label, minute_entry, task_name_label, time_instr_label, current_action

        btn_frame.pack_forget()
        add_task_btn.grid_forget()
        edit_task_btn.grid_forget()
        del_task_btn.grid_forget()
        del_all_btn.grid_forget()
        enter_task_label.place_forget()
        task_entry.pack_forget()

        if current_action == 'add':
            y_add = 0
            task_name_label = Label(root, text="Task: {}".format(task), font=('Helvetica bold', 12), bg="pink")
            task_name_label.place(x=30, y=278)
            time_instr_label = Label(root, text="Enter the due date!", font=('Helvetica bold', 12), bg="light blue")
            time_instr_label.pack(pady=0)
        elif current_action == 'edit':
            y_add = 45
            enter_task_label.place(x=30, y=280)
            task_entry.pack(pady=10)
            time_instr_label = Label(root, text="Enter the due date!", font=('Helvetica bold', 12), bg="light blue")
            time_instr_label.pack(pady=0)

        year_label = Label(root, text="Enter Year: ", font=('Helvetica bold', 12), bg="#AFAFD7")
        year_label.place(x=30, y=315+y_add)
        year_entry = tk.Entry(root, width=25, font=('Helvetica bold', 14))
        year_entry.pack(pady=10)

        month_label = Label(root, text="Enter Month: ", font=('Helvetica bold', 12), bg="#AFAFD7")
        month_label.place(x=30, y=360+y_add)
        month_entry = tk.Entry(root, width=25, font=('Helvetica bold', 14))
        month_entry.pack(pady=10)

        day_label = Label(root, text="Enter Day: ", font=('Helvetica bold', 12), bg="#AFAFD7")
        day_label.place(x=30, y=405+y_add)
        day_entry = tk.Entry(root, width=25, font=('Helvetica bold', 14))
        day_entry.pack(pady=10)

        hour_label = Label(root, text="Enter Hour: ", font=('Helvetica bold', 12), bg="#AFAFD7")
        hour_label.place(x=30, y=450+y_add)
        hour_entry = tk.Entry(root, width=25, font=('Helvetica bold', 14))
        hour_entry.pack(pady=10)

        minute_label = Label(root, text="Enter Minute: ", font=('Helvetica bold', 12), bg="#AFAFD7")
        minute_label.place(x=30, y=495+y_add)
        minute_entry = tk.Entry(root, width=25, font=('Helvetica bold', 14))
        minute_entry.pack(pady=10)

    def add_time():
        global selected_task, task_list, current_action
        time_due = []

        if current_action == 'edit':
            selected_task = task_entry.get()
        '''
        due = Label(root, text="{}".format(due_date), bg="#AFAFD7")
        due.place(x=200, y=200)
        '''

        year = year_entry.get()
        time_due.append(int(year))
        month = month_entry.get()
        time_due.append(int(month))
        day = day_entry.get()
        time_due.append(int(day))
        hour = hour_entry.get()
        time_due.append(int(hour))
        minute = minute_entry.get()
        time_due.append(int(minute))

        due_date = datetime(time_due[0], time_due[1], time_due[2], time_due[3], time_due[4], 0,
                            tzinfo=timezone(timedelta(hours=-6)))

        month_due = '{:%B}'.format(due_date)
        hour_due = int('{:%H}'.format(due_date))

        if hour_due >= 12 and hour_due != 24:
            if hour_due != 12:
                hour_due = hour_due - 12
                time_day = 'pm'
            elif hour_due == 12:
                time_day = 'pm'
        elif hour_due == 0 or hour_due == 24:
            hour_due = 12
            time_day = 'am'
        else:
            time_day = 'am'

        hour_min = '{}:{:%M}'.format(hour_due, due_date)
        due_time = '{} {:%d, %Y} @{}{}'.format(month_due[0:3], due_date, hour_min, time_day)

        task_left_due = [selected_task, 'STILL WORKING', due_time]

        if current_action == 'edit':
            delete_task()

        task_list.append(task_left_due)
        with open("task.txt", 'a') as task_file:
            task_file.write(task_left_due[0] + '^&')
            task_file.write(task_left_due[1] + '^&')
            task_file.write(task_left_due[2] + '^&\n')

        listbox_name.insert(tk.END, task_left_due[0])
        listbox_time_rem.insert(tk.END, task_left_due[1])
        listbox_due.insert(tk.END, task_left_due[2])
        cancel_edit()


    def add_task():
        global selected_task, current_action, add_time_btn_frame, confirm_time_btn
        task = task_entry.get()
        selected_task = task
        current_action = 'add'

        insert_due_date(task)
        add_time_btn_frame = tk.Frame(root, width=280, height=5)
        add_time_btn_frame.pack(pady=0)
        confirm_time_btn = tk.Button(add_time_btn_frame, text="Enter", font=('Helvetica bold', 12),
                                     bg='light green', command=add_time)
        confirm_time_btn.grid(row=0, column=0)


    def delete_task():
        global task_list, edited_task, current_action
        if current_action != 'edit':
            task = task_entry.get()
        else:
            current_action == 'delete'
            task = edited_task[0]

        for i in task_list:
            if task == i[0]:
                task_list.remove(i)

        open('task.txt', 'w').close()
        with open("task.txt", 'a') as task_file:
            for item in task_list:
                task_file.write(item[0] + '^&')
                task_file.write(item[1] + '^&')
                task_file.write(item[2] + '^&\n')
        listbox_name.delete(0, END)
        listbox_time_rem.delete(0, END)
        listbox_due.delete(0, END)

        if current_action == 'delete':
            for item in task_list:
                listbox_name.insert(tk.END, item[0])
                listbox_time_rem.insert(tk.END, item[1])
                listbox_due.insert(tk.END, item[2])


    def cancel_edit():
        global edit_btn_frame, confirm_edit_btn, cancel_edit_btn, minute_label, minute_entry, task_name_label
        global year_label, year_entry, month_label, month_entry, day_label, day_entry, hour_label, hour_entry
        global time_instr_label, current_action

        year_label.destroy()
        year_entry.destroy()
        month_label.destroy()
        month_entry.destroy()
        day_label.destroy()
        day_entry.destroy()
        hour_label.destroy()
        hour_entry.destroy()
        minute_label.destroy()
        minute_entry.destroy()
        time_instr_label.destroy()

        if current_action == 'edit':
            edit_btn_frame.pack_forget()
            confirm_edit_btn.destroy()
            cancel_edit_btn.destroy()
        elif current_action == 'add':
            task_name_label.destroy()
            add_time_btn_frame.pack_forget()
            confirm_time_btn.destroy()
            enter_task_label.place(x=30, y=285)
            task_entry.pack(pady=10)

        btn_frame.pack()
        add_task_btn.grid(row=0, column=0)
        edit_task_btn.grid(row=0, column=1)
        del_task_btn.grid(row=0, column=2)
        del_all_btn.grid(row=0, column=3)

        current_action = ''


    def edit_task():
        global task_list, selected_task, edit_btn_frame, confirm_edit_btn, cancel_edit_btn, current_action, edited_task

        task = task_entry.get()
        selected_task = task
        current_action = 'edit'

        for i in task_list:
            if task == i[0]:
                edited_task = i
                insert_due_date(task)
                edit_btn_frame = tk.Frame(root, width=280, height=5)
                edit_btn_frame.pack(pady=0)
                confirm_edit_btn = tk.Button(edit_btn_frame, text="Confirm Edit", bg='light green',
                                             command=add_time)
                confirm_edit_btn.grid(row=0, column=0)
                cancel_edit_btn = tk.Button(edit_btn_frame, text="Cancel Edit ", bg='red', command=cancel_edit)
                cancel_edit_btn.grid(row=0, column=1)


    def del_all():
        open('task.txt', 'w').close()
        listbox_name.delete(0, END)
        listbox_time_rem.delete(0, END)
        listbox_due.delete(0, END)


    def open_task_file():
        global task_list
        with open("task.txt", 'r') as task_file:
            tasks = task_file.readlines()
        print(tasks)
        for task in tasks:
            task_line = task.split('^&')
            task_list.append(task_line)
            listbox_name.insert(tk.END, task_line[0])
            listbox_time_rem.insert(tk.END, task_line[1])
            listbox_due.insert(tk.END, task_line[2])


    root = tk.Tk()
    root.title("TO DO LIST")
    root.geometry("600x650")
    root.config(bg="#AFAFD7")
    root.resizable(0, 0)

    title_label_name = Label(root, text="Task Name", font=('Helvetica bold', 16), bg="#AFAFD7")
    title_label_name.place(x=60, y=0)
    title_label_time_rem = Label(root, text="Time Remaining", font=('Helvetica bold', 16), bg="#AFAFD7")
    title_label_time_rem.pack()
    title_label_due = Label(root, text="Due Date", font=('Helvetica bold', 16), bg="#AFAFD7")
    title_label_due.place(x=440, y=0)

    frame = tk.Frame(root, bd=3, width=300, height=350)
    frame.pack(pady=5)

    listbox_name = tk.Listbox(frame, font=('Helvetica bold', 12), width=20, height=12)
    listbox_name.grid(row=0, column=0)
    listbox_time_rem = tk.Listbox(frame, font=('Helvetica bold', 12), width=20, height=12)
    listbox_time_rem.grid(row=0, column=1)
    listbox_due = tk.Listbox(frame, font=('Helvetica bold', 12), width=20, height=12)
    listbox_due.grid(row=0, column=2)
    open_task_file()

# listbox / task list
enter_task_label = Label(root, text="Enter a task name: ", font=('Helvetica bold', 12), bg="#AFAFD7")
enter_task_label.place(x=30, y=285)
task_entry = tk.Entry(root, width=25, font=('times', 14))
task_entry.pack(pady=10)

btn_frame = tk.Frame(root, width=290, height=20)
btn_frame.pack(pady=0)
add_task_btn = tk.Button(btn_frame, text="  Add Task ", bg='light green', command=add_task)
add_task_btn.grid(row=0, column=0)
edit_task_btn = tk.Button(btn_frame, text=" Edit Task ", bg='orange', command=edit_task)
edit_task_btn.grid(row=0, column=1)
del_task_btn = tk.Button(btn_frame, text="Delete Task", bg='red', command=delete_task)
del_task_btn.grid(row=0, column=2)
del_all_btn = tk.Button(btn_frame, text="   CLEAR   ", bg='white', command=del_all)
del_all_btn.grid(row=0, column=3)

root.mainloop()
