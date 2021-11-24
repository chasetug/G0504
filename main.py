import database
import tkinter as tk
from tkinter import *

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

    def insert_due_date():
        global year_label, year_entry, month_label, month_entry, day_label, day_entry, hour_label, hour_entry
        global minute_label, minute_entry

        btn_frame.pack_forget()
        add_task_btn.grid_forget()
        edit_task_btn.grid_forget()
        del_task_btn.grid_forget()
        del_all_btn.grid_forget()

        year_label = Label(root, text="Enter Year: ", bg="#AFAFD7")
        year_label.place(x=20, y=315)
        year_entry = tk.Entry(root, width=25, font=('times', 14))
        year_entry.pack(pady=10)

        month_label = Label(root, text="Enter Month: ", bg="#AFAFD7")
        month_label.place(x=20, y=360)
        month_entry = tk.Entry(root, width=25, font=('times', 14))
        month_entry.pack(pady=10)

        day_label = Label(root, text="Enter Day: ", bg="#AFAFD7")
        day_label.place(x=20, y=405)
        day_entry = tk.Entry(root, width=25, font=('times', 14))
        day_entry.pack(pady=10)

        hour_label = Label(root, text="Enter Hour: ", bg="#AFAFD7")
        hour_label.place(x=20, y=450)
        hour_entry = tk.Entry(root, width=25, font=('times', 14))
        hour_entry.pack(pady=10)

        minute_label = Label(root, text="Enter Minute: ", bg="#AFAFD7")
        minute_label.place(x=20, y=495)
        minute_entry = tk.Entry(root, width=25, font=('times', 14))
        minute_entry.pack(pady=10)

    def add_time():
        global task_list

        insert_due_date()
        add_time_btn_frame = tk.Frame(root, width=280, height=5)
        add_time_btn_frame.pack(pady=0)
        confirm_time_btn = tk.Button(add_time_btn_frame, text="Confirm Edit", bg='light green', command=confirm_edit)
        confirm_edit_btn.grid(row=0, column=0)

        task = task_entry.get() + "\n"
        with open("task.txt", 'a') as task_file:
            task_file.write(task)
        task_list.append(task)
        listbox.insert(tk.END, task)


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
        global edit_btn_frame, confirm_edit_btn, cancel_edit_btn, minute_label, minute_entry
        global year_label, year_entry, month_label, month_entry, day_label, day_entry, hour_label, hour_entry

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
        if task in task_list:

            insert_due_date()

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
