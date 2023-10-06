# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 18:42:57 2022

@author: milos
"""

# -*- coding: utf-8 -*-
import sqlite3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("""Content-type:text/html\n\n
<!DOCTYPE html>
<head>
    <title> Change number of students enrolled in a course </title>
</head>
<body> """)
    
form = cgi.FieldStorage()

course_code = int(form["course_code"].value)
nof_students = int(form["nof_students"].value)

db_connection = sqlite3.connect('test_courses.db')
cursor = db_connection.cursor()
try:
    cursor.execute("""UPDATE Courses set nof_students = ? where course_code = ?""", \
             	(nof_students, course_code))
    x = cursor.rowcount
    if cursor.rowcount < 1:
        print('<h2> Course ' + str(course_code) + ' does not exist </h2>')
    else:
        print('<h2> Course: ' + str(course_code) + ': number of students enrolled was set to ' + str(nof_students) + '</h2>')  

except sqlite3.Error as er:
    print('<h2> Error in SELECT: ', er + '<h2/>')


db_connection.commit()
db_connection.close()

print("""  <hr>
           <p> <a href="http://localhost:5556/cgi-bin/contactList.py" > Show course list. </a> </p>
           <p> <a href="http://localhost:5556/index.html" > Return to main page. </a> </p>
      
</body>
</html>""")