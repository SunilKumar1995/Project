# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:09:04 2017

@author: knewton
"""
import mysql.connector
 
#Doing our connection
connection_string = mysql.connector.connect( user='root',
               password='',
               host='127.0.0.1',
               database='CUBE')

def convert_to_string(database_list):

    print(database_list)
    str1 = ''.join(str(e) for e in database_list)
    str1=str1.replace('(','')
    str1=str1.replace('\'','')
    str1=str1.replace(')','')
    str1=str1.replace('\'','')
    str1=str1.replace(',',' ')
    str1=str1[:len(str1)-1]
    
    return str1

def convert_to_list(database_string):
    database_list=database_string.split(' ')
    return (database_list)
list1=[]
def connect_to_database():
    try:
        cursor=connection_string.cursor()
        # Create a new record
            #sql_INSERT = "INSERT INTO dictionary (word, definition, synonyms, related_words) VALUES (%s, %s, %s, %s)"
        sql_select_all= "SELECT word FROM dictionary"
        cursor.execute(sql_select_all)
        result=cursor.fetchall()  
        #for z in result:
         #   list1.append(z[0])
        #print(list1)
            
        result=convert_to_string(result)
        result=convert_to_list(result)
        print(result)
        
            

    # connection is not autocommit by default. So you must commit to save
    # your changes.
        #connection_string.commit()

        #with connection.cursor() as cursor:
        # Read a single record
        #sql = "SELECT synonyms FROM dictionary"
        #cursor.execute(sql)
        #result = cursor.fetchone()
        #print(result)
        
    finally:
        connection_string.close()

    
    return (result)

