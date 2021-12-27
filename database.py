import mysql.connector
from mysql.connector import Error
import pandas as pd
from obj import *

class dbtools:
	def connect(host_name, user_name, user_password, db_name):
	    connection = None
	    try:
	        connection = mysql.connector.connect(
	            host=host_name,
	            user=user_name,
	            passwd=user_password,
	            database=db_name
	        )
	        print("MySQL Database connection successful")
	    except Error as err:
	        print(f"Error: '{err}'")

	    return connection
	def execute(connection, query):
	    cursor = connection.cursor()
	    try:
	        cursor.execute(query)
	        connection.commit()
	        print("Query successful")
	    except Error as err:
	        print(f"Error: '{err}'")
	        
	def read(connection, query):
	    cursor = connection.cursor()
	    result = None
	    try:
	        cursor.execute(query)
	        result = cursor.fetchall()
	        return result
	    except Error as err:
	        print(f"Error: '{err}'")
	 