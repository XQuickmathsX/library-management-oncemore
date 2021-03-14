CREATE DATABASE library_management_project;

use library_management_project;

CREATE table STUDENTS (
stud_ID integer(11) PRIMARY KEY,
stfname char(20),
stlname char(20),
stcourse varchar(20),
styear year,
stcontact integer(10),
stage integer(2),
stbirthdate date,
stgender char(1)
);

CREATE table USERS (
staff_ID integer(20) PRIMARY KEY,
stffname char(20),
stflname char(20),
stfcontactnumber integer(20),
stfemail varchar(80),
stfaddresss varchar(100),
stfpassword varchar(16),
stftype char(20)
);

CREATE TABLE BOOK( 
book_ID VARCHAR(10) PRIMARY KEY, 
bktitle VARCHAR(100), 
bkedition VARCHAR(100), 
bkauthor CHAR(20), 
bkpublisher CHAR(20), 
bkcopies INT(100), 
bk_source CHAR(50), 
bk_cost INT(4),
bk_remarks VARCHAR(150)
);

CREATE TABLE borrowers_records( 
Borrowers_ID INTEGER(20) PRIMARY KEY, 
book_ID VARCHAR(10), 
bktitle VARCHAR(100), 
stud_ID INTEGER(11), 
stffname CHAR(20), 
staff_ID INTEGER(20), 
studentNOcopies VARCHAR(100), 
releaseDate DATE, 
dueDATE DATE
);

CREATE TABLE BookReturnRecords( 
Borrowers_ID INTEGER(20) PRIMARY KEY, 
book_ID VARCHAR(10), 
bktitle VARCHAR(100), 
stud_ID INTEGER(11), 
stfname CHAR(20), 
staff_ID INTEGER(20), 
stffname CHAR(20), 
studentNOcopies VARCHAR(100), 
releaseDate DATE, 
duedate DATE, 
bkdatereturn DATE 
)