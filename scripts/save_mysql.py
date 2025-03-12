import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# Establishing the connection using SQLAlchemy
engine = create_engine("mysql+mysqlconnector://root:@localhost/Sport_Db")

# Creating a cursor object using the connection
conn = engine.raw_connection()

# Check connection
if conn:
    print("Good")
else:
    print("Conn Problem")

# Creating the table in MySQL (only if it does not exist)
create_table_query = """
CREATE TABLE IF NOT EXISTS players (
     id INT AUTO_INCREMENT PRIMARY KEY,
     player_name VARCHAR(100) NOT NULL,
     sport VARCHAR(50) NOT NULL,
     team VARCHAR(50) NOT NULL,
     games_played INT,
     goals INT,
     assists INT,
     matches_won INT,
     points INT
);
"""

# Creating the table using the cursor
cursor = conn.cursor()
cursor.execute(create_table_query)
conn.commit()

# Loading the transformed data into a DataFrame
df = pd.read_csv(r"C:\Users\P15\Desktop\ETL\data\transformed_data.csv")

# Saving DataFrame to the MySQL database
df.to_sql("players", con=engine, if_exists="replace", index=False)

# Close the connection
conn.close()
