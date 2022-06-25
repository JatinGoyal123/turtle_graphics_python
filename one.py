from re import T
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Helloo')
root.geometry("640x440")
root.minsize(300,100)
root.maxsize(1200,980)
lab=Label(text="Hi My name is XYZ",bg='red')
lab.pack()
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")
B = Button(root, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(root, text = "Music", variable = CheckVar1, 
                 onvalue = 1, offvalue = 0, height=5, 
                 width = 20, )
C2 = Checkbutton(root, text = "Video", variable = CheckVar2, 
                 onvalue = 1, offvalue = 0, height=5, 
                 width = 20,)
C1.flash()                
C1.pack()
C2.pack()
f1=Frame(root,bg="grey",borderwidth="4")
f1.pack(side=LEFT,fill="y")
l=Label(f1,text="hlo tkinter")
l.pack()
root.mainloop()
