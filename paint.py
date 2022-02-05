from tkinter import *
from tkinter import ttk

class window():
    def paint():
        def down(event):
            x1,y1 = (event.x,event.y)
            x2,y2 = (event.x,event.y)
            c1.create_oval(x1,y1,x2,y2,fill="black")
        def cls():
            c1.delete("all")
        root = Tk()
        root.title("Paint")
        c1 = Canvas(root,width=640,height=300)
        b1 = ttk.Button(root,text="Delete",command=cls)
        c1.pack(pady=5)
        c1.bind("<B1-Motion>",down)
        b1.pack()
