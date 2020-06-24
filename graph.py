import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import hotspot_customer
import db.db
from sklearn.svm import SVR

class mclass:
    def __init__(self):
        self.window =Tk()
        self.window.attributes('-fullscreen', True)
        
    def plot (self,m_no):
        d=db.db.get_dates(m_no)
        r=db.db.get_reading(m_no)
        dates=d[:-1]
        reading=r[:-1]
        dates = np.reshape(dates,(len(dates),1))
        svr_rbf= SVR(kernel= 'rbf', C=1e3,gamma=0.1)
        svr_rbf.fit(dates,reading)
        fig=Figure(figsize=(7,7))
        plt=fig.add_subplot(111)
        plt.scatter(dates,reading,color='black',label='Data')
        plt.plot(dates,svr_rbf.predict(dates),color='red',label='RBF model')
        plt.set_xlabel('Date')
        plt.set_ylabel('Reading')
        plt.set_title('Support Vector Regression')
        canvas = FigureCanvasTkAgg(fig,self.window)
        canvas.get_tk_widget().place(x=300,y=10)
        canvas.draw()
        return (svr_rbf.predict(np.array([len(d)]).reshape(1,1)),reading[-1])
        
    def cancel(self):
        self.window.destroy()
        hotspot_customer.Admin_Operation().hotspot_frame()

    def p(self,data):
        #creating form to show customer details
        
        self.l=Label(self.window,text="Customer Details",font="halvetica 18 underline bold")
        self.l.place(x=80,y=40)

        self.name=Label(self.window,text="NAME        : ",font="halvetica 10 bold",width=10)
        self.name.place(x=10,y=80)
        
        self.fname=Label(self.window,text=data[1],font="halvetica 10 bold")
        self.fname.place(x=100,y=80)

        self.mname=Label(self.window,text=data[2],font="halvetica 10 bold")
        self.mname.place(x=165,y=80)

        self.lname=Label(self.window,text=data[3],font="halvetica 10 bold")
        self.lname.place(x=220,y=80)

        self.gender=Label(self.window,text="GENDER     : ",font="halvetica 10 bold",width=10)
        self.gender.place(x=10,y=120)
        if data[4]=='M':
            gen="Male"
        else:
            gen='Female'
        self.gender=Label(self.window,text=gen,font="halvetica 10 bold").place(x=100,y=120)

        self.address1=Label(self.window,text="ADDRESS1 : ",font="halvetica 10 bold",width=10)
        self.address1.place(x=10,y=160)
        self.address1=Label(self.window,text=data[5],font="halvetica 10 bold")
        self.address1.place(x=100,y=160)
        
        self.address2=Label(self.window,text="ADDRESS2 :",font="halvetica 10 bold",width=10)
        self.address2.place(x=10,y=200)
        self.address2=Label(self.window,text=data[6],font="halvetica 10 bold")
        self.address2.place(x=100,y=200)
        
        self.city=Label(self.window,text="CITY           :",font="halvetica 10 bold",width=10)
        self.city.place(x=10,y=240)
        self.city=Label(self.window,text=data[7],font="halvetica 10 bold")
        self.city.place(x=100,y=240)
        
        self.state=Label(self.window,text="STATE      :",font="halvetica 10 bold",width=10)
        self.state.place(x=10,y=280)
        self.state=Label(self.window,text=data[8],font="halvetica 10 bold")
        self.state.place(x=100,y=280)
        
        self.pin=Label(self.window,text="PIN           :",font="halvetica 10 bold",width=10)
        self.pin.place(x=10,y=320)
        self.pin=Label(self.window,text=data[9],font="halvetica 10 bold")
        self.pin.place(x=100,y=320)

        self.back=Button(self.window,text="BACK",font="halvetica 10 bold",command=self.cancel)
        self.back.place(x=100,y=380)
        res=self.plot(data[0])
        self.result(res)
    def result(self,res):
        if res[0]<0:
            r=res[0]*-1
        else:
            r=res[0]
        if r[0]<res[1]:
            clr="green"
            per=round(((res[1]-r[0])/res[1])*100,2)
        else:
            clr="red"
            per=round(((r[0]-res[1])/r[0])*100,2)
        self.canvas=Canvas(self.window,height=1000)
        self.canvas.place(x=1000,y=10)
        Label(self.canvas,text="Result Details",font="halvetica 18 underline bold").place(x=10,y=10)
        Label(self.canvas,text="Present day predected value:",font="halvetica 12").place(x=10,y=60)
        self.f=Label(self.canvas,text=r,font="halvetica 10")
        self.f.place(x=15,y=85)
        Label(self.canvas,text="Original value",font="halvetica 12").place(x=10,y=110)
        self.v=Label(self.canvas,text=res[1],font="halvetica 10")
        self.v.place(x=15,y=135)
            
        self.canvas.create_oval(150,150,300,300,fill="blue")
        self.canvas.create_oval(170,170,280,280,fill=clr)
        Label(self.canvas,text=str(per)+"%",font="halvetica 24 bold", bg=clr,fg="white").place(x=198,y=210)


        self.window.mainloop()
'''        
if __name__=="__main__":
    mclass().plot(111)
'''
