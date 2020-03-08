import tkinter
from tkinter import *
from tkinter import messagebox
import random
from tkinter.font import Font

root = Tk()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
Calpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
schar = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '\\', '/']
Cho = Calpha + alpha + num + schar


def lenf():
    passw = ''
    try:
        event = int(et.get())
        for i in range(event):
            rnd = random.choice(Cho)
            passw = passw + rnd
        var.set(passw)
        et.delete(0, END)
    except ValueError:
        var.set('''ERROR!! 
        Please enter a numeric value. ''')
        et.delete(0, END)


def about():
    messagebox.showinfo('About', '''This application is designed
to generate strong passwords.''')


def info():
    messagebox.showinfo('Info', 'Version 1.0.0')


def menu():
    menubar = Menu(root)
    helpm = Menu(menubar, tearoff=0)
    helpm.add_command(label="About", command=about)
    helpm.add_command(label='Info', command=info)
    menubar.add_cascade(label='Help', menu=helpm)
    root.config(menu=menubar)


fr = Frame(root, bg='bisque', highlightcolor='peach puff')

fr.pack(side=BOTTOM)

fontStyle = Font(family="Lucida Grande", size=15)

intro = Label(root,
              text="Welcome To Password Generator!!!", bd=8,
              relief=RAISED, bg="PaleGreen3", width=39, height=4, font=Font(family="Comic Sans", size=18))
entlen = Label(fr, text='Enter the length of the password you want: ',
               bg='bisque', width=62, height=2, font=Font(size=12), anchor='s')
et = Entry(fr, justify=CENTER)


B2 = Button(fr,
            text='Quit',
            command=root.quit)
B1 = Button(fr, text='Generate', command=lenf)

var = StringVar()

password = Label(fr, textvariable=var, relief=RAISED, bd=5, bg='gray64', width=60, height=5, wraplength=400)

menu()

intro.pack()
entlen.pack()
et.pack()
B1.pack()
password.pack()
B2.pack()
root.mainloop()
