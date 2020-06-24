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
        str1="700x500+"+str(x)+"+"+str(y)
        self.win.geometry(str1)
        self.win.resizable(0,0)

        self.win.title("WELCOME | E-BILLING GOVERNING FRAUD DETECTION | UCEM")

        #adding frame
        self.frame=Frame(self.canvas,height=400,width=600)
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
                self.update_form(res)
            else:
                messagebox.showinfo("Alert!","No data found")


    def cancel(self):
        self.win.destroy()
        admin_console.Admin_Console().add_frame()
        


    def update_frame(self):
       
        #creating add customer form
        
        self.label=Label(self.canvas,text="UPDATE CUSTOMER",font="halvetica 22 underline bold italic",bg="white")
        self.label.place(x=10,y=10)
        self.meterno=Label(self.frame,text="ENTER METER NO. TO ADD")
        self.meterno.place(x=5,y=10)
        self.meterno_entry=Entry(self.frame)
        self.meterno_entry.place(x=170,y=10)
        self.meterno=Button(self.frame,text="GO",command=self.go)#go button checks whether meter no is present or not.
        self.meterno.place(x=350,y=10)
        self.meterno=Button(self.frame,text="CANCEL",command=self.cancel)#code for cancel button
        self.meterno.place(x=400,y=10)



    def update_form(self,data):
        #creating form to add customer
        self.meterno_entry.config(state=DISABLED)
        self.l=Label(self.frame,text="Update Customer Details",font="halvetica 18 underline bold")
        self.l.place(x=150,y=40)

        self.name=Label(self.frame,text="NAME",bg='dark grey',fg='white',font="halvetica 10 bold",width=8)
        self.name.place(x=10,y=80)
        
        self.fname=Entry(self.frame,font="halvetica 10")
        self.fname.insert(0,data[1])
        self.fname.place(x=90,y=80)

        self.mname=Entry(self.frame,font="halvetica 10")
        self.mname.insert(0,data[2])
        self.mname.place(x=250,y=80)

        self.lname=Entry(self.frame,font="halvetica 10")
        self.lname.insert(0,data[3])
        self.lname.place(x=410,y=80)

        self.gender=Label(self.frame,text="GENDER",bg='dark grey',fg='white',font="halvetica 10 bold",width=8)
        self.gender.place(x=10,y=120)
        if data[4]=='M':
            temp=2
        else:
            temp=1
        self.var=IntVar(self.frame,temp)###data[4]
        self.female=Radiobutton(self.frame,text="Female",value=1,variable=self.var).place(x=200,y=120)
        self.male=Radiobutton(self.frame,text="Male",value=2,variable=self.var).place(x=110,y=120) 

        self.address1=Label(self.frame,text="ADDRESS1",bg='dark grey',fg='white',font="halvetica 10 bold",width=8)
        self.address1.place(x=10,y=160)
        self.address1=Entry(self.frame,font="halvetica 10",width=50)
        self.address1.insert(0,data[5])
        self.address1.place(x=90,y=160)
        
        self.address2=Label(self.frame,text="ADDRESS2",bg='dark grey',fg='white',font="halvetica 10 bold",width=8)
        self.address2.place(x=10,y=200)
        self.address2=Entry(self.frame,font="halvetica 10",width=50)
        self.address2.insert(0,data[6])
        self.address2.place(x=90,y=200)
        
        self.city=Label(self.frame,text="CITY",bg='dark grey',fg='white',font="halvetica 10 bold",width=8)
        self.city.place(x=10,y=240)
        self.city=Entry(self.frame,font="halvetica 10")
        self.city.insert(0,data[7])
        self.city.place(x=90,y=240)
        
        self.state=Label(self.frame,text="STATE",bg='dark grey',fg='white',font="halvetica 10 bold",width=8)
        self.state.place(x=10,y=280)
        self.state=Entry(self.frame,font="halvetica 10")
        self.state.insert(0,data[8])
        self.state.place(x=90,y=280)
        
        self.pin=Label(self.frame,text="PIN",bg='dark grey',fg='white',font="halvetica 10 bold",width=8)
        self.pin.place(x=10,y=320)
        self.pin=Entry(self.frame,font="halvetica 10")
        self.pin.insert(0,data[9])
        self.pin.place(x=90,y=320)

        self.update=Button(self.frame,text="UPDATE",font="halvetica 10 bold",command=self.update)
        self.update.place(x=300,y=360)
        self.win.mainloop()

    def update(self):
        if self.var.get()==1:
            gen='F'
        else:
            gen= "M"
        #taking entire form data in tuple
        data=(
            self.fname.get(),
            self.mname.get(),
            self.lname.get(),
            gen,
            self.address1.get(),
            self.address2.get(),
            self.city.get(),
            self.state.get(),
            str(self.pin.get())
            )
        ret=db.db.update_customer(self.meterno_entry.get(),data)
        if ret==1:
            messagebox.showinfo("SUCESS","Record updated")
            self.cancel()#once record is added close the window and go back
        if ret==0:
            messagebox.showinfo("Alert","pin and meter number should be numbers")

        
if __name__=='__main__':
    Admin_Operation().update_frame()
