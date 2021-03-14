
#note/ importing all the files and modules needed for this library_management_project
import mysql.connector, STUDENTS1, USERS1, BOOK1, BORROWERS_RECORDS1, BookReturnRecords1
#note/ connecting with sql database
mydb= mysql.connector(host="127.0.0.1", user="root", passwd="2zkNKcz&EOZaRjc$",database="library_management_project")
#note/ storing sql data in mycursor
mycursor=mydb.cursor()
errormessage='''
YOU HAVE GIVEN WRONG INPUT!!!
POSSIBLE ERRORS MIGHT INCLUDE:-
1.WRONG SPELLING
2.ROLE DOESN'T MATCH WITH THE DEFINED LIBRARY TYPE USERS'''
goback="DON'T WASTE TIME OF OTHERS AND YOURS PLEASE"
usernotexist="THIS USER_ID DOESN'T EXIST IN THE DATABASE"
#note/ first we will check that if the user is STAFF or STUDENT
stafforstudent=input("ARE YOU A STAFF OR STUDENT? ")
if stafforstudent.lower()=="staff":
    #note/ now we will check if the staff member is already registered or not
    registereduser=input("ARE YOU A REGISTERED STAFF MEMBER OF THIS LIBRARY? ")
    if registereduser.lower()=="yes":
        #note/ here we will check the staff member's presence in the database
        staffID=int(input("PLEASE ENTER YOUR STAFF_ID:- "))
        #todo query to verify the presence of staff_ID in the database
        verificationstf="PLACE HOLDER TEXT"     #todo query to check the presence of this exact staffID into the database
        if verificationstf==True:       #todo write the condition correctly in order to verify the user as existing
            #note/ here we will ask the user to enter the specific task they want to perform
            wdywtd=input('''
            WHAT ACTION DO YOU WANT TO PERFORM FROM THE GIVEN OPTIONS(WRITE NO. OF THE ACTION YOU WANT TO PERFORM):-
            1.BORROW A BOOK
            2.RETURN A BOOK
            3.MANAGE YOUR DATA
            4.FETCH YOUR DATA
            5.ADD A BOOK
            6.MANAGE THE DATA OF A BOOK''')
            #note/ here we are forwarding the program to another program file BORROWERS_RECORDS in order for the user to borrow the book
            if wdywtd==1:
                BORROWERS_RECORDS1.borrowerstaffadd()
            #note/ here we are forwarding the program to another program file BookReturnRecords in order for the user to successfully return the book
            elif wdywtd==2:
                BookReturnRecords1.returneestaffadd()
            #note/ here we are forwarding the program to another program file USERS in order for users to update their data in the database
            elif wdywtd==3:
                USERS1.userupdate()
            #note/ here we are showing the user their data as registered in the database
            elif wdywtd==4:
                pass    #todo query to show the OP's data from the database
            #note/ here the staff member can add the new book's data in the database
            elif wdywtd==5:
                BOOK1.bookadd()
            #note/ here the staff member can update the data of existing books in the database
            elif wdywtd==6:
                BOOK1.bookupdate()      #!THERE MIGHT BE A PROBLEM HERE
            else:
                print(errormessage)
        elif verificationstf==False:       #todo write the condition correctly in order to verify the user as non-existing
            print(usernotexist)
        else:
            print(errormessage)
    elif registereduser.lower()=="no":
        #note/ here the staff member can add their data in the database
        wdyw=input("DO YOU WANT TO REGISTER AS A NEW STAFF MEMBER OF THIS LIBRARY? ")
        if wdyw.lower()=="yes":
            USERS1.useradd()
        elif wdyw.lower()=="no":
            print(goback)
        else:
            print(errormessage)
    else:
        print(errormessage)
elif stafforstudent.lower()=="student":
    #note/ here we are checking if the student is already registered or not
    registereduser=input("ARE YOU A REGISTERED STUDENT OF THIS LIBRARY? ")
    if registereduser.lower()=="yes":
        #note/ here we will verify the students presence in the database
        studID=int(input("PLEASE ENTER YOUR STUDENT_ID:- "))
        #todo query ot verify the presence of studID into the database
        verificationst="PLACE HOLDER TEXT"     #todo query to check the presence of this exact studID into the database
        if verificationst==True:       #todo write the condition correctly in order to verify the user as existing
            #note/ here we will ask the user to enter the specific task they want to perform
            wdywtd=input('''
            WHAT ACTION DO YOU WANT TO PERFORM FROM THE GIVEN OPTIONS(WRITE NO. OF THE ACTION YOU WANT TO PERFORM):-
            1.BORROW A BOOK
            2.RETURN A BOOK
            3.MANAGE YOUR DATA
            4.FETCH YOUR DATA''')
            #note/ here we are forwarding the program to another program file BORROWERS_RECORDS in order for the user to borrow the book
            if wdywtd==1:
                BORROWERS_RECORDS1.borrowerstudentadd()
            #note/ here we are forwarding the program to another program file BookReturnRecords in order for the user to successfully return the book
            elif wdywtd==2:
                BookReturnRecords1.returneestudentadd()
            #note/ here we are forwarding the program to another program file STUDENTS in order for users to update their data in the database
            elif wdywtd==3:
                STUDENTS1.userupdate()
            #note/ here we are showing the user their data as registered in the database
            elif wdywtd==4:
                pass    #todo query to show the OP's data from the database
            else:
                print(errormessage)
        elif verificationst==False:       #todo write the condition correctly in order to verify the user as non-existing
            print(usernotexist)
        else:
            print(errormessage)
    elif registereduser.lower()=="no":
        #note/ here the student can add their data in the database
        wdyw=input("DO YOU WANT TO REGISTER AS A NEW USER OF THIS LIBRARY? ")
        if wdyw.lower()=="yes":
            STUDENTS1.useradd()
        elif wdyw.lower()=="no":
            print(goback)
        else:
            print(errormessage)
    else:
        print(errormessage)
else:
    print(errormessage)