from tkinter import *
from tkinter import messagebox
import mysql.connector
import welcome
import db.db
import time
import webbrowser 

class DataLog:
    
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
       
        self.frame=Frame(self.canvas,height=310,width=500)
        self.frame.place(x=50,y=50)
        x,y=70,20

        self.label = Label(self.frame, text="E-POINT")
        self.label.config(font=("Courier", 40, 'bold'))
        self.label.place(x=140, y = y + 10)

        self.emlabel = Label(self.frame, text="Meter No.")
        self.emlabel.config(font=("Courier", 14, 'bold'))
        self.emlabel.place(x=50, y= y + 100)

        self.meter = Entry(self.frame, font='Courier 12')
        self.meter.place(x=200, y= y + 100)

        self.pslabel = Label(self.frame, text="Enter Reading")
        self.pslabel.config(font=("Courier", 14, 'bold'))
        self.pslabel.place(x=50, y=y+130)

        self.reading = Entry(self.frame, font='Courier 12')
        self.reading.place(x=200, y=y+130)

        self.button = Button(self.frame, text="Submit", font='Courier 18 bold',command=self.submit)
                             
        self.button.place(x=60, y=y+180)

        self.button = Button(self.frame, text="Back", font='Courier 18 bold',command=self.back)
                                 
        self.button.place(x=200, y=y+180)

        self.button=Button(self.frame,text='TEXT-FILE',font='Courier 12 bold',command=self.file)
        self.button.place(x=30,y=y+240)

        self.button=Button(self.frame,text='DATABASE',font='Courier 12 bold',command=self.database)
        self.button.place(x=350,y=y+240)

        self.win.mainloop()

    def file(self):
        #displaying text file
        webbrowser.open("file.txt")

    def database(self):
        #displaying database
        webbrowser.open("file.txt")
    
    def back(self):
        #code for back button
        self.win.destroy()
        bk=welcome.WelcomeWindow()
        bk.add_frame()

    def submit(self):
        #getting data in a tuple
        data=(self.meter.get(),
            self.reading.get())
    
        if self.meter.get()=="":
            messagebox.showinfo("Alert!", "Enter Meter No. First")
        elif self.reading.get()=="":
            messagebox.showinfo("Alert!", "Enter Meter Reading")
        else:
            res=db.db.add_log(data)
            if res:
                t = time.strftime("%Y-%m-%d")
                f= open("file.txt", "a+")
                f.write(t+","+str(data[0])+","+str(data[1])+'\n')
                f.close()
                messagebox.showinfo("Alert!", "Data Updated Sucessfully")
            else:
                messagebox.showinfo("Alert!", "something went wrong")

