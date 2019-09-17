import Tkinter
import tkMessageBox


top = Tkinter.Tk()

top.geometry("500x500")
def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()

top.mainloop()
