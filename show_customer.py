from tkinter import *
from tkinter import messagebox
import db.db
import admin_console
class Admin_Operation:

    def __init__(self):
        
        #creating constructor
        self.win=Tk()

        #creating canvas
        self.canvas=Canvas(self.win,height=500,width=700,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)

        #making window in middle
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-700/2)
        y=int(height/2-500/2)
        str1="800x500+"+str(x)+"+"+str(y)
        self.win.geometry(str1)
        self.win.resizable(0,0)

        self.win.title("WELCOME | E-BILLING GOVERNING FRAUD DETECTION | UCEM")

        #adding frame
        self.frame=Frame(self.canvas,height=400,width=700)
        self.frame.place(x=50,y=50)


    def go(self):
        #getting meter_no
        meterno=self.meterno_entry.get()
        if meterno=="":
            messagebox.showinfo("Alert!","Enter meter number")
        else:
            #check whether meter number is already present or not
            res=db.db.check_meter_no(meterno)
            if res:
                self.show_form(res)
            else:
                messagebox.showinfo("Sorry!","No Record found")


    def cancel(self):
        self.win.destroy()
        admin_console.Admin_Console().add_frame()

    #def all_customer(self):
        
    def show_frame(self):
       
        #creating add customer form
        self.label=Label(self.canvas,text="SHOW CUSTOMER",font="halvetica 22 underline bold italic",bg="white",fg="red")
        self.label.place(x=10,y=10)

        #creating header of delete customer
        self.meterno=Label(self.frame,text="ENTER METER NO.")
        self.meterno.place(x=5,y=10)
        self.meterno_entry=Entry(self.frame)
        self.meterno_entry.place(x=170,y=10)
        self.meterno=Button(self.frame,text="GO",command=self.go)#go button checks whether meter no is present or not.
        self.meterno.place(x=350,y=10)
        self.meterno=Button(self.frame,text="CANCEL",command=self.cancel)#code for cancel button
        self.meterno.place(x=400,y=10)
        Label(self.frame,text="List of customers :",font="halvetica 15 underline bold").place(x=10,y=80)
        customers=db.db.show_customer()
        b=90
        a=0
        for cust in customers:
            b=b+30
            a=a+1
            Label(self.frame,text=str(a)+'.)',font="halvetica 10 bold").place(x=5,y=b)
            Label(self.frame,text=cust,font="halvetica 10 bold").place(x=30,y=b)


    def show_form(self,data):
        #creating form to delete customer
        self.frame=Frame(self.canvas,height=400,width=700)
        self.frame.place(x=50,y=50)

        
        self.l=Label(self.frame,text="Customer Details",font="halvetica 18 underline bold")
        self.l.place(x=150,y=40)

        self.name=Label(self.frame,text="NAME        : ",font="halvetica 10 bold",width=10)
        self.name.place(x=10,y=80)
        
        self.fname=Label(self.frame,text=data[1],font="halvetica 10 bold")
        self.fname.place(x=100,y=80)

        self.mname=Label(self.frame,text=data[2],font="halvetica 10 bold")
        self.mname.place(x=165,y=80)

        self.lname=Label(self.frame,text=data[3],font="halvetica 10 bold")
        self.lname.place(x=220,y=80)

        self.gender=Label(self.frame,text="GENDER     : ",font="halvetica 10 bold",width=10)
        self.gender.place(x=10,y=120)
        if data[4]=='M':
            gen="Male"
        else:
            gen='Female'
        self.gender=Label(self.frame,text=gen,font="halvetica 10 bold").place(x=100,y=120)

        self.address1=Label(self.frame,text="ADDRESS1 : ",font="halvetica 10 bold",width=10)
        self.address1.place(x=10,y=160)
        self.address1=Label(self.frame,text=data[5],font="halvetica 10 bold")
        self.address1.place(x=100,y=160)
        
        self.address2=Label(self.frame,text="ADDRESS2 :",font="halvetica 10 bold",width=10)
        self.address2.place(x=10,y=200)
        self.address2=Label(self.frame,text=data[6],font="halvetica 10 bold")
        self.address2.place(x=100,y=200)
        
        self.city=Label(self.frame,text="CITY           :",font="halvetica 10 bold",width=10)
        self.city.place(x=10,y=240)
        self.city=Label(self.frame,text=data[7],font="halvetica 10 bold")
        self.city.place(x=100,y=240)
        
        self.state=Label(self.frame,text="STATE      :",font="halvetica 10 bold",width=10)
        self.state.place(x=10,y=280)
        self.state=Label(self.frame,text=data[8],font="halvetica 10 bold")
        self.state.place(x=100,y=280)
        
        self.pin=Label(self.frame,text="PIN           :",font="halvetica 10 bold",width=10)
        self.pin.place(x=10,y=320)
        self.pin=Label(self.frame,text=data[9],font="halvetica 10 bold")
        self.pin.place(x=100,y=320)

        self.delete=Button(self.frame,text="OK",font="halvetica 10 bold",command=self.show)
        self.delete.place(x=300,y=360)
        self.win.mainloop()

    def show(self):
        #billing module will be attached with it
        self.win.destroy()
        admin_console.Admin_Console().add_frame()
        

if __name__=='__main__':
    Admin_Operation().show_frame()

