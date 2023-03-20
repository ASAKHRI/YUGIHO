#import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database="diabetes",
    user="root",
    password="root" )

cursor = conn.cursor()
cursor.execute("SELECT * FROM diabetes")

for row in cursor:
    print(row)
