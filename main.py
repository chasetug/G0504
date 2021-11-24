import database
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

    def insert_due_date(task, selection):
        global year_label, year_entry, month_label, month_entry, day_label, day_entry, hour_label, hour_entry
        global minute_label, minute_entry, task_name_label, time_instr_label

        btn_frame.pack_forget()
        add_task_btn.grid_forget()
        edit_task_btn.grid_forget()
        del_task_btn.grid_forget()
        del_all_btn.grid_forget()
        enter_task_label.place_forget()
        task_entry.pack_forget()

        if selection == 'add':
            y_add = 0
            task_name_label = Label(root, text="Task: {}".format(task), bg="#AFAFD7")
            task_name_label.place(x=20, y=259)
            time_instr_label = Label(root, text="Enter the due date!", bg="#AFAFD7")
            time_instr_label.pack(pady=0)
        elif selection == 'edit':
            y_add = 45
            enter_task_label.place(x=20, y=270)
            task_entry.pack(pady=10)
            time_instr_label = Label(root, text="Enter the due date!", bg="#AFAFD7")
            time_instr_label.pack(pady=0)

        year_label = Label(root, text="Enter Year: ", bg="#AFAFD7")
        year_label.place(x=20, y=290+y_add)
        year_entry = tk.Entry(root, width=25, font=('times', 14))
        year_entry.pack(pady=10)

        month_label = Label(root, text="Enter Month: ", bg="#AFAFD7")
        month_label.place(x=20, y=335+y_add)
        month_entry = tk.Entry(root, width=25, font=('times', 14))
        month_entry.pack(pady=10)

        day_label = Label(root, text="Enter Day: ", bg="#AFAFD7")
        day_label.place(x=20, y=380+y_add)
        day_entry = tk.Entry(root, width=25, font=('times', 14))
        day_entry.pack(pady=10)

        hour_label = Label(root, text="Enter Hour: ", bg="#AFAFD7")
        hour_label.place(x=20, y=425+y_add)
        hour_entry = tk.Entry(root, width=25, font=('times', 14))
        hour_entry.pack(pady=10)

        minute_label = Label(root, text="Enter Minute: ", bg="#AFAFD7")
        minute_label.place(x=20, y=470+y_add)
        minute_entry = tk.Entry(root, width=25, font=('times', 14))
        minute_entry.pack(pady=10)

    def add_time():
        global selected_task
        time_due = []
        task_left_due = []

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
        due_time = 'Due: {:%B %d, %Y} @{}{}'.format(due_date, hour_min, time_day)
        due = Label(root, text="{}".format(due_time), bg="#AFAFD7")
        due.place(x=200, y=200)

        task_left_due = [selected_task, due_time]
        with open("task.txt", 'a') as task_file:
            task_file.write(task_left_due[1])
        task_list.append(task_left_due[1])
        listbox.insert(tk.END, task_left_due[1], task_left_due[0])


    def add_task():
        global task_list, selected_task
        task = task_entry.get() + "\n"
        selected_task = task
        add = 'add'

        insert_due_date(task, add)
        add_time_btn_frame = tk.Frame(root, width=280, height=5)
        add_time_btn_frame.pack(pady=0)
        confirm_time_btn = tk.Button(add_time_btn_frame, text="Enter Due Date", bg='light green',
                                     command=add_time)
        confirm_time_btn.grid(row=0, column=0)


    def delete_task():
        global task_list
        task = task_entry.get() + "\n"
        if task in task_list:
            task_list.remove(task)
            open('task.txt', 'w').close()
            with open("task.txt", 'a') as task_file:
                for item in task_list:
                    task_file.write(item)
        listbox.delete(0, END)
        for item in task_list:
            listbox.insert(tk.END, item)


    def confirm_edit():
        global task_list, selected_task
        new_task_name = task_entry.get() + "\n"
        task_list.remove(selected_task)
        task_list.append(new_task_name)
        open('task.txt', 'w').close()
        with open("task.txt", 'a') as task_file:
            for item in task_list:
                task_file.write(item)
        listbox.delete(0, END)
        for item in task_list:
            listbox.insert(tk.END, item)
        cancel_edit()


    def cancel_edit():
        global edit_btn_frame, confirm_edit_btn, cancel_edit_btn, minute_label, minute_entry, task_name_label
        global year_label, year_entry, month_label, month_entry, day_label, day_entry, hour_label, hour_entry
        global time_instr_label

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

        edit_btn_frame.pack_forget()
        confirm_edit_btn.destroy()
        cancel_edit_btn.destroy()

        btn_frame.pack()
        add_task_btn.grid(row=0, column=0)
        edit_task_btn.grid(row=0, column=1)
        del_task_btn.grid(row=0, column=2)
        del_all_btn.grid(row=0, column=3)


    def edit_task():
        global task_list, selected_task, edit_btn_frame, confirm_edit_btn, cancel_edit_btn

        task = task_entry.get() + "\n"
        selected_task = task
        edit = 'edit'

        if task in task_list:
            insert_due_date(task, edit)

            edit_btn_frame = tk.Frame(root, width=280, height=5)
            edit_btn_frame.pack(pady=0)
            confirm_edit_btn = tk.Button(edit_btn_frame, text="Confirm Edit", bg='light green', command=confirm_edit)
            confirm_edit_btn.grid(row=0, column=0)
            cancel_edit_btn = tk.Button(edit_btn_frame, text="Cancel Edit ", bg='red', command=cancel_edit)
            cancel_edit_btn.grid(row=0, column=1)


    def del_all():
        open('task.txt', 'w').close()
        listbox.delete(0, END)


    def open_task_file():
        global task_list
        with open("task.txt", 'r') as task_file:
            tasks = task_file.readlines()
        print(tasks)
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(tk.END, task)


    root = tk.Tk()
    root.title("TO DO LIST")
    root.geometry("500x600")
    root.config(bg="#AFAFD7")
    root.resizable(0, 0)
    frame = tk.Frame(root, bd=3, width=300, height=350)
    frame.pack(pady=10)
    listbox = tk.Listbox(frame, font=('arial', 12), width=40, height=12)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
    open_task_file()
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

# listbox / task list
enter_task_label = Label(root, text="Enter a task name: ", bg="#AFAFD7")
enter_task_label.place(x=20, y=270)
task_entry = tk.Entry(root, width=25, font=('times', 14))
task_entry.pack(pady=10)

btn_frame = tk.Frame(root, width=280, height=5)
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
