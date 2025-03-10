import mysql.connector
import pandas as pd


#Establishing the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Sport_Db"      
)

if conn:
    print("Good")
else:
    print("Conn Problem")

#Creating a cursor object using the connection
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS players (
     id INT AUTO_INCREMENT PRIMARY KEY,
     player_name VARCHAR(100) NOT NULL,
     Sport VARCHAR(50) NOT NULL,
     team VARCHAR(50) NOT NULL,
     games_played INT,
     goals INT,
     assists INT,
     matches_won INT,
     points INT

);
"""

cursor.execute(create_table_query)
conn.commit()
