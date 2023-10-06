#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#
def insertIntoTable(conn, name, code, nof_students):
    try:
        cursor = conn.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO Courses
                          (course_name, course_code, nof_students) 
                          VALUES (?, ?, ?);"""

        data_tuple = (name, code, nof_students)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        print("Python Variables inserted successfully into Courses table")


    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    
#

def main():
    database = "C:/Users/milos/Lisbon_classes/Computer Networks/CN2/test_courses.db" # db name with path 

    sql_create_courses_table = """ CREATE TABLE IF NOT EXISTS Courses (
                                        course_name STRING NOT NULL,
                                        course_code INTEGER PRIMARY KEY UNIQUE,
                                        nof_students INTEGER NOT NULL
                                    ); """


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create employees table
        create_table(conn, sql_create_courses_table)
        # insert values into database
        insertIntoTable(conn, 'Aprendizagem Automatica', '11157', '125')
        insertIntoTable(conn, 'Programacao Avancada para Ciencia', '12529', '45')
        insertIntoTable(conn, 'Recuperacao de Informacao', '12077', '150')
        insertIntoTable(conn, 'Sistemas para Processamento de Big Data', '12078', '89')
        conn.close()
        
    else:
        print("Error! cannot create the database connection.")
    

if __name__ == '__main__':
    main()