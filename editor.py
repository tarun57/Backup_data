import Tkinter
import tkMessageBox
import ttk

def new_window():
	root = Tkinter.Tk(className='Editor')
	root.mainloo()
	text = Tkinter.Text()
	text.pack(fill=Tkinter.BOTH, expand=1)
	text.config(font="Arial 32")
	text.focus_set()
	text.pack()

root = Tkinter.Tk(className='Editor')

root.title("Text editor")
root.geometry("800x800")
root.configure(background='white')
text = Tkinter.Text()
text.pack(fill=Tkinter.BOTH, expand=1)
text.config(font="Arial 2")
text.focus_set()
text.pack()

def saveas():
    global text	
    t = text.get("1.0", "end-1c")
    savelocation=Tkinter.tkFileDialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

menu = Tkinter.Menu(root) 
root.config(menu=menu) 
filemenu = Tkinter.Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New', command=new_window) 
filemenu.add_command(label='Open...') 
filemenu.add_command(label='Save', command=saveas)
filemenu.add_command(label='Save as')
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
viewmenu = Tkinter.Menu(menu)
menu.add_cascade(label='View', menu=viewmenu) 
viewmenu.add_command(label='cut')
viewmenu.add_command(label='copy')
viewmenu.add_command(label='paste')
viewmenu.add_command(label='Font')

helpmenu = Tkinter.Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 

text.configure(font=("Times New Roman", 12, "bold"))

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

root.mainloop()
