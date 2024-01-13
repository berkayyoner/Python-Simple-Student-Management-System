from tkinter import *
import database
import loginpage

def studentpage(root, username):
    def logout():
        frame.destroy()
        loginpage.loginpage(root)

    root = root
    username = username

    connection = database.create_db_connection("localhost", "root", "", "cobra")
    midterm_query = "select Midterm from accounts where Username = '" + username + "'"
    midterm_point = database.read_query_one(connection, midterm_query)
    final_query = "select Final from accounts where Username = '" + username + "'"
    final_point = database.read_query_one(connection, final_query)

    frame = Frame(root, width=770, height=390, bg="white")
    frame.place(x=80, y=50)

    heading = Label(frame, text='Welcome, ' + username, fg='#00b1ad', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=230, y=5)

    midterm_label = Label(frame, text='Midterm', fg='black', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'))
    midterm_label.place(x=40, y=130)
    if midterm_point:
        midterm_point_label = Label(frame, text=str(midterm_point[0]), fg='black', bg='white', font=('Microsoft YaHei UI Light', 20, ))
        midterm_point_label.place(x=40, y=180)
    else:
        midterm_point_label = Label(frame, text='0', fg='black', bg='white', font=('Microsoft YaHei UI Light', 20,))
        midterm_point_label.place(x=40, y=180)

    final_label = Label(frame, text='Final', fg='black', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'))
    final_label.place(x=370, y=130)
    if final_point:
        final_point_label = Label(frame, text=str(final_point[0]), fg='black', bg='white', font=('Microsoft YaHei UI Light', 20, ))
        final_point_label.place(x=370, y=180)
    else:
        final_point_label = Label(frame, text=str(final_point[0]), fg='black', bg='white', font=('Microsoft YaHei UI Light', 20,))
        final_point_label.place(x=370, y=180)

    average_label = Label(frame, text='Average', fg='black', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'))
    average_label.place(x=655, y=130)
    if midterm_point and final_point:
        average_point_label = Label(frame, text=str((40*int(midterm_point[0]/100))+(60*int(final_point[0])/100)), fg='black', bg='white', font=('Microsoft YaHei UI Light', 20,))
        average_point_label.place(x=655, y=180)
    else:
        average_point_label = Label(frame, text='0', fg='black', bg='white', font=('Microsoft YaHei UI Light', 20, ))
        average_point_label.place(x=655, y=180)

    Button(frame, width=39, pady=7, text='Log Out', bg='#00b1ad', fg='white', border=0, command=logout).place(x=240,y=300)

