import mysql.connector
mydb= mysql.connector(host="127.0.0.1", user="root", passwd="2zkNKcz&EOZaRjc$",database="library_management_project")
def useradd():
    staffIDp=int(input("ENTER YOUR STAFF_ID:- "))
    #todo query to add this expression into the database
    stffnamep=input("ENTER YOUR FIRST NAME:- ")
    #todo query to add this expression into the database
    stflnamep=input("ENTER YOUR LAST NAME")
    #todo query to add this expression into the database
    stfcontactnumberp=int(input("ENTER YOUR CONTACT NUMBER:- "))
    #todo query to add this expression into the database
    stfemailp=input("ENTER YOUR EMAIL_ID:- ")
    #todo query to add this expression into the database
    stfaddressp=input("ENTER YOUR ADDRESS:- ")
    #todo query to add this expression into the database
    stfpasswordp=input("ENTER YOUR PASSWORD:- ")
    #todo query to add this expression into the database
    stftypep=input("ENTER YOUR STAFF TYPE:- ")
    #todo query to add this expression into the database
def userupdate():
    staffIDp=int(input("ENTER YOUR STAFF_ID:- "))
    #todo query to update this expression into the database
    stffnamep=input("ENTER YOUR FIRST NAME:- ")
    #todo query to update this expression into the database
    stflnamep=input("ENTER YOUR LAST NAME")
    #todo query to update this expression into the database
    stfcontactnumberp=int(input("ENTER YOUR CONTACT NUMBER:- "))
    #todo query to update this expression into the database
    stfemailp=input("ENTER YOUR EMAIL_ID:- ")
    #todo query to update this expression into the database
    stfaddressp=input("ENTER YOUR ADDRESS:- ")
    #todo query to update this expression into the database
    stfpasswordp=input("ENTER YOUR PASSWORD:- ")
    #todo query to update this expression into the database
    stftypep=input("ENTER YOUR STAFF TYPE:- ")
    #todo query to update this expression into the database