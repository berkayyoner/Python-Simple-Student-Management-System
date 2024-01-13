from tkinter import *
from tkinter import messagebox
import loginpage
import database

def signuppage(root):
    connection = database.create_db_connection("localhost", "root", "", "cobra")

    root = root
    def signup():
        username=user.get()
        password=code.get()
        password_again=again.get()

        if username != "" and password != "" and password_again != "" and username != "Username" and password != "Password" and password_again != "Password Again":
            if password == password_again:
                try:
                    if var.get() == 0:
                        query = "insert into accounts (Username, Password, Version) values ('" + username + "','" + password + "','Student')"
                        database.execute_query(connection, query)
                        messagebox.showinfo('Sign up', 'Successfully signed up as student.')
                        signin()
                    elif var.get() == 1:
                        query = "insert into accounts (Username, Password, Version) values ('" + username + "','" + password + "','Teacher')"
                        database.execute_query(connection, query)
                        messagebox.showinfo('Sign up', 'Successfully signed up as teacher.')
                        signin()

                except:
                    print("An error occurred while trying to sign up")

            else:
                messagebox.showerror('Invalid',"Both password should match")
        else:
            messagebox.showerror('Invalid', "Please fill all of the informations")

    def signin():
        frame.destroy()
        loginpage.loginpage(root)

    frame=Frame(root,width=350,height=450,bg="white")
    frame.place(x=312,y=40)

    heading=Label(frame,text='Sign up',fg='#00b1ad',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)

    #-----------------------Username Entry-------------------------

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')

    user = Entry(frame, width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,"Username")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    #--------------------------------------------------------------

    #-----------------------Password Entry-------------------------

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')

    code = Entry(frame, width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,"Password")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    #--------------------------------------------------------------

    # -------------------Password Again Entry----------------------

    def on_enter(e):
        again.delete(0, 'end')

    def on_leave(e):
        name = again.get()
        if name == '':
            again.insert(0, 'Password Again')

    again = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    again.place(x=30, y=220)
    again.insert(0, "Password Again")
    again.bind('<FocusIn>', on_enter)
    again.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)
    # --------------------------------------------------------------

    # -------------------Radio Buttons----------------------

    var = IntVar()
    radio1 = Radiobutton(frame, text='Student', bg='white', variable=var, value=0, font=('Microsoft YaHei UI Light', 11))
    radio1.place(x=30,y=270)
    radio2 = Radiobutton(frame, text='Teacher', bg='white', variable=var, value=1, font=('Microsoft YaHei UI Light', 11))
    radio2.place(x=120, y=270)

    # --------------------------------------------------------------

    Button(frame,width=39,pady=7,text='Sign up',bg='#00b1ad',fg='white',border=0,command=signup).place(x=35,y=314)
    label=Label(frame,text="Alredy have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=75,y=380)

    sign_up = Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#00b1ad',command=signin)
    sign_up.place(x=215,y=380)