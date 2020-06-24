import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import db.db
import welcome
win = tk.Tk()
win.configure(bg="#D6EAF8")

#making the window to be in the middle of screen
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
x=int(width/2-300/2)
y=int(height/2-100/2)
str1="300x300+"+str(x)+"+"+str(y)
win.geometry(str1)
win.resizable(height=False,width=False)

win.title("Electricity Billing")
unit=0

def show():
    meter=int(meter_no.get())
    month=int(combo.current()+1)
    year=int(combo1.get())
    if meter=="":
        messagebox.showinfo("Alert!", "Enter meter number")
    elif month=="":
        messagebox.showinfo("Alert!", "select month")
    elif year=="":
        messagebox.showinfo("Alert!", "select year")
    else:
        res=db.db.unit((meter,year,month))
        if res:
            global unit
            unit=float(res)
            bill_unit.set(str(res))
        else:
            messagebox.showinfo("Alert!","NO Record found")
 
#Calculation of Amount
def amount_calc():
    amount = 0
    total = 0

    units = unit
    
    if units < 50 :
        amount = units * 2.60
        surcharge = 25
    elif units <= 100 :
        amount = 130 + ((units - 50) * 3.25)
        surcharge =35
    elif units <= 200 :
        amount = 130 + 162.50 +((units - 100) * 5.26)
        surcharge = 45
    else :
        amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
        surcharge = 75

    total = amount + surcharge
    amt_unit.set(str(total))

def back():
    win.destroy()
    x=welcome.WelcomeWindow()
    x.add_frame()
tk.Label(win , text ="Meter Number" , bg ="#D6EAF8").grid(row=1 , column =1, padx=20,pady=5)
tk.Label(win , text ="Select Month" , bg ="#D6EAF8").grid(row=2 , column =1, padx=20,pady=5)
tk.Label(win , text ="Select Year" , bg ="#D6EAF8").grid(row=3 , column =1, padx=20,pady=5)
tk.Label(win , text = "Units " , bg ="#D6EAF8").grid(row=5 , column = 1, padx=20,pady=5)
tk.Label(win , text = "Amount (Rs.)" , bg ="#D6EAF8").grid(row=6 , column = 1, padx=20,pady=5)


meter_no=tk.Entry(win)
meter_no.grid(row=1 , column=2)

combo = ttk.Combobox(win , values =("January","Feburary","March","April",
     "May","June","July","August","September","October",
     "November","December"),state="readonly")
combo.grid(row = 2 , column = 2)

combo1 =ttk.Combobox(win ,values =(2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,
                                   2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020),state="readonly")
combo1.grid(row = 3 , column = 2)
bill_unit=tk.StringVar()
units_used = tk.Label(win ,textvariable=bill_unit ,bg ="#FFFFFF" ,width = 20 , height =1).grid(row = 5 , column = 2 ,padx=20 , pady=5)
amt_unit=tk.StringVar()
amt = tk.Label(win ,textvariable=amt_unit, bg ="#FFFFFF" ,width = 20 , height =1).grid(row = 6 , column = 2 ,padx=20 , pady=5)


cal_bill= tk.Button(win , text ="CALCULATE BILL" , bg ="#D6EAF8",command=amount_calc).grid(row=7 , column=2,pady = 5)
show_unit = tk.Button(win , text ="Show unit" , bg ="#D6EAF8",command=show).grid(row=4 , column=2,pady = 5)
back = tk.Button(win , text ="Back" , bg ="#D6EAF8",command=back).grid(row=7 , column=1,pady = 5)

win.mainloop()


