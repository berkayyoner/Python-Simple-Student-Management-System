from tkinter import *
from tkinter import messagebox
import signuppage
import database
import studentpage
import teacherpage

def loginpage(root):
    connection = database.create_db_connection("localhost", "root", "", "cobra")
    root = root

    def signin():
        username=user.get()
        password=code.get()

        if username!='' and password!='' and username!='Username' and password != 'Password':

            query = "select Password, Version from accounts where Username = '" + username + "'"
            result = database.read_query_one(connection, query)

            if username=='teacher' and password=='123':
                print(f"You have successfully logged in as {username}")
                frame.destroy()
                teacherpage.teacherpage(root, username)
            elif result and password==result[0]:
                print(f"You have successfully logged in as {username}")
                if str(result[1]) == "Student":
                    studentpage.studentpage(root, username)
                elif str(result[1]) == "Teacher":
                    teacherpage.teacherpage(root, username)
                frame.destroy()

            else:
                messagebox.showerror('Invalid', "Please check if all the informations are correct.")
        else:
            messagebox.showerror('Invalid', "Please fill all of the informations")
        

    def signup():
        frame.destroy()
        signuppage.signuppage(root)

    frame=Frame(root,width=350,height=350,bg="white")
    frame.place(x=300,y=70)

    heading=Label(frame,text='Sign in',fg='#00b1ad',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
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

    Button(frame,width=39,pady=7,text='Sign in',bg='#00b1ad',fg='white',border=0,command=signin).place(x=35,y=204)
    label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=75,y=270)

    sign_up = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#00b1ad',command=signup)
    sign_up.place(x=215,y=270)