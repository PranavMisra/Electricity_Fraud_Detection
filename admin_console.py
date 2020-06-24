from tkinter import *
from tkinter import messagebox
import welcome
import add_customer
import update_customer
import delete_customer
import hotspot_customer
import show_customer

class Admin_Console:

    def __init__(self):
        #creating constructor

        self.win=Tk()

        #creating canvas
        self.canvas=Canvas(self.win,height=300,width=500,bg='#82eedd')
        self.canvas.pack(expand=YES,fill=BOTH)

        self.label=Label(self.canvas,text="ADMIN CONSOLE",bg='#82eeee',fg='black', font='halevetica 20 underline bold')
        self.label.pack()

        #making the window in middle
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-500/2)
        y=int(height/2-300/2)
        str1="500x300+"+str(x)+"+"+str(y)
        self.win.geometry(str1)

        self.win.resizable(0,0)

        self.win.title("WELCOME | E-BILLING GOVERNING FRAUD DETECTION | UCEM")



    def add_frame(self):
        
        #adding frame
        self.frame=Frame(self.canvas,height=220,bg='#f1e39b', width=400)
        self.frame.place(x=50, y=50)

        #creating admin window
        self.showbutton = Button(self.frame, text=" SHOW CUSTOMER ", font='Courier 15 bold',bg='red',command=self.show)                 
        self.showbutton.place(x=20, y=0)

        self.addbutton = Button(self.frame, text=" ADD CUSTOMER  ", font='Courier 15 bold',bg='yellow',command=self.add)                 
        self.addbutton.place(x=20, y=50)

        self.updatebutton = Button(self.frame, text="UPDATE CUSTOMER", font='Courier 15 bold',bg='cyan',command=self.update)
        self.updatebutton.place(x=20, y=110)

        self.delbutton = Button(self.frame, text="DELETE CUSTOMER", font='Courier 15 bold',bg='magenta',command=self.delete)
        self.delbutton.place(x=20, y=170)

        self.hotspotbutton = Button(self.frame, text="HOTSPOT",height=5,width=10, font='Courier 15 bold',command=self.hotspot)
        self.hotspotbutton.place(x=240, y=70)

        self.logoutbutton = Button(self.frame, text="LOG OUT", font='Courier 15 bold',bg='light green',command=self.logout)
        self.logoutbutton.place(x=280, y=10)

        self.win.mainloop()

    def logout(self):
        #code for logout button
        messagebox.showinfo("ADMIN","       LOGGED OUT        ")
        self.win.destroy()
        bk=welcome.WelcomeWindow()
        bk.add_frame()

    def add(self):
        #code for add customer button
        self.win.destroy()
        add_customer.Admin_Operation().add_frame()

    def update(self):
        #code for add customer button
        self.win.destroy()
        update_customer.Admin_Operation().update_frame()

    def delete(self):
        #code for add customer button
        self.win.destroy()
        delete_customer.Admin_Operation().delete_frame()

    def show(self):
        #code for add customer button
        self.win.destroy()
        show_customer.Admin_Operation().show_frame()

    def hotspot(self):
        #code for add customer button
        self.win.destroy()
        hotspot_customer.Admin_Operation().hotspot_frame()

'''
if __name__=="__main__":
    Admin_Console().add_frame()
'''
