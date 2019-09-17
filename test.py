from Tkinter import *
import Tkinter as tk

root = Tk() 
root.geometry("500x500")

v = IntVar() 
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W) 
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W) 
mainloop() 
