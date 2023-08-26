import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import os

root = Tk()
root.title("Prototype")
root.geometry("400x400")

master_username_var = StringVar()
master_password_var = StringVar()

# ASKING USERNAME AND PASSWORD
label1= Label(root, text="Username: ")
label1.place(x=10,y=150)
username= Entry(root, width=50, borderwidth=5,textvariable=master_username_var)
username.place(x=80,y=150)

label2= Label(root, text="Password: ")
label2.place(x=10,y=180)
password= Entry(root, width=50, borderwidth=5, textvariable=master_password_var)
password.place(x=80,y=180)

#REGISTER BUTTON
def register_():
    global top
    top = Toplevel()
    top.title("Registration form")
    top.geometry("550x350")

    #CREATING A DATABASE
    usrinfo = sqlite3.connect("userinfo.db")
    #CREATING A CURSOR
    u = usrinfo.cursor()
    #CREATING TABLE
    u.execute("CREATE TABLE IF NOT EXISTS userinfo( FName Text, SName Text,email Text, Phone NUMERIC,usernameText,PasswordText)")

    #COMMITING CHANGES
    usrinfo.commit()

    #CLOSING 
    usrinfo.close()

    def create_acc():

        global usrn
        usrn = u_name.get()

        if usrn=="":
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

        else:
            #CREATING A DATABASE
            acc = sqlite3.connect(f"{usrn}.db")
            #CREATING A CURSOR
            a = acc.cursor()
            #CREATING TABLE
            a.execute(f"CREATE TABLE IF NOT EXISTS passwords( Domain Text, username Text,email Text, password Text, description Text)")

            #COMMITING CHANGES
            acc.commit()

            #CLOSING 
            acc.close()
        
        fname = f_name.get()
        lname = l_name.get()
        mal = email.get()
        phone = ph_num.get()
        new_pass = n_pass.get()

        #CREATING A DATABASE
        usrinfo = sqlite3.connect("userinfo.db")
        #CREATING A CURSOR
        u = usrinfo.cursor()
        u.execute("INSERT INTO userinfo VALUES('"+fname+"','"+lname+"','"+mal+"','"+phone+"','"+usrn+"','"+new_pass+"')")
        messagebox.showinfo("Information","Successfully Inserted!")
        top.destroy()


        usrinfo.commit()
        usrinfo.close()
        
    #ASKING THE INPUTS
    label3 = Label(top, text="First Name: ")
    label3.place(x=70, y=50)
    f_name = Entry(top, width=50, borderwidth=5)
    f_name.place(x=180 ,y=50)
    label4= Label(top, text="Last Name: ")
    label4.place(x=70 ,y=80)
    l_name = Entry(top, width=50, borderwidth=5)
    l_name.place(x=180 ,y=80)
    label5 = Label(top, text="E-mail: ")
    label5.place(x=70,y=110)
    email = Entry(top, width=50, borderwidth=5)
    email.place(x=180 ,y=110)
    label6 = Label(top, text="Ph-Num: ")
    label6.place(x=70,y=140)
    ph_num= Entry(top, width=50, borderwidth=5)
    ph_num.place(x=180,y=140)
    label7= Label(top, text="Username: ")
    label7.place(x=70,y=170)
    u_name= Entry(top, width=50,borderwidth=5)
    u_name.place(x=180, y=170)
    label8= Label(top, text="New Password: ")
    label8.place(x=70,y=200)
    n_pass= Entry(top, width=50,borderwidth=5)
    n_pass.place(x=180, y=200)
    btn3 = Button(top, text="Create Account", command=create_acc)
    btn3.place(x=255,y=250)
        
