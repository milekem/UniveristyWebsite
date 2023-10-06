#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("""Content-type:text/html\n\n
<!DOCTYPE html>
<head>
    <title> New Course </title>
</head>
<body> """)
    
form = cgi.FieldStorage()

course_name = str(form["course_name"].value)
course_code = str(form["course_code"].value)
nof_students = int(form["nof_students"].value)

db_connection = sqlite3.connect('test_courses.db')
cursor = db_connection.cursor()

try:
    cursor.execute('INSERT INTO Courses VALUES(?, ?, ?);' , \
               	(course_name, course_code, nof_students ))
    print('<h2> A new course was added ' + \
      	course_code + ', ' + course_name + '</h2> <p>')    
except sqlite3.Error as er:
	print('Error in INSERT: ', er)
db_connection.commit()
db_connection.close()


print("""  <p> <a href="http://localhost:5556/cgi-bin/contactList.py" > Show course list. </a> </p>
           <p> <a href="http://localhost:5556/index.html" > Return to main page. </a> </p>
      
</body>
</html>""")