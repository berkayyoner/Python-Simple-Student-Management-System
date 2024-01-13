
#-------------------------- Download tkinker, MySQL Connector -------------------------------

from tkinter import *
import loginpage

root=Tk()
root.title('Cobra')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)


loginpage.loginpage(root)
root.mainloop()