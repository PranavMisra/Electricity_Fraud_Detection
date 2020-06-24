from tkinter import *
import admin_view
import epoint
class WelcomeWindow:
    
    def __init__(self):
        #Creating constructor
        self.win=Tk()

        #create canvas
        self.canvas=Canvas(self.win,height=400,width=600,bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)

        #making the canvas in the middle of th screen
        width=self.win.winfo_screenwidth()
        height=self.win.winfo_screenheight()
        x=int(width/2-600/2)
        y=int(height/2 - 400/2)
        str1="600x400+"+str(x)+"+"+str(y)
        self.win.geometry(str1)

        #stopping window to get maximized (fixing it)
        self.win.resizable(height=False,width=False)

        self.win.title("WELCOME | E-BILLING GOVERNING FRAUD DETECTION | UCEM")

    def add_frame(self):
        
        #creating frame inside canvas
        self.frame=Frame(self.canvas,height=300, width=500)
        self.frame.place(x=50, y=50)

        x,y=70,20
        
        #adding image which is in images folder
        self.img=PhotoImage(file='images/logo.png')
        self.label=Label(self.frame,image=self.img)
        self.label.place(x=50,y=0)

        #creating welcome window
        self.labeltitle=Label(self.frame,text='"WELCOME"',fg='purple')
        self.labeltitle.config(font=("Courier", 60, 'bold'))
        self.labeltitle.place(x=30,y=100)

        self.button1=Button(self.frame,text='ADMIN VIEW',font=('halevetica',20,'bold'),bg='#dddddd',fg='red',command=self.admin_view)
        self.button1.place(x=10,y=220)

        self.button2=Button(self.frame,text="CUSTOMER VIEW",font=('halvetica',20,'bold'),bg="#e8dfdf",fg="#00bb00",command=self.cust_view)
        self.button2.place(x=230,y=220)

        self.button1=Button(self.frame,text='E-POINT',font=('halevetica',12,'bold'),bg='#aaddee',fg='black',command=self.epoint)
        self.button1.place(x=25,y=180)


        self.win.mainloop()

    def epoint(self):
        #code for e-point button
        self.win.destroy()
        data=epoint.DataLog()
        data.add_frame()

    def admin_view(self):
        #code for admin view button
        self.win.destroy()
        admin=admin_view.AdminLogin()
        admin.add_frame()


    def cust_view(self):
        #code for customer view button
        self.win.destroy()
        import extra


if __name__=='__main__':
    x=WelcomeWindow()
    x.add_frame()
