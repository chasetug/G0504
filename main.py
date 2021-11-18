import database
import tkinter as tk
from tkinter import *

if __name__ == "__main__":
    task_list = []


    def addTask(*args):
        global task_list
        task = task_entry.get()
        if task:
            with open("task.txt", 'a') as taskfile:
                taskfile.write("\n" + task)
            task_list.append(task)
            listbox.insert(tk.END, task)


    def deleteTask():
        global task_list
        task = listbox.get(tk.ANCHOR)
        if task in task_list:
            task_list.remove(task)
            with open("task.txt", 'w') as taskfile:
                for task in task_list:
                    taskfile.write(task + "\n")
            listbox.delete(tk.ANCHOR)


    def CheckTask():
        global task_list
        task = listbox.get(tk.ANCHOR)
        for item in listbox.curselection():
            sel = item
        if task in task_list:
            listbox.itemconfig(sel, {'bg': 'light green'})


    def UncheckTask():
        global task_list
        task = listbox.get(tk.ANCHOR)
        for item in listbox.curselection():
            sel = item
        if task in task_list:
            listbox.itemconfig(sel, {'bg': 'white'})


    def DelAll():
        listbox.delete(0, END)


    def openTaskFile():
        global task_list
        with open("task.txt", 'r') as taskfile:
            tasks = taskfile.readlines()
        print(tasks)
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(tk.END, task)


    root = tk.Tk()
    root.title("TO DO LIST")
    root.geometry("400x360")
    root.config(bg="#AFAFD7")
    root.resizable(0, 0)
    frame = tk.Frame(root, bd=3, width=300, height=350)
    frame.pack(pady=10)
    listbox = tk.Listbox(frame, font=('arial', 12), width=40, height=12)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
    openTaskFile()
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    #listbox / tasklist
task_entry = tk.Entry(root, width=25, font=('times', 14))
task_entry.pack(pady=10)
task_entry.bind("<Return>", addTask)
btn_frame = tk.Frame(root, width=280, height=5)
btn_frame.pack(pady=0)
add_task_btn = tk.Button(btn_frame, text=" Add Task ", bg='gold', command=addTask)
add_task_btn.grid(row=0, column=0)
del_task_btn = tk.Button(btn_frame, text=" Delete Task ", bg='orange', command=deleteTask)
del_task_btn.grid(row=0, column=3)
check_task_btn = tk.Button(btn_frame, text=" Check Task ", bg='light green', command=CheckTask)
check_task_btn.grid(row=0, column=1)
uncheck_task_btn = tk.Button(btn_frame, text=" UnCheck Task ", bg='white', command=UncheckTask)
uncheck_task_btn.grid(row=0, column=2)
del_all_btn = tk.Button(btn_frame, text="     CLEAR     ", bg='red', command=DelAll)
del_all_btn.grid(row=0, column=4)
root.mainloop()