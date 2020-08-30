import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msbox

win =tk.Tk()
win.title('Jarvis')
win.geometry('400x400')

labframe=ttk.LabelFrame(win,text='Passwaord Manager')
labframe.grid(row=0,column=0,padx=100,pady=20)

userl = ttk.Label(labframe, text='Username : ')
userl.grid(row=0, column=0, sticky=tk.W, pady=5)
uservar=tk.StringVar()
userf =ttk.Entry(labframe,width=20,textvariable=uservar)
userf.grid(row=0, column=1, pady=5)
userf.focus()
passl = ttk.Label(labframe,text='Password  : ')
passl.grid(row=1, column=0, sticky=tk.W, pady=5)

passvar = tk.StringVar()
passf = ttk.Entry(labframe, width=20,show='*',textvariable=passvar,border=None)
passf.grid(row=1, column=1, pady=5)


choice=ttk.Label(labframe,text='Suggestion')
choice.grid()
choice.grid(row=4, column=0, sticky=tk.W, pady=5)
choicebutton = ttk.Button(labframe, text='Generate Password', width=20)
choicebutton.grid(row=4, column=1, pady=5)

perl=ttk.Label(labframe,text='Preference')
perv=tk.StringVar()
per1 = ttk.Radiobutton(labframe, text='Public', textvariable=perv)
per1.grid(row=5, column=1, pady=5)

perv = tk.StringVar()
per2 = ttk.Radiobutton(labframe, text='Public', textvariable=perv)
per2.grid(row=5, column=2, pady=5)

combovar=tk.StringVar()
combo=ttk.Combobox(labframe,width=17,textvariable=combovar,state='readonly')
combo['values']=('--Select--','Admin','User','SignUp')
combo.current(0)
combo.grid(row=6, column=1, pady=5)


def take():
    username=uservar.get()
    password=passvar.get()
    print(f'{username} + ...password is..{password}')


def msg():
    msbox.showinfo('Password Successfully Stored !!')

sub = ttk.Button(labframe,text='Submit', command=msg, width=20)
sub.grid(row=7, column=1, pady=5)


     


win.mainloop()
