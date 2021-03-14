import mysql.connector
mydb= mysql.connector(host="127.0.0.1", user="root", passwd="2zkNKcz&EOZaRjc$",database="library_management_project")
def returneestudentadd():
    Borrowers_IDp=int(input("ENTER YOUR BORROWERS_ID:- "))
    #todo query to add this expression into the database
    bookIDp=int(input("ENTER YOUR BOOK'S ID:- "))
    #todo query to add this expression into the database
    bktitlep=input("ENTER YOUR BOOK'S TITLE/NAME:- ")
    #todo query to add this expression into the database
    studIDp=input("ENTER YOUR STUDENT_ID:- ")
    #todo query to add this expression into the database
    stfnamep=input("ENTER YOUR FIRST NAME:- ")
    #todo query to add this expression into the database
    releaseDatep=int(input("ENTER RELEASE DATE(MMDDYYYY):- "))
    #todo query to add this expression into the database
    duedatep=int(input("ENTER YOUR DUE DATE(MMDDYYYY):- "))
    #todo query to add this expression into the database
    bkdatereturnp=int(input("ENTER THE BOOK RETURN DATE(MMDDYYYY)"))
    #todo query to add this expression into the database
def returneestaffadd():
    Borrowers_IDp=int(input("ENTER YOUR BORROWERS_ID:- "))
    #todo query to update this expression into the database
    bookIDp=int(input("ENTER YOUR BOOK'S ID:- "))
    #todo query to update this expression into the database
    bktitlep=input("ENTER YOUR BOOK'S TITLE/NAME:- ")
    #todo query to update this expression into the database
    staffIDp=input("ENTER YOUR STUDENT_ID:- ")
    #todo query to update this expression into the database
    stffnamep=input("ENTER YOUR FIRST NAME:- ")
    #todo query to update this expression into the database
    releaseDatep=int(input("ENTER RELEASE DATE(MMDDYYYY):- "))
    #todo query to update this expression into the database
    duedatep=int(input("ENTER YOUR DUE DATE(MMDDYYYY):- "))
    #todo query to update this expression into the database
    bkdatereturnp=int(input("ENTER THE BOOK RETURN DATE(MMDDYYYY)"))
    #todo query to update this expression into the database