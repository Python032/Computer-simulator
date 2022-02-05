from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename

def run():
    def save():
        global filename
        textContent = t1.get("1.0",END)
        filename = asksaveasfilename(defaultextension=".th")
        if filename == "":
            return
        output = open(filename,"w")
        output.write(textContent)
        output.close()
    def open():
        global filename
        filename = askopenfilename()
        if askopenfilename == "":
            return
        with open(filename,"r") as fileObj:
            content = fileObj.read()
            fileObj.close()
    def new():
        t1.delete("1.0",END)
    root = Tk()
    root.title("TXT阅读器 1.0")
    menubar = Menu(root)
    filemenu = Menu(menubar,tearoff=False)
    menubar.add_command(label="保存",command=save)
    menubar.add_command(label="打开",command=open)
    menubar.add_command(label="新建",command=new)
    xbar = Scrollbar(root,orient=HORIZONTAL)
    ybar = Scrollbar(root)
    t1 = Text(root)
    xbar.pack(side=BOTTOM,fill=X)
    ybar.pack(side=RIGHT,fill=Y)
    xbar.config(command=t1.xview)
    ybar.config(command=t1.yview)
    t1.config(yscrollcommand=ybar.set)
    t1.config(xscrollcommand=xbar.set)
    t1.pack(fill=BOTH,expand=True)

    root.config(menu=menubar)
    root.mainloop()
