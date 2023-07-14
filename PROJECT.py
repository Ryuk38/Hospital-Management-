#project class 12 cbse

from emoji import emojize

import mysql.connector

from tabulate import tabulate

from datetime import datetime as dt

string=dt.now()
a=[("TODAYS DATE AND TIME",string)]
print(emojize("\t\t\t\t:hospital:"))

b=[["WELCOME to BSP HOSPITAL,KANNUR"]]
print(tabulate(a,tablefmt="pipe"))
print(tabulate(b,tablefmt="fancy_grid"))

def project():
      
      c="Y"
      c="y"
      while c=="Y" or c=="y":
            mydata=[["CHOOSE OUR SERVICES"],
                    ["1.PATIENT"],
                    ["2.DOCTOR"],
                    ["3.MANAGEMENT"],
                    ["4.PROJECT DATA"],
                    ["5.AMBULANCE SERVICE"],
                    ["6.AMBULANCE_DATA"],
                    ["7.EXIT"]]
            print(tabulate(mydata,tablefmt="jira"))
            
            choice=int(input("ENTER YOUR CHOICE:"))
            if choice== 1:
                  patient()
            elif choice==2:
                  doctor()
            elif choice==3:
                  management()
            elif choice==4:
                  PROJECT_data()
            elif choice==5:
                  ambulance()
            elif choice==6:
                  ambulance_data()
            elif choice==7:
                  print("exiting")
                  print("THANK YOU, SEE YOU AGAIN!!!")
                  print(emojize("\t\t\U0001F600"))
                  break
            else:
                  print("INVALID INPUT")
            c=input("do you wish to continue(y/n):)")
            while c=="n" or c=="N":
                  print("THANK YOU, SEE YOU AGAIN!!!")
                  print(emojize("\t\t\U0001F600"))
                  break

#patient_data
            
def patient():
      a=[["1.BOOK APPOINTMENT" ],["2.CHECK APPOINTMENT DETAILS"]]
      headers=["WHAT WOULD YOU LIKE TO DO"]
      print(tabulate(a,headers,tablefmt="rst"))
      r=int(input(""))
      if r==1:
            
            #TO BOOK APPOINTMENT
            
            x=input("Please enter patient's name in block letters:")
            y=int(input("Enter your age:"))
            v=input("enter your Gender (M/F/RATHER NOT TO SAY):")
            z=input("Enter your Address:")
            print(x," please choose the type of doctor you want to meet...")
            m1=[["1.PEDIATRICS","2.SURGEON","3.CARDIOLOGISTS"],["4.ANESTHESIOLOGISTS","5.DERMATOLOGISTS","6.ENDOCRINOLOGISTS"],["7.FAMILY PHYSICIANS","8.NEUROLOGISTS","9.GYNECOLOGISTS"],["10.OPTHALMOLOGISTS","12.PLASTIC SURGEONS","13.PSYCHIATRISTS"],["14.RADIOLOGISTS","15.GENERAL SURGEONS"]]
            print(tabulate(m1,tablefmt="fancy_grid"))
            u=input("ENTER TYPE OF DOCTOR:")
            mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="doctor")
            mycursor=mydb.cursor()  
            
            if u=="pediatrics" or u=="PEDIATRICS":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='PEDIATRICS'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            if u=="surgeon" or u=="SURGEON":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='SURGEON'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            if u=="CARDIOLOGISTS" or u=="cardiologists":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='CARDIOLOGISTS'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            if u=="anesthesiologists" or u=="ANESTHESIOLOGISTS":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='ANESTHESIOLOGISTS'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            if u=="DERMATOLOGISTS" or u=="dermatologists":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='DERMATOLOGISTS'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            if u=="ENDOCRINOLOGISTS" or u=="endocrinologists":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='ENDOCRINOLOGISTS'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            if u=="FAMILY PHYSICIANS" or u=="family physicians":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='family physicians'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with")
                  
            if u=="NEUROLOGISTS" or u=="neurologists":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='NEUROLOGISTS'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  

            if u=="GYNECOLOGISTS" or u=="gynecologists":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='GYNECOLOGISTS'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            if u=="OPTHALMOLOGISTS" or u=="opthalmologists":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='OPTHALMOLOGISTS'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            
            if u=="PLASTIC SURGEONS" or u=="plastic surgeons":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='plastic surgeons'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            if u=="PSYCHIATRISTS" or u=="psychiatrists":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='psychiatrists'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            if u=="RADIOLOGISTS" or u=="radiologists":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='RADIOLOGISTS'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            if u=="GENERAL SURGEONS" or u=="general surgeons":
                  s="select did,name,department,qualification,timings,days_available from doctor_details where department='general surgeons'"
                  mycursor.execute(s)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=["DID","NAME","DEPARTMENT","QUALIFICATIONS","TIMINGS","DAYS_AVIAILABLE"],tablefmt="grid"))
                  l=input("whom do you want to book appointment with:")
                  
            import random
            x1=random.randint(0,100)
            print("your token no is :",x1)
            mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="patient")
            mycursor=mydb.cursor()
            s="INSERT INTO PATIENT_DETAILS(token_no,name,age,gender,address,DEPARTMENT,visited_doctor,DATE_TIME) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            t=(x1,x,y,v,z,u,l,string)
            mycursor.execute(s,t)
            mydb.commit()
            print("THANK YOU")
         
             
      if r==2:
            
            #TO CHECK APPOINTMENT DETAILS
            
            mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="patient")
            mycursor=mydb.cursor()
            x=(input("ENTER NAME:"))
            c=("SELECT TOKEN_NO,name,AGE,GENDER,ADDRESS,DEPARTMENT FROM PATIENT_DETAILS WHERE NAME=%s")
            t=(x,)
            mycursor.execute(c,t)
            e=mycursor.fetchall()
            print(tabulate(e,headers=['TOKEN_NO','Name','AGE','GENDER','ADDRESS','DEPARTMENT'],tablefmt="grid"))
   
            
                  
#doctor_data
    
def doctor():
      x=(input("ENTER THE PASSWORD:"))
      if x=="123":
            a=[["1.TO SEE PATIENT DETAILS"],["2.TO SEE YOUR DEATILS\n"]]
            headers=["WHAT WOULD YOU LIKE TO DO"]
            print(tabulate(a,headers,tablefmt="rst"))
            y=int(input(""))
            
            if y==1:
                  
                  #TO SEE PATIENT DETAILS
                  
                  a=(input("ENTER YOUR DEPARTMENT:"))
                  mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="patient")
                  mycursor=mydb.cursor()
                  c=("SELECT TOKEN_NO,name,AGE,GENDER,ADDRESS,DEPARTMENT,VISITED_DOCTOR FROM PATIENT_DETAILS WHERE department=%s")
                  t=(a,)
                  mycursor.execute(c,t)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=['TOKEN_NO-','Name-','AGE-','GENDER-','ADDRESS-','DEPARTMENT-','DOCTOR-'],tablefmt="grid"))
                  
            if y==2:
                  
                  #TO SEE SELF DEATILS
                  
                  a=int(input("ENTER YOUR SALARY SLIP NUMBER:"))
                  mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="doctor")
                  mycursor=mydb.cursor()
                  c=("SELECT did,name,age,GENDER,ADDRESS,DEPARTMENT,QUALIFICATION,TIMINGS,DAYS_AVAILABLE,SALARY,SALARYSLIP_NO from doctor_details where salaryslip_no=%s")
                  t=(a,)
                  mycursor.execute(c,t)
                  e=mycursor.fetchall()
                  print(tabulate(e,headers=['DID','NAME','AGE','GENDER','ADDRESS','DEPARTMENT','QUALIFICATIONS','TIMINGS','DAYS AVAILABLE','SALARY','SALARY SLIP NO',],tablefmt="grid"))

      else:
            print("wrong password")
             
                                     
#management
            
