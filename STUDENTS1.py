import mysql.connector
mydb= mysql.connector(host="127.0.0.1", user="root", passwd="2zkNKcz&EOZaRjc$",database="library_management_project")
mycursor=mydb.cursor()
def useradd():
    studIDp=int(input("ENTER YOUR STUDENT_ID:- "))
    #todo query to add this expression into the database
    stfnamep=input("ENTER YOUR FIRST NAME:- ")
    #todo query to add this expression into the database
    stlnamep=input("ENTER YOUR LAST NAME:- ")
    #todo query to add this expression into the database
    stcoursep=input("ENTER YOUR COURSE:- ")
    #todo query to add this expression into the database
    styearp=int(input("ENTER YOUR ADMISSION YEAR:- "))
    #todo query to add this expression into the database
    stcontactp=int(input("ENTER YOUR CONTACT NUMBER:- "))
    #todo query to add this expression into the database
    stagep=int(input("ENTER YOUR AGE:- "))
    #todo query to add this expression into the database
    stbirthdatep=int(input("ENTER YOUR DATE OF BIRTH(MMDDYYYY):- "))
    #todo query to add this expression into the database
    stgenderp=input("ENTER YOUR GENDER:- ")
    #todo query to add this expression into the database
def userupdate():
    studIDp=int(input("ENTER YOUR STUDENT_ID:- "))
    #todo query to update this expression into the database
    stfnamep=input("ENTER YOUR FIRST NAME:- ")
    #todo query to update this expression into the database
    stlnamep=input("ENTER YOUR LAST NAME:- ")
    #todo query to update this expression into the database
    stcoursep=input("ENTER YOUR COURSE:- ")
    #todo query to update this expression into the database
    styearp=int(input("ENTER YOUR ADMISSION YEAR:- "))
    #todo query to update this expression into the database
    stcontactp=int(input("ENTER YOUR CONTACT NUMBER:- "))
    #todo query to update this expression into the database
    stagep=int(input("ENTER YOUR AGE:- "))
    #todo query to update this expression into the database
    stbirthdatep=int(input("ENTER YOUR DATE OF BIRTH(MMDDYYYY):- "))
    #todo query to update this expression into the database
    stgenderp=input("ENTER YOUR GENDER:- ")
    #todo query to update this expression into the database