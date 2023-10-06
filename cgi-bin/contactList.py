#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#!
import sqlite3
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("""Content-type:text/html\n\n
<!DOCTYPE html>
<head>
    <title> Courses </title>
</head>
<body>
    
    <h1> Courses Listed </h1>""")

db_connection = sqlite3.connect('test_courses.db')
cursor = db_connection.cursor()
try:
    cursor.execute("SELECT * FROM Courses;")
    linhas = cursor.fetchall()
except sqlite3.Error as er:
	print('<h2> Error in SELECT: ', er + '<h2/>')
    
print('<ul>')
suma = 0

for index, linha in enumerate(linhas):
    print( '<li>' + str(linha[0]) + ' ' + str(linha[1]) + ' ' \
          + str(linha[2]) + '</li>')
    suma += int(linha[2])
    loopcount = index
mean = suma/(loopcount + 1)

print('</ul>')
print('<hr>')
print('<p>'+ 'Number of courses: ' + str(loopcount + 1) + ' | ' + '\tTotal number of students:' + str(suma) + ' | ' + '\tAverage number of students: ' + str(mean) + '</p>')
print('<hr>')
print("""<p> <a href="http://localhost:5556/index.html" > Return to main page. </a> </p>""")
print("""</body> </html>""")

db_connection.commit()
db_connection.close()

