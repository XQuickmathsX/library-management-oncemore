import mysql.connector
mydb= mysql.connector.connect(host="127.0.0.1", user="root", passwd="2zkNKcz&EOZaRjc$",database="library_management_project")
mycursor=mydb.cursor()
def bookadd():
    bookIDp=input("ENTER THE BOOK'S ID:- ")
    #todo query to add this expression into the database
    bktitlep=input("ENTER THE BOOK'S TITLE/NAME:- ")
    #todo query to add this expression into the database
    bkauthorp=input("ENTER THE BOOK'S AUTHOR NAME:- ")
    #todo query to add this expression into the database
    bkpublisherp=input("ENTER THE BOOK'S PUBLISHER NAME:- ")
    #todo query to add this expression into the database
    bkcopiesp=int(input("ENTER THE TOTAL NUMBER OF THE COPIES OF THIS BOOK:- "))
    #todo query to add this expression into the database
    bk_sourcep=input("ENTER THE BOOK'S SOURCE:- ")
    #todo query to add this expression into the database
    bk_costp=int(input("ENTER THE BOOK'S COST OF ONE UNIT:- "))
    #todo query to add this expression into the database
    bk_remarksp=input("ENTER BOOK'S REMARKS:- ")
    #todo query to add this expression into the database
def bookupdate():
    bookIDp=input("ENTER THE BOOK'S ID:- ")
    #todo query to update this expression into the database
    bktitlep=input("ENTER THE BOOK'S TITLE/NAME:- ")
    #todo query to update this expression into the database
    bkauthorp=input("ENTER THE BOOK'S AUTHOR NAME:- ")
    #todo query to update this expression into the database
    bkpublisherp=input("ENTER THE BOOK'S PUBLISHER NAME:- ")
    #todo query to update this expression into the database
    bkcopiesp=int(input("ENTER THE TOTAL NUMBER OF THE COPIES OF THIS BOOK:- "))
    #todo query to update this expression into the database
    bk_sourcep=input("ENTER THE BOOK'S SOURCE:- ")
    #todo query to update this expression into the database
    bk_costp=int(input("ENTER THE BOOK'S COST OF ONE UNIT:- "))
    #todo query to update this expression into the database
    bk_remarksp=input("ENTER BOOK'S REMARKS:- ")
    #todo query to update this expression into the database
