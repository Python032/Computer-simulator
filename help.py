from tkinter import *
from tkinter import ttk

def start(v="v1.6"):
    root = Tk()
    root.title("Update")
    root.geometry("400x300")
    root.resizable(False,False)

    l1 = ttk.Label(root,text="Command "+v,font=("",18))
    t1 = Text(root,font=("",14))
    t1.insert(END,"All update:")
    t1.insert(END,"(1)Higher security")

    l1.pack()
    t1.pack(fill=BOTH)