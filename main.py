import tkinter as tk
from tkinter import ttk
win =tk.Tk()
win.title('Jarvis')
win.geometry('400x400')
style=Style()
style.configure('Tbut')

userl = ttk.Label(win,text='Username : ')
userl.grid(row=0,column=0)
uservar=tk.StringVar()
userf =ttk.Entry(win,width=20,textvariable=uservar)
userf.grid(row=0,column=1)

passl = ttk.Label(win,text='Password  : ')
passl.grid(row=1,column=0)

passvar = tk.StringVar()
passf = ttk.Entry(win, width=20, textvariable=passvar)
passf.grid(row=1,column=1)

choice=ttk.Label(win,text='Suggestion')
choice.grid(row=4,column=0)
choicebutton=ttk.Button(win,text='Generate Password')
choicebutton.grid(row=4,column=1)

per=ttk.Radiobutton(win,text='Public')
per.grid(row=5,column=1)

sub = ttk.Button(win,text='Submit')
sub.grid(row=6,column=1)

win.mainloop()
