from tkinter import *
from tkinter import ttk
import start_command

def start():
    start_command.system_start.logon()

def end():
    exit()

root = Tk()
root.title("Run system")
root.geometry("300x100")

l1 = ttk.Label(root,text="The system start app.")
lf1 = ttk.LabelFrame(root,text="Configs")
b1 = ttk.Button(lf1,text="Start system",command=start)
b2 = ttk.Button(lf1,text="Exit",command=end)
l1.pack()
lf1.pack()
b1.pack()
b2.pack()

root.mainloop()