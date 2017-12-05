# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:09:04 2017

@author: Binary
"""
import mysql.connector
 
#Doing our connection
connection_string = mysql.connector.connect( user='root',
               password='',
               host='127.0.0.1',
               database='CUBE')

def connect_to_database():
    try:
        cursor=connection_string.cursor()
        # Create a new record
            #sql_INSERT = "INSERT INTO dictionary (word, definition, synonyms, related_words) VALUES (%s, %s, %s, %s)"
        sql_select_all= ("SELECT word FROM dictionary")
        cursor.execute(sql_select_all)
        result=cursor.fetchall()
        print(list(result))
        
            

    # connection is not autocommit by default. So you must commit to save
    # your changes.
        connection_string.commit()

        '''with connection.cursor() as cursor:
        # Read a single record
            sql = "SELECT * FROM 'Dictionary' "
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)'''
    finally:
                connection_string.close()
    return (list(result))
