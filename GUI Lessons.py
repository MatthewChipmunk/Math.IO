
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font


def main():
    def verify():
        check = open('sigh', 'r')
        c = check.readlines()
        for i in range(len(c)):
            print(i)

    def Log():
        top = Toplevel()
        Label(top, text='Username').pack()
        Entry(top).pack()
        Label(top, text='Password').pack()
        Entry(top).pack()
        Button(top, text='Submit', command=verify).pack()

    def signup():
        def what():
            messagebox.showinfo('', 'You have successfully signed up. Please log in with your username and password')
            top.destroy()
            check = open('sigh', 'r')
            c = check.readlines()
            file = open('sigh', 'w')
            file.write('Username: ' + x.get() + '\n')
            file.write('Password: ' + p.get() + '\n')
            file.write('email: ' + e.get() + '\n')
            file.write('_______________\n')
            for i in c:
                file.write(i)
            file.close()
            top.destroy()

        top = Toplevel()
        e = StringVar()
        x = StringVar()
        p = StringVar()
        Label(top, text='What do you want your username to be?').pack()
        Entry(top, textvariable=x).pack()
        Label(top, text='What do you want your password to be?').pack()
        Entry(top, textvariable=p).pack()
        Label(top, text='What\'s your email?').pack()
        Entry(top, textvariable=e).pack()
        Button(top, text='Submit', command=what).pack()

    root = Tk()
    root.title('Math.IO')
    f = Font(family='Times', size=30, weight='bold')
    m = Font(family='Times', size=20)
    Label(root, text='Math.IO', font=f).pack()
    Label(root, text='The Math Dictionary').pack()
    Label(root, text='What is Math.IO', font=m).pack()
    Label(root, text='Math.IO is a place where you can learn any methods or formulas quick and easy').pack()
    Button(root, text='JOIN Math.IO TODAY!*', command=signup).pack()
    Label(root, text='*Math.IO is completely free').pack()
    Button(root, text='Already have a account?, click here!', command=Log).pack()

    root.mainloop()


main()
