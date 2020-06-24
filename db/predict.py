import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',passwd='qwerty',database='project')

dates=[]
reading=[]

cursor=con.cursor()
cursor.execute("SELECT count(mtr_no) FROM project.data_log where mtr_no=111;")
n=cursor.fetchone()[0]
dates = [i for i in range(n)]
cursor.execute("select `reading` from `data_log` where mtr_no=111")
l=cursor.fetchall()
for i in range(365):
        reading.append(l[i][0])

def predict_prices(dates, reading, x):
    dates = np.array([dates]).reshape(-1,1)#np.reshape(dates,(len(dates),1))
    #array.reshape(1, -1)
    #svr_lin= SVR(kernel = 'linear',C=1e3)
    #svr_poly=SVR(kernel= 'poly', C=1e3,degree = 2)
    svr_rbf= SVR(kernel= 'rbf', C=1e3,gamma=0.1)
    #svr_lin.fit(dates,prices)
    #svr_poly.fit(dates,prices)
    svr_rbf.fit(dates,reading)

    plt.scatter(dates,reading,color='black',label='Data')
    plt.plot(dates,svr_rbf.predict(dates),color='red',label='RBF model')
    #plt.plot(dates,svr_lin.predict(dates),color='green',label='Linear model')
    #plt.plot(dates,svr_poly.predict(dates),color='blue',label='Polynomial model')
    plt.xlabel('Date')
    plt.ylabel('Reading')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()
    return svr_rbf.predict(np.array([x]).reshape(1,1)),#svr_lin.predict(np.array([x]).reshape(1,1)), svr_poly.predict(np.array([x]).reshape(1,1))

#get_data('C:\\Users\\Master-Pc\\Desktop\\a.csv')
predicted_price= predict_prices(dates,reading,366)
#print(predicted_price)
         

                           
