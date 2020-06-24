from tkinter import *
from tkinter import messagebox
import db.db
import graph
import admin_console
class Admin_Operation:

    def __init__(self):
        
        #creating constructor
        self.win=Tk()

        #creating canvas
        #self.canvas=Canvas(self.win,bg='white')
        #self.canvas.pack(expand=YES,fill=BOTH)

        #making window in middle
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-700/2)
        y=int(height/2-500/2)
        str1="600x400+"+str(x)+"+"+str(y)
        self.win.geometry(str1)
        self.win.resizable(0,0)

        self.win.title("WELCOME | E-BILLING GOVERNING FRAUD DETECTION | UCEM")

        #adding frame
        self.frame=Frame(self.win).pack(expand=YES,fill=BOTH)

    def go(self):
        #getting meter_no
        meterno=self.meterno_entry.get()
        if meterno=="":
            messagebox.showinfo("Alert!","Enter meter number")
        else:
            #check whether meter number is already present or not
            res=db.db.check_meter_no(meterno)
            if res:
                #self.show_form(res)
                self.win.destroy()
                graph.mclass().p(res)
            else:
                messagebox.showinfo("Alert!","No data found")


    def cancel(self):
        self.win.destroy()
        admin_console.Admin_Console().add_frame()
        


    def hotspot_frame(self):
       
        #creating add customer form
        self.label=Label(self.frame,text="HOTSPOT CUSTOMER",font="halvetica 32 underline bold italic")
        self.label.place(x=100,y=10)
        self.meterno=Label(self.frame,text="ENTER METER NO.",font="halvetica 14 underline bold italic")
        self.meterno.place(x=10,y=162)
        self.meterno_entry=Entry(self.frame,font="halvetica 22 italic")
        self.meterno_entry.place(x=210,y=162)
        self.meterno=Button(self.frame,text="GO",command=self.go,height=2,width=20,activebackground ="#8EF0F7")
        #go button checks whether meter no is present or not.
        self.meterno.place(x=50,y=300)
        self.meterno=Button(self.frame,text="CANCEL",command=self.cancel,height=2,width=20,activebackground ="#6EF0E6")#code for cancel button
        self.meterno.place(x=400,y=300)

if __name__=='__main__':
    Admin_Operation().hotspot_frame()