# LOGIN
def log_in():

    global master_username_var
    global master_password_var
    u = master_username_var.get()
    if not os.path.isfile(f'{u}.db'):
        messagebox.showinfo("Warning!","No Account Found! Create an Account")
        return
    else:
        usrinfo = sqlite3.connect("userinfo.db")
        c = usrinfo.cursor()
        try:
            c.execute(f'''SELECT PasswordText FROM userinfo WHERE usernameText="{u}"''')
            passw = c.fetchall()[0][0]
            if not passw == master_password_var.get():
                messagebox.showinfo("Warning!","Incorrect Username or Password")
                return
        except:
            messagebox.showinfo("Warning!","Incorrect Username or Password")
            return
        usrinfo.commit()
        usrinfo.close()



    bottom = Toplevel()
    bottom.title("Passwords")
    bottom.geometry("500x500")

    #FUNCTION FOR ADDING DATA INTO THE DATABASE
    def push():
        web = website.get()
        mail = email.get()
        usrnm = username.get()
        paswd = password.get()
        descrip = str(clicked.get())

        acc = sqlite3.connect(f"{usrn}.db")
        a = acc.cursor()
        a.execute("INSERT INTO passwords VALUES('"+web+"','"+usrnm+"','"+mail+"','"+paswd+"','"+descrip+"')")
        messagebox.showinfo("Information","Successfully Inserted!")

        acc.commit()
        acc.close()

    #CREATING THE TITLE
    lbltitle = Label(bottom, bd=20, text="Enter Details", bg="white",font=("times new roman", 22, "bold"))
    lbltitle.pack(side=TOP,fill=X)

    #CREATING THE DATA FRAME
    Entryframe = Frame(bottom, bd=12,relief=RIDGE)
    Entryframe.place(x=0,y=90,width=500,height=350)

    #ENTERING DETAILS
    label1 = Label(bottom,text="Website: ", font=("open sans",12))
    label1.place(x=50, y=180)
    website=Entry(bottom, width=50, borderwidth=5)
    website.place(x=150,y=180)

    label2 = Label(bottom,text="E-mail: ", font=("open sans",12))
    label2.place(x=50, y=220)
    email=Entry(bottom, width=50, borderwidth=5)
    email.place(x=150,y=220)

    label3 = Label(bottom,text="Username: ", font=("open sans",12))
    label3.place(x=50, y=260)
    username=Entry(bottom, width=50, borderwidth=5)
    username.place(x=150,y=260)

    label4 = Label(bottom,text="Password: ", font=("open sans",12))
    label4.place(x=50, y=300)
    password=Entry(bottom, width=50, borderwidth=5)
    password.place(x=150,y=300)

    label5 = Label(bottom,text="Description: ", font=("open sans",12))
    label5.place(x=50, y=340)

    #DROPDOWN MENU
    types = ["Social", "Business","Personal", "OTT"]
    clicked = StringVar(bottom)
    clicked.set("Account Type")
    description = tkinter.OptionMenu(bottom, clicked, *types )
    description.place(x=150,y=340)

    #ADD BUTTON
    add_btn = Button(bottom, text="Add",width=18, command= push)
    add_btn.place(x=100, y=385)

    #BUTTON TO GENERATE PASSWORD
    pwd_btn = Button(bottom, text="Generate Password",width=18)
    pwd_btn.place(x=350, y=330)

    #FUNCTION FOR SHOWING DETAILS
    def show_details():
        mid = Toplevel()
        mid.title("Main Data")
        mid.geometry("710x800")

        def update_details():
            pass

        def delete_details():
            pass
        
        lbltitle = Label(mid, bd=20, text="Data Records", bg="white",font=("times new roman", 22, "bold"),padx=270,pady=5)
        lbltitle.grid(row=0,column=0,columnspan= 20)

        #TABLE HEADINGS
        h1 = Label(mid,text="Website", font="time 15 bold")
        h1.grid(row=1,column=0,padx=10,pady=10)

        h2 = Label(mid,text="Email", font="time 15 bold")
        h2.grid(row=1,column=1,padx=10,pady=10)

        h3 = Label(mid,text="Username", font="time 15 bold")
        h3.grid(row=1,column=2,padx=10,pady=10)

        h4 = Label(mid,text="Password", font="time 15 bold")
        h4.grid(row=1,column=3,padx=10,pady=10)

        h5 = Label(mid,text="Description", font="time 15 bold")
        h5.grid(row=1,column=4,padx=10,pady=10)
        
        update_btn = Button(mid, text="Update",command=update_details)
        update_btn.grid(row=1,column=5)
        update_btn = Button(mid, text="Delete",command=delete_details)
        update_btn.grid(row=2,column=5)
        #CONNECTING TO THE DB TO FETCH AND DISPLAY DATA
        acc = sqlite3.connect("passwords.db")
        a = acc.cursor()
        a.execute("SELECT * FROM passwords")

        r = a.fetchall()
        num = 2
        for i in r:
            website = Label(mid, text=i[0], font="time 8 bold")
            website.grid(row=num,column=0,padx=10,pady=10)

            email = Label(mid, text=i[1], font="time 8 bold")
            email.grid(row=num,column=1,padx=10,pady=10)

            username = Label(mid, text=i[2], font="time 8 bold")
            username.grid(row=num,column=2,padx=10,pady=10)

            password = Label(mid, text=i[3], font="time 8 bold")
            password.grid(row=num,column=3,padx=10,pady=10)

            description = Label(mid, text=i[4], font="time 8 bold")
            description.grid(row=num,column=4,padx=10,pady=10)
            
            num = num+1
        acc.commit()
        acc.close()


        mid.mainloop()

    #SHOW DETAILS BUTTON
    show_btn = Button(bottom, text="Show details",width=18, command=show_details)
    show_btn.place(x=250, y=385)

    bottom.mainloop()

btn1 = Button(root, text="Log-In", command=log_in)
btn1.place(x=170,y=212)
btn2 = Button(root, text="Register", command=register_)
btn2.place(x=220,y=212)

root.mainloop()