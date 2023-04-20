# Importing the main class
from pathlib import Path
import sqlite3
import pandas as pd
from confidential.confidential import directory, raw_directory

# Creating a Path object to create a new sqlite file
Path(directory).touch()

# Creating a new database and opening a database connection to allow sqlite3 to work with it. Implicitly create the database if it does not exist.
con = sqlite3.connect(directory)

# Creating a database cursor to enable execution of SQL statements and SQL queries
cur = con.cursor()

# Creating a database table
cur.execute('DROP TABLE IF EXISTS titanic_data')
cur.execute( '''CREATE TABLE titanic_data 
              (pclass int, 
               survived int, 
               name text, 
               sex text, 
               age double, 
               sibsp int, 
               parch int, 
               ticket int,
               fare double,
               cabin text,
               embarked text,
               boat int,
               body double,
               PRIMARY KEY (Name, ticket)) ''' )

# Import the csv data
df = pd.read_csv(raw_directory)

# Write data written in a DataFrame to sqlite
df.to_sql('titanic_data', con, if_exists='replace')

cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