def management():
    print("TO ACCESS THIS ENTER PASSWORD")
    x=int(input("ENTER PASSWORD:"))
    if x==1234:
          q=[[" 1.CREATE NEWDATABASE "],[" 2.UPDATE DATA"],["3.DELETE DATA"],[" 4.DISPLAY DATA"],[" 5.ADD DOCTOR DATA"]]
          headers=["WHAT WOULD YOU LIKE TO DO"]
          print(tabulate(q,headers,tablefmt="rst"))
          q=int(input(""))
          if q==1:
                a=int(input("WHOSE DATABASE WOULD YOU LIKE TO CREATE \n 1.PATIENT\n 2.DOCTOR\n 3.AMBULANCE/DRIVER/SERVICE\n"))
                if a==1:
                      
                      # CREATE PATIENT DATABASE
                      
                      import mysql.connector
                      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH")
                      mycursor=mydb.cursor()
                      mycursor.execute("CREATE DATABASE patient")
                      print("DATABASE CREATED SUCCESSFULLY")
                      import mysql.connector
                      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="patient")
                      mycursor=mydb.cursor()
                      mycursor.execute("CREATE TABLE patient_details(TOKEN_NO INTEGER(3),DATE_TIME VARCHAR(50),NAME VARCHAR(50),AGE INTEGER(2),GENDER VARCHAR(10),ADDRESS VARCHAR(100),DEPARTMENT varchar(35),VISITED_DOCTOR VARCHAR(50))")

                elif a==2:
                      
                      #CREATE DOCTOR DATABASE
                      
                      import mysql.connector
                      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH")
                      mycursor=mydb.cursor()
                      mycursor.execute("CREATE DATABASE DOCTOR")
                      print("DATABASE CREATED SUCCESSFULLY")
                      import mysql.connector
                      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="doctor")
                      mycursor=mydb.cursor()
                      mycursor.execute("CREATE TABLE doctor_details(DID INTEGER PRIMARY KEY,NAME VARCHAR(20),AGE INTEGER(2),GENDER VARCHAR(10),ADDRESS VARCHAR(100),DEPARTMENT VARCHAR(50),QUALIFICATION VARCHAR(30),TIMINGS VARCHAR(20),DAYS_AVAILABLE VARCHAR(50),SALARY VARCHAR(10),SALARYSLIP_NO INTEGER)")
                      
                elif a==3:
                      x=int(input("WHOSE DATABASE WOULD YOU LIKE TO CREATE\n 1.AMBULANCE SERVICE\n 2.DRIVER DETAILS\n 3.AMBULANCE DETAILS"))
                      if x==1:
                            
                            #CREATE AMBULANCE DATABASE
                            
                            import mysql.connector
                            mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH")
                            mycursor=mydb.cursor()
                            mycursor.execute("CREATE DATABASE AMBULANCE")
                            print("DATABASE CREATED SUCCESSFULLY")
                            import mysql.connector
                            mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="AMBULANCE")
                            mycursor=mydb.cursor()
                            mycursor.execute("CREATE TABLE ambulance_service(TOKEN_NO INTEGER,DATE_TIME VARCHAR(50),PATIENT_NAME VARCHAR(30),AGE INTEGER,GENDER VARCHAR(5),ADDRESS VARCHAR(100),PICKUP_POINT VARCHAR(30),DESTINATION_POINT VARCHAR(30),DRIVER_NAME VARCHAR(30),PHONE_NO_DRIVER INTEGER)")

                      if x==2:
                            
                            # CREATE DRIVER DETAILS DATABASE
                            
                            import mysql.connector
                            mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="AMBULANCE")
                            mycursor=mydb.cursor()
                            mycursor.execute("CREATE TABLE DRIVER_DETAILS(DID INTEGER,DRIVER_NAME VARCHAR(30),AGE INTEGER,GENDER CHAR(2),ADDRESS VARCHAR(100),VEHICLE_NO INTEGER,PHONE_NO INTEGER(20))")
            
                      if x==3:
                            
                            # CREATE AMBULANCE DETAILS DATABASE
                            
                            import mysql.connector
                            mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="AMBULANCE")
                            mycursor=mydb.cursor()
                            mycursor.execute("CREATE TABLE AMBULANCE_DETAILS(VEHICLE_NO VARCHAR(20),MODEL VARCHAR(15),DRIVER_NAME VARCHAR(20),YEAR_MANUFACTURED INTEGER,FACILITIES VARCHAR(50),SIZE VARCHAR(20),DRIVER_PHONENO INTEGER)")
                      else:
                            print("wrong input")
                          
          if q==2:
                a=int(input("WHOSE DATA WOULD YOU LIKE TO UPDATE \n 1.PATIENT 2.DOCTOR\n 3.DISPLAY DATA\n"))
                if a==1:
                      
                      #UPDATE PATIENT DATA
                      import mysql.connector
                      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="patient")
                      mycursor=mydb.cursor()
                      b=int(input("WHAT DO YOU WANT TO UPDATE\n 1.TOKEN_NO\n 2.NAME\n 3.AGE\n 4.GENDER\n 5.ADDRESS\n 6.VISITED DOCTOR"))
                      if b==1:
                            y=input("ENTER NAME:")
                            x=int(input("ENTER NEW TOKEN_NO:"))
                            c=("update patient_details set token_no=%s WHERE NAME=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("TOKEN_NO UPDATED SUCCESSFULLY")
                      if b==2:
                            y=int(input("ENTER TOKEN_NO:"))
                            x=input("ENTER NEW NAME:")
                            c=("update patient_details set NAME=%s WHERE TOKEN_NO=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("NAME UPDATED SUCCESSFULLY")
                      if b==3:
                            y=input("ENTER TOKEN_NO:")
                            x=int(input("ENTER NEW AGE:"))
                            c=("update patient_details set AGE=%s WHERE TOKEN_NO=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("AGE UPDATED SUCCESSFULLY")
                      if b==4:
                            y=input("ENTER TOKEN_NO:")
                            x=(input("ENTER NEW Gender:"))
                            c=("update patient_details set gender=%s WHERE TOKEN_NO=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("GENDER UPDATED SUCCESSFULLY")
                      if b==5:
                            y=input("ENTER TOKEN_NO:")
                            x=(input("ENTER NEW ADDRESS:"))
                            c=("update patient_details set ADDRESS=%s WHERE TOKEN_NO=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("ADDRESS UPDATED SUCCESSFULLY")
                      if b==6:
                            y=input("ENTER TOKEN_NO:")
                            x=(input("ENTER NEW VISITED DOCTOR:"))
                            c=("update patient_details set VISITED_DOCTOR=%s WHERE TOKEN_NO=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("DATA UPDATED SUCCESSFULLY")
                if a==2:
                      
                      #UPDATE DOCTOR DATA
                      import mysql.connector
                      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="DOCTOR")
                      mycursor=mydb.cursor()
                      b=int(input("WHAT DO YOU WANT TO UPDATE\n 1.DID\n 2.NAME\n 3.AGE\n 4.GENDER\n 5.ADDRESS\n 6.DEPARTMENT\n 7.QUALIFICATIONS\n 8.TIMINGS \n 9.DAYS AVAILABLE\n 10.SALARY\n 11.SALARY SLIP NUMBER\n"))
                      if b==1:
                            y=input("ENTER name:")
                            x=int(input("ENTER NEW DID:"))
                            c=("update DOCTOR_details set DID=%s WHERE NAME=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("DID UPDATED SUCCESSFULLY")
                          
                      if b==2:
                            y=input("ENTER DID:")
                            x=(input("ENTER NEW NAME:"))
                            c=("update DOCTOR_details set NAME=%s WHERE DID=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("NAME UPDATED SUCCESSFULLY")
                          
                      if b==3:
                            y=input("ENTER DID:")
                            x=int(input("ENTER NEW Age:"))
                            c=("update DOCTOR_details set age=%s WHERE DID=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("Age UPDATED SUCCESSFULLY")
                            
                      if b==4:
                            y=input("ENTER DID:")
                            x=(input("ENTER NEW GENDER:"))
                            c=("update DOCTOR_details set GENDER=%s WHERE DID=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("GENDER UPDATED SUCCESSFULLY")
                        
                      if b==5:
                            y=input("ENTER DID:")
                            x=(input("ENTER NEW ADDRESS:"))
                            c=("update DOCTOR_details set address=%s WHERE DID=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("ADDRESS UPDATED SUCCESSFULLY")

                      if b==6:
                            y=input("ENTER DID:")
                            x=(input("ENTER NEW DEPARTMENT:"))
                            c=("update DOCTOR_details set DEPARTMENT=%s WHERE DID=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("DEPARTMENT UPDATED SUCCESSFULLY")

                      if b==7:
                            y=input("ENTER DID:")
                            x=(input("ENTER NEW QUALIFICATIONS:"))
                            c=("update DOCTOR_details set QUALIFICATIONS=%s WHERE DID=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("QUALIFICATIONS UPDATED SUCCESSFULLY")
                            
                      if b==8:
                            y=input("ENTER DID:")
                            x=(input("ENTER NEW TIMINGS:"))
                            c=("update DOCTOR_details set TIMINGS=%s WHERE DID=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("TIMINGS UPDATED SUCCESSFULLY")

                      if  b==9:
                            y=input("ENTER DID:")
                            x=(input("ENTER NEW DAYS AVAILABLE:"))
                            c=("update DOCTOR_details set DAYS_AVAILABLE=%s WHERE DID=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("DAYS AVAILABLE UPDATED SUCCESSFULLY")
                      if b==10:
                            y=int(input("ENTER SALARY SLIP NUMBER:"))
                            x=(input("ENTER NEW SALARY:"))
                            c=("update DOCTOR_details set SALARY=%s WHERE SALARYSLIP_NO=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("SALARY AVAILABLE UPDATED SUCCESSFULLY")
                        
                      if b==11:
                            y=input("ENTER DID:")
                            x=(input("ENTER NEW SALARYSLIP NUMBER:"))
                            c=("update DOCTOR_details set SALARYSLIP_NO=%s WHERE DID=%s")
                            t=(x,y)
                            mycursor.execute(c,t)
                            mydb.commit()
                            print("SALARY SLIP NUMBER UPDATED SUCCESSFULLY")
          if q==3:
                
                # DELETE DATA
                import mysql.connector
                
                x=int(input("WHOSE DATA WOULD YOU LIKE TO DELETE \n 1.PATIENT \n 2.DOCTOR\n:"))
                if x==1:
                      q=int(input("ENTER TOKEN NO:"))
                      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="patient")
                      mycursor=mydb.cursor()
                      c=("DELETE from patient_details WHERE TOKEN_NO=%s")
                      t=(q,)
                      mycursor.execute(c,t)
                      mydb.commit()
                      print("DATA DELETED SUCCESSFULLY")

                if x==2:
                      q=int(input("ENTER DID:"))
                      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="DOCTOR")
                      mycursor=mydb.cursor()
                      c=("DELETE from DOCTOR_details WHERE DID=%s")
                      t=(q,)
                      mycursor.execute(c,t)
                      mydb.commit()
                      print("DATA DELETED SUCCESSFULLY")
                      print("SALARY SLIP NUMBER UPDATED SUCCESSFULLY")
                      
          if q==4:
                # PRINT DATA
                import mysql.connector
                
                x=int(input("WHOSE DATA WOULD YOU LIKE TO PRINT \n 1.PATIENT \n 2.DOCTOR\n:"))
                if x==1:
                      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="patient")
                      mycursor=mydb.cursor()
                      mycursor.execute("select * from patient_details")
                      e=mycursor.fetchall()
                      print(tabulate(e,headers=['TOKEN_NO-','Name-','AGE-','GENDER-','ADDRESS-','DEPARTMENT-','DOCTOR-'],tablefmt="grid"))

                if x==2:
                      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="DOCTOR")
                      mycursor=mydb.cursor()
                      c=("select * from DOCTOR_details")
                      mycursor.execute(c)
                      e=mycursor.fetchall()
                      print(tabulate(e,headers=['DID','NAME','AGE','GENDER','ADDRESS','DEPARTMENT','QUALIFICATIONS','TIMINGS','DAYS AVAILABLE','SALARY','SALARY SLIP NO',],tablefmt="grid"))


          if q==5:
                # ADD DOCTOR DATA
                import mysql.connector
                
                x=int(input("ENTER DID NO:"))
                y=input("ENTER NAME:")
                z=int(input("ENTER AGE:"))
                q=input("ENTER GENDER:")
                w=input("ENTER ADDRESS:")
                e=input("ENTER DEPARTMENT:")
                r=input("ENTER QUALIFICATIONS:")
                t=input("ENTER TIMINGS:")
                y=input("ENTER DAYS AVIALABLE:")
                u=input("ENTER SALARY:")
                i=int(input("ENTER salary slip no:"))
                import mysql.connector
                mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="doctor")
                mycursor=mydb.cursor()
                c=("INSERT INTO DOCTOR_DETAILS(DID,NAME,AGE,GENDER,ADDRESS,DEPARTMENT,QUALIFICATION,TIMINGS,DAYS_AVAILABLE,SALARY,SALARYSLIP_NO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                h=(x,y,z,q,w,e,r,t,y,u,i)
                mycursor.execute(c,h)
                mydb.commit()
                print("DATA ADDED SUCCESSFULLY")
                            
    else:
          print("wrong password")
          

#project_data
        
def PROJECTDOCTOR_DATA():

      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="doctor")
      mycursor=mydb.cursor()
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(19,'DR.ROY MATHEW',34,'M','23 RK ROAD,KANNUR','PEDIATRICS','MBBBS','1PM-5PM','MONDAY,WEDNESDAY,FRIDAY','$2000',78945)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(27,'DR.JAMES DINO',24,'M','34 RAMASWAMI ROAD,KANNUR','SURGEON','MBBBS','9AM-5PM','MONDAY,TUESDAY,FRIDAY','$2400',54755)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(34,'DR.JOHNS ABRAHAM',25,'M','HOUSE NO 78 BRIJ VIHAR,KASARGOD','CARDIOLOGISTS','MBBBS','1PM-3PM','MONDAY,FRIDAY','$3000',45645)")

      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(49,'DR.RAHUL NAIR',54,'M','HOUSE NO34 GANESH NAGAR,TALIPARAMBA','ANESTHESIOLOGISTS','MBBBS','10AM-8PM','MONDAY,TUESDAY,WEDNESDAY,FRIDAY','$1800',14753)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(57,'DR.RENUKA LAKSHMI',37,'F','23 ED ROAD,CHALA','DERMATOLOGISTS','MBBBS','8PM-10AM','MONDAY,WEDNESDAY','$2300',35845)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(61,'DR JIBIL JAMES',57,'M','48 GANDHI ROAD,PAYYANUR','ENDOCRINOLOGISTS','MBBBS','11AM-1PM','MONDAY,TUESDAY,THURSDAY,FRIDAY','$2600',78978)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(77,'ROY CYIAC',44,'M','KUDILIL HOUSE,MALAKLLU,KANNUR','FAMILY PHYSICIAN','MBBBS','10AM-5PM','DAILY','$2800',742014)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(87,'JYOTHIS SANJAY',31,'M','23 TK ROAD,KANNUR','NEUROLOGISTS','MBBBS','1PM-5PM','MONDAY,WEDNESDAY,FRIDAY','$2900',12456)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(90,'NEHA MATHEW',25,'F','45 RADHA HOUSE,KAMBIL','GYNECOLOGISTS','MBBBS','10AM-3PM','MONDAY,WEDNESDAY,THURSDAY,FRIDAY','$2400',24785)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(10,'MATHEW JOHN',24,'M','KUNDAN HOUSE, KANNUR','OPTHALMOLOGISTS','MBBBS','1PM-3PM','MONDAY,WEDNESDAY,FRIDAY','$3000',54236)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(71,'JWALA MARY',49,'F','45 MK ROAD,KANNUR','PLASTIC SURGEONS','MBBBS','1PM-5PM','MONDAY,WEDNESDAY,FRIDAY,SATURDAY','$2080',36541)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(82,'JITHIN THOMAS',24,'M','67 MP ROAD,KANNUR','PSYCHIATRISTS','MBBBS','9AM-12PM','MONDAY,WEDNESDAY,FRIDAY,SUNDAY','$3000',78000)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(63,'ANNIE THOMAS',56,'F','23 RK ROAD,KANNUR','RADIOLOGISTS','MBBBS','1PM-2PM','MONDAY','$5000',11111)")
      
      mycursor.execute("INSERT INTO DOCTOR_DETAILS VALUES(44,'JOHNNY LAL',51,'M','56 MALL ROAD,KANNUR','GENERAL SURGEONS','MBBBS','10AM-6PM','MONDAY,TUESDAY,WEDNESDAY,FRIDAY,SATURDAY','$4000',88994)")
      
      mydb.commit()
      
#ambulance_data
      
def PROJECTAMBULANCE_DATA():
      
      mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="AMBULANCE")
      mycursor=mydb.cursor()
      mycursor.execute("INSERT INTO DRIVER_DETAILS VALUES(12,'RAJESH KUMAR',34,'M','BESIDE MB CHWAK,TALIPARAMBA',2334,876162781)")
      mycursor.execute("INSERT INTO AMBULANCE_DETAILS VALUES(2334,'FORCE 4020','RAJESH KUMAR',2000,'ELECTRIC POWER,OXYGEN,SUCTION,STRETCHER,MONITOR','LARGE',876162781)")
      
      mycursor.execute("INSERT INTO DRIVER_DETAILS VALUES(78,'RAJU MATHEW',54,'M','BESIDE GB CHAWCK,TALIP',8744,784572781)")
      mycursor.execute("INSERT INTO AMBULANCE_DETAILS VALUES(8744,'FORCE 4060','RAJU MATHEW',2004,'OXYGEN,STRETCHER,MONITOR','LARGE',784572781)")
      
      mycursor.execute("INSERT INTO DRIVER_DETAILS VALUES(18,'JOHNNY LAL',34,'M','HOUSE NO 34,RK COLONY,TALIPARAMBA',6977,851155477)")
      mycursor.execute("INSERT INTO AMBULANCE_DETAILS VALUES(6977,'MAHINDRA SUPRO','JOHNNY LAL',2002,'OXYGEN,MONITOR','MEDIUM',851155477)")
      
      mycursor.execute("INSERT INTO DRIVER_DETAILS VALUES(22,'SURABHI SINGH',24,'F','CK ROAD,TALIPARAMBA',4157,875466742)")
      mycursor.execute("INSERT INTO AMBULANCE_DETAILS VALUES(4157,'TATA WINGER','SURABHI SINGH',2010,'OXYGEN,AC','SMALL',875466742)")
      
      mycursor.execute("INSERT INTO DRIVER_DETAILS VALUES(89,'NARAYAN JOSHI',44,'M','JOSHI HOUSE,KASARGOD',5621,654189324)")
      mycursor.execute("INSERT INTO AMBULANCE_DETAILS VALUES(5621,'FORCE 4020','NARAYAN JOSHI',2016,'OXYGEN,MONITOR,SUCTION','LARGE',654189324)")
      
      mycursor.execute("INSERT INTO DRIVER_DETAILS VALUES(55,'JOB JOSE',49,'M','HOUSE NO 45,MADAMPAM,TALIPARAMBA',2338,776627815)")
      mycursor.execute("INSERT INTO AMBULANCE_DETAILS VALUES(2338,'FORCE 3000','JOB JOSE',2021,'OXYGEN,STRETCHER','MEDIUM',776627815)")

      mycursor.execute("INSERT INTO DRIVER_DETAILS VALUES(01,'MOHAMMAD ALI KHAN',51,'M','BESIDE SK VILLA,THAMBA',4559,854562815)")
      mycursor.execute("INSERT INTO AMBULANCE_DETAILS VALUES(4559,'MARUTI OMNI','MOHAMMAD ALI KHAN',2014,'OXYGEN,AC,MONITOR','SMALL',854562815)")

      mycursor.execute("INSERT INTO DRIVER_DETAILS VALUES(14,'RAKESH MOHAN',64,'M','NEAR RK PURAM,KANHANGAD',5454,876162815)")
      mycursor.execute("INSERT INTO AMBULANCE_DETAILS VALUES(5454,'MAHINDRA SUPRO','RAKESH MOHAN',2020,'ELECTRIC POWER,AC,OXYGEN,STRETCHER','LARGE',876162815)")

      mycursor.execute("INSERT INTO DRIVER_DETAILS VALUES(98,'RAM YADAV',41,'M','YADAV HOUSE,TALIP',2222,877412785)")
      mycursor.execute("INSERT INTO AMBULANCE_DETAILS VALUES(2222,'HEARSE VAN','RAM YADAV',2016,'OXYGEN,AC,MONITOR,STRETCHER,VENTILATOR','LARGE',877412785)")

      mycursor.execute("INSERT INTO DRIVER_DETAILS VALUES(85,'MANAS MISHRA',29,'M','NEAR JUHU BEACH,HOSDURG',1234,982562815)")
      mycursor.execute("INSERT INTO AMBULANCE_DETAILS VALUES(1234,'MARUTI OMNI','MANAS MISHRA',2018,'OXYGEN','MEDIUM',982562815)")

      mydb.commit()


#ambulance
      
def ambulance():
      a=[["1.BOOK AMBULANCE" ],["2.CHECK BOOKING DETAILS"]]
      headers=["WHAT WOULD YOU LIKE TO DO"]
      print(tabulate(a,headers,tablefmt="rst"))
      r=int(input(""))
      
      if r==1:
            
            #to book  ambulance
            import random
            j=random.randint(1,100)
            x=input("Please enter patient's name in block letters:")
            y=int(input("Enter your age:"))
            v=input("enter your Gender (M/F/RATHER NOT TO SAY):")
            z=input("Enter your Address:")
            q=input("Enter pick up point:")
            w=input("Enter Destination:")
            mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="ambulance")
            mycursor=mydb.cursor()
            c=("select DID,DRIVER_NAME,VEHICLE_NO,PHONE_NO from DRIVER_details")
            d=("select size from ambulance_details") 
            mycursor.execute(c,)
            e=mycursor.fetchall()
            headers=["DID","DRIVER NAME","VEHICLE NO","PHONE NO"]
            print(tabulate(e,headers,tablefmt="grid"))
            l=int(input("ENTER VEHICLE NUMBER TO BOOK AMBULANCE:"))
            print("YOUR TOKEN NO IS:",j)
            print("AMBULANCE BOOKED SUCCESSFULLY")
            mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="ambulance")
            mycursor=mydb.cursor()
            c=("INSERT INTO AMBULANCE_SERVICE(TOKEN_NO,date_time,PATIENT_NAME,AGE,GENDER,ADDRESS,PICKUP_POINT,DESTINATION_POINT,DRIVER_NAME) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            t=(j,string,x,y,v,z,q,w,l)
            mycursor.execute(c,t)
            mydb.commit()
            print("THANK YOU")
      

      if r==2:
            
            #to check booking details
            x=int(input("ENTER TOKEN_NO TO DISPLAY DATA:"))
            mydb=mysql.connector.connect(host="localhost",user="root",password="BINEESH",database="ambulance")
            mycursor=mydb.cursor()
            c=("select * from AMBULANCE_SERVICE where token_no=%s")
            t=(x,)
            mycursor.execute(c,t)
            e=mycursor.fetchall()
            print(tabulate(e,headers=["TOKEN_NO","DATE_TIME","PATIENT_NAME","AGE","GENDER","ADDRESS","PICKUP_POINT","DESTINATION","DRIVER_NAME"],tablefmt="grid"))

     
            
      
project()

#END
      








