from tkinter import *
import database
import loginpage

def teacherpage(root, username):
    connection = database.create_db_connection("localhost", "root", "", "cobra")

    def logout():
        frame.destroy()
        loginpage.loginpage(root)

    root = root

    frame = Frame(root, width=770, height=390, bg="white")
    frame.place(x=80, y=50)

    heading = Label(frame, text='Welcome, ' + username, fg='#00b1ad', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=230, y=5)

    student_label = Label(frame, text='Student', fg='black', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'))
    student_label.place(x=20, y=100)
    midterm_label = Label(frame, text='Midterm', fg='black', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'))
    midterm_label.place(x=350, y=100)
    final_label = Label(frame, text='Final', fg='black', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'))
    final_label.place(x=635, y=100)

    version_query = "select Version from accounts"
    verisons_data = database.read_query_all(connection,version_query)
    versions = []
    for vers in verisons_data:
        versions.append(vers)

#--------------------Student Name List-------------------------------------
    student_usernames_query = "select Username from accounts"
    student_usernames = database.read_query_all(connection, student_usernames_query)
    students = []

    for student in student_usernames:
        students.append(student)
    print(students)

    student_name_labels = []
    index1 = 0
    student_name_x = 20
    student_name_y = 130
    for vers in versions:
        if str(vers).removeprefix("('").removesuffix("',)") == "Student":
            student_name_labels.append(Label(frame, text=students[index1], fg='black', bg='white', font=('Microsoft YaHei UI Light', 11)))
            student_name_labels[index1].place(x=student_name_x, y=student_name_y)
            student_name_y = student_name_y + 20
        index1 = index1 + 1

#--------------------Student Midterm List-------------------------------------
    student_midterms_query = "select Midterm from accounts"
    student_midterms = database.read_query_all(connection, student_midterms_query)
    midterms = []
    for midterm in student_midterms:
        midterms.append(midterm)
    print(midterms)

    student_midterm_labels = []
    index2 = 0
    student_midterm_x = 350
    student_midterm_y = 130
    for vers in versions:
        if str(vers).removeprefix("('").removesuffix("',)") == "Student":
            student_midterm_labels.append(Entry(frame, fg='black', bg='white', font=('Microsoft YaHei UI Light', 11)))
            student_midterm_labels[index2].insert(0, midterms[index2])
            student_midterm_labels[index2].place(x=student_midterm_x, y=student_midterm_y)
            student_midterm_y = student_midterm_y + 20
        index2 = index2 + 1


#--------------------Student Final List-------------------------------------
    student_finals_query = "select Final from accounts"
    student_finals = database.read_query_all(connection, student_finals_query)
    finals = []
    for final in student_finals:
        finals.append(final)
    print(finals)

    student_final_labels = []
    index3 = 0
    student_final_x = 635
    student_final_y = 130
    for vers in versions:
        if str(vers).removeprefix("('").removesuffix("',)") == "Student":
            student_final_labels.append(Entry(frame, fg='black', bg='white', font=('Microsoft YaHei UI Light', 11)))
            student_final_labels[index3].insert(0, finals[index3])
            student_final_labels[index3].place(x=student_final_x, y=student_final_y)
            student_final_y = student_final_y + 20
        index3 = index3 + 1

    def save():
        index4 = 0
        for student in students:
            midterm_value = str(student_midterm_labels[index4].get()) if student_midterm_labels[
                                                                             index4].get() is not None else 'NULL'
            final_value = str(student_final_labels[index4].get()) if student_final_labels[
                                                                         index4].get() is not None else 'NULL'
            save_query = "UPDATE accounts SET Midterm = " + midterm_value + ", Final = " + final_value + " WHERE Username = '" + str(students[index4]).removeprefix("('").removesuffix("',)") + "'"
            print(save_query)
            database.execute_query(connection, save_query)
            index4 = index4+1

#----------------------Buttons----------------------
    Button(frame, width=39, pady=7, text='Save', bg='#00b1ad', fg='white', border=0, command=save).place(x=240,y=320)
    Button(frame, width=39, pady=7, text='Log Out', bg='#00b1ad', fg='white', border=0, command=logout).place(x=240,y=360)

