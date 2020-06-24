import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',passwd='qwerty',database='project')

cursor=con.cursor()

def admin_login(data):
    try:
        cursor.execute("select * from `admin` where `login id`=%s and `password`=%s",data)
        return (cursor.fetchone())
    except:
        return False

def check_meter_no(meterno):
    try:
        q="SELECT * FROM `customer_details` where `meter_no`="+str(meterno)
        cursor.execute(q)
        return (cursor.fetchone())
    except:
        return False

def add_customer(data):
    try:
        add_q="INSERT INTO `project`.`customer_details` (`meter_no`, `fname`, `mname`, `lname`, `gender`, `address1`, `address2`, `city`, `state`, `pin`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(add_q,data)
        q="INSERT INTO `project`.`hotspot` (`meter_no`) VALUES ("+data[0]+")"
        n=cursor.execute(q)
        con.commit()
        return 1
    except:
        return 0

def delete_customer(meterno):
    try:
        del_q="DELETE FROM `project`.`customer_details` WHERE `meter_no` ="+str(meterno)
        del_log="DELETE FROM `data_log` where `mtr_no`="+str(meterno)
        del_hotspot="DELETE FROM `project`.`hotspot` where `meter_no`="+str(meterno)
        cursor.execute(del_hotspot)
        cursor.execute(del_log)
        cursor.execute(del_q)
        con.commit()
        return 1
    except:
        return 0

def show_customer():
    try:
        cursor.execute("select * from `customer_details`")
        return (cursor.fetchall())
    except:
        return False

def update_customer(meterno,data):
    try:
        update_q="UPDATE `project`.`customer_details` SET `fname` = %s, `mname` = %s, `lname` = %s, `gender` = %s, `address1` = %s, `address2` = %s, `city` = %s, `state` = %s, `pin` = %s WHERE `meter_no` ="+str(meterno)
        cursor.execute(update_q,data)
        con.commit()
        return 1
    except:
        return 0

def get_dates(mno):
    try:
        q="SELECT count(mtr_no) FROM project.data_log where mtr_no="+str(mno)
        cursor.execute(q)
        n=cursor.fetchone()[0]
        dates = [i for i in range(n)]
        return dates
    except:
        return False

def get_reading(mno):
    reading=[]
    try:
        q="select `reading` from `data_log` where mtr_no="+str(mno)
        cursor.execute(q)
        l=cursor.fetchall()
        for i in range(len(l)):
            reading.append(l[i][0])
        return reading
    except:
        return False

def unit(data):
    try:
        if data[2]==10 or data[2]==11 or data[2]==12:
            q="SELECT reading FROM project.data_log where mtr_no=%s and date_time like '%s-%s-__';"
        else:
            q=q="SELECT reading FROM project.data_log where mtr_no=%s and date_time like '%s-0%s-__';"
        cursor.execute(q,data)
        n=cursor.fetchall()
        sum=0
        for i in n:
            sum=sum+i[0]
        return sum
    except:
        return False


def add_log(data):
    try:
        q = "INSERT INTO data_log(date_time, mtr_no, reading) VALUES(curdate(),%s,%s)"
        cursor.execute(q,data)
        con.commit()
        return 1
    except:
        return False
