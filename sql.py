import sqlite3

#connect to sqlit
connection = sqlite3.connect("student.db")

#create a cursor to insert record, create table, retrieve
cursor = connection.cursor()

##create the table 
table_info = """
CREATE TABLE STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

##insert some more records
 
cursor.execute('''Insert into STUDENT values("kanishka","maths","A",90)''')
cursor.execute('''Insert into STUDENT values("dilu","bio","B",80)''')
cursor.execute('''Insert into STUDENT values("krish","data science","A",98)''')
cursor.execute('''Insert into STUDENT values("john","devops","A",91)''')
cursor.execute('''Insert into STUDENT values("virat","devops","A",96)''')

##display all the record
print("The insert records are")

data = cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)

##close the connection
connection.commit()
connection.close()