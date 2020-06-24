from tkinter import *
from tkinter import messagebox
import welcome
import db.db
import admin_console

class AdminLogin:
    
    def __init__(self):
        #creating constructor
        self.win=Tk()

        #creating canvas
        self.canvas=Canvas(self.win,height=400,width=600,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)

        #making the window to be in the middle of screen
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-600/2)
        y=int(height/2-400/2)
        str1="600x400+"+str(x)+"+"+str(y)
        self.win.geometry(str1)
        self.win.resizable(height=False,width=False)

        self.win.title("WELCOME | E-BILLING GOVERNING FRAUD DETECTION | UCEM")

    def add_frame(self):
        #adding frame in canvas
        self.frame=Frame(self.canvas,height=310,width=500)
        self.frame.place(x=50,y=50)
        x,y=70,20

        #adding image
        self.img=PhotoImage(file='images/login.png')
        self.label=Label(self.frame,image=self.img)
        self.label.place(x=50,y=10)

        #creating login form
        self.label = Label(self.frame, text="User Login")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=140, y = y + 100)

        self.emlabel = Label(self.frame, text="Enter Email")
        self.emlabel.config(font=("Courier", 12, 'bold'))
        self.emlabel.place(x=50, y= y + 180)

        self.email = Entry(self.frame, font='Courier 12')
        self.email.place(x=200, y= y + 180)

        self.pslabel = Label(self.frame, text="Enter Password")
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x=50, y=y+210)

        self.password = Entry(self.frame,show='*', font='Courier 12')
        self.password.place(x=200, y=y+210)

        self.button = Button(self.frame, text="Login", font='Courier 15 bold',command=self.login)
                             
        self.button.place(x=70, y=y+240)

        self.button = Button(self.frame, text="Back", font='Courier 15 bold',command=self.back)
                                 
        self.button.place(x=170, y=y+240)


        self.win.mainloop()

    def back(self):
        #code for back button
        self.win.destroy()
        bk=welcome.WelcomeWindow()
        bk.add_frame()

    def login(self):
        #getting data in a tuple
        data=(
            self.email.get(),
            self.password.get()
            )

        #checking conditions for userid and password
        if self.email.get()=="":
            messagebox.showinfo("Alert!", "Enter Email First")
        elif self.password.get()=="":
            messagebox.showinfo("Alert!", "Enter password")
        else:
            #passing the data into db file and checking from database
            res=db.db.admin_login(data)
            if res:
                messagebox.showinfo("Message","Login Successful")
                self.win.destroy()
                x=admin_console.Admin_Console()
                x.add_frame()
            else:
                messagebox.showinfo("Alert!","wrong username/password")

