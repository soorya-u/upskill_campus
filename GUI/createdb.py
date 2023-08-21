from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Registration form")
root.geometry("550x350")

def create_acc():
    if u_name.get()=="":
        messagebox.showerror("Warning!", "Enter username")

    elif email.get() == "":
        messagebox.showerror("Warning!", "Enter E-mail")

    elif f_name.get() == "":
        messagebox.showerror("Warning!", "Enter your first name")

    elif l_name.get() == "":
        messagebox.showerror("Warning!", "Enter your last name")

    elif ph_num.get() == "":
        messagebox.showerror("Warning!", "Enter phone number")
    
    elif n_pass.get() == "":
        messagebox.showerror("Warning!", "Enter New Password")

    elif c_pass.get() == "":
        messagebox.showerror("Warning!", "Confirm Password")

    else:
        #CREATING A DATABASE
        acc = sqlite3.connect(u_name.get()+".db")
        #CREATING A CURSOR
        a = acc.cursor()
        #CREATING TABLE
        a.execute("CREATE TABLE passwords( Domain Text, username Text,email Text, password Text, description Text)")

        #COMMITING CHANGES
        acc.commit()
        #CLOSING 
        acc.close()
        
#ASKING THE INPUTS
label3 = Label(root, text="First Name: ")
label3.place(x=70, y=40)
f_name = Entry(root, width=50, borderwidth=5)
f_name.place(x=180 ,y=40)
label4= Label(root, text="Last Name: ")
label4.place(x=70 ,y=70)
l_name = Entry(root, width=50, borderwidth=5)
l_name.place(x=180 ,y=70)
label5 = Label(root, text="E-mail: ")
label5.place(x=70,y=100)
email = Entry(root, width=50, borderwidth=5)
email.place(x=180 ,y=100)
label6 = Label(root, text="Ph-Num: ")
label6.place(x=70,y=130)
ph_num= Entry(root, width=50, borderwidth=5)
ph_num.place(x=180,y=130)
label7= Label(root, text="Username: ")
label7.place(x=70,y=160)
u_name= Entry(root, width=50,borderwidth=5)
u_name.place(x=180, y=160)
label8= Label(root, text="New Password: ")
label8.place(x=70,y=190)
n_pass= Entry(root, width=50,borderwidth=5)
n_pass.place(x=180, y=190)
label9= Label(root, text="Confirm Password: ")
label9.place(x=70,y=220)
c_pass= Entry(root, width=50,borderwidth=5)
c_pass.place(x=180, y=220)
btn3 = Button(root, text="Create Account", command=create_acc)
btn3.place(x=255,y=260)


root.mainloop()