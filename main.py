import tkinter as tk
from tkinter import ttk
win =tk.Tk()
win.title('Jarvis')
win.geometry('400x400')


userl = ttk.Label(win,text='Username : ')
userl.grid(row=0,column=0,sticky=tk.W)
uservar=tk.StringVar()
userf =ttk.Entry(win,width=20,textvariable=uservar)
userf.grid(row=0,column=1)

passl = ttk.Label(win,text='Password  : ')
passl.grid(row=1, column=0, sticky=tk.W)

passvar = tk.StringVar()
passf = ttk.Entry(win, width=20,show='*',textvariable=passvar,border=None)
passf.grid(row=1,column=1)

choice=ttk.Label(win,text='Suggestion')
choice.grid(row=4, column=0, sticky=tk.W)
choicebutton=ttk.Button(win,text='Generate Password')
choicebutton.grid(row=4,column=1)

perv=tk.StringVar()
per = ttk.Radiobutton(win, text='Public', textvariable=perv)
per.grid(row=5,column=1)

def take():
    username=uservar.get()
    password=passvar.get()
    print(f'{username} + ...password is..{password}')

sub = ttk.Button(win,text='Submit', command=take)
sub.grid(row=6,column=1)

win.mainloop()
