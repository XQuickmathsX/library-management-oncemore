import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="5678",database="library_management_project")
mycursor=mydb.cursor()
def useradd():
    studIDp=int(input("ENTER YOUR STUDENT_ID:- "))
    mycursor.execute("INSERT INTO STUDENTS (stud_ID) VALUES (studIDp)")
    mydb.commit()
    stfnamep=input("ENTER YOUR FIRST NAME:- ")
    mycursor.execute("INSERT INTO STUDENTS (stfname) VALUES (stfnamep)")
    mydb.commit()
    stlnamep=input("ENTER YOUR LAST NAME:- ")
    mycursor.execute("INSERT INTO STUDENTS (stlname) VALUES (stlnamep)")
    mydb.commit()
    stcoursep=input("ENTER YOUR COURSE:- ")
    mycursor.execute("INSERT INTO STUDENTS (stcourse) VALUES (stcoursep)")
    mydb.commit()
    styearp=int(input("ENTER YOUR ADMISSION YEAR:- "))
    mycursor.execute("INSERT INTO STUDENTS (styear) VALUES (styearp)")
    mydb.commit()
    stcontactp=int(input("ENTER YOUR CONTACT NUMBER:- "))
    mycursor.execute("INSERT INTO STUDENTS (stcontact) VALUES (stcontactp)")
    mydb.commit()
    stagep=int(input("ENTER YOUR AGE:- "))
    mycursor.execute("INSERT INTO STUDENTS (stage) VALUES (stagep)")
    mydb.commit()
    stbirthdatep=int(input("ENTER YOUR DATE OF BIRTH(MMDDYYYY):- "))
    mycursor.execute("INSERT INTO STUDENTS (stbirthdate) VALUES (stbirthdatep)")
    mydb.commit()
    stgenderp=input("ENTER YOUR GENDER:- ")
    mycursor.execute("INSERT INTO STUDENTS (stgender) VALUES (stgenderp)")
    mydb.commit()
def userupdate():
    studIDp=int(input("ENTER YOUR STUDENT_ID:- "))
    mycursor.execute("UPDATE STUDENTS SET stud_ID = studIDp")
    mydb.commit()
    stfnamep=input("ENTER YOUR FIRST NAME:- ")
    mycursor.execute("UPDATE STUDENTS SET stud_ID = stfnamep")
    mydb.commit()
    stlnamep=input("ENTER YOUR LAST NAME:- ")
    mycursor.execute("UPDATE STUDENTS SET stlname= stlnamep")
    mydb.commit()
    stcoursep=input("ENTER YOUR COURSE:- ")
    mycursor.execute("UPDATE STUDENTS SET stcourse = stcoursep")
    mydb.commit()
    styearp=int(input("ENTER YOUR ADMISSION YEAR:- "))
    mycursor.execute("UPDATE STUDENTS SET styear = styearp")
    mydb.commit()
    stcontactp=int(input("ENTER YOUR CONTACT NUMBER:- "))
    mycursor.execute("UPDATE STUDENTS SET stcontract = stcontractp")
    mydb.commit()
    stagep=int(input("ENTER YOUR AGE:- "))
    mycursor.execute("UPDATE STUDENTS SET stage = stagep")
    mydb.commit()
    stbirthdatep=int(input("ENTER YOUR DATE OF BIRTH(MMDDYYYY):- "))
    mycursor.execute("UPDATE STUDENTS SET stbirthdate = stbirthdatep")
    mydb.commit()
    stgenderp=input("ENTER YOUR GENDER:- ")
    mycursor.execute("UPDATE STUDENTS SET stgender = stgender")
    mydb.commit()
