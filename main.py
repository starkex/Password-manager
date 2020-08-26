import tkinter as tk
from tkinter import ttk
win =tk.Tk()
win.title('Jarvis')

userl = ttk.Label(win,text='Username : ')
userl.grid(row=0,column=0)

userf =ttk.Entry(win,width=20)
userf.grid(row=0,column=1)

passl = ttk.Label(win,text='Password  : ')
passl.grid(row=1,column=0)

passf =ttk.Entry(win,width=20)
passf.grid(row=1,column=1)

sub = ttk.Button(win,text='Submit')
sub.grid(row=4,column=1)

win.mainloop()