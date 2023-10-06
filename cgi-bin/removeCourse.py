# -*- coding: utf-8 -*-
import sqlite3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("""Content-type:text/html\n\n
<!DOCTYPE html>
<head>
    <title> Remove Course </title>
</head>
<body> """)
    
form = cgi.FieldStorage()

course_code = str(form["course_code"].value)

db_connection = sqlite3.connect('test_courses.db')
cursor = db_connection.cursor()



try:
    sql_update_query = """DELETE from Courses where course_code = ?"""
    cursor.execute(sql_update_query, (course_code,))
    x = cursor.rowcount
    if cursor.rowcount < 1:
        print('<h2> Course ' + course_code + ' does not exist </h2>')
    else:
        print('<h2> Course: ' + course_code + ' was removed' + '</h2> </p>')  

except sqlite3.Error as er:
    print('<h2> Error in SELECT: ', er + '<h2/>')


print("""  <p> <a href="http://localhost:5556/cgi-bin/contactList.py" > Show course list. </a> </p>
           <p> <a href="http://localhost:5556/index.html" > Return to main page. </a> </p>
           </body>
           </html>""")
db_connection.commit()
db_connection.close()
#xcept sqlite3.Error as er:
#print('Error in DELETE: ',er.message)