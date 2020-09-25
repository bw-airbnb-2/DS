# import some libraries
#import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from fastapi import APIRouter

import pandas as pd
import numpy as np


df = pd.read_csv("https://raw.githubusercontent.com/bw-airbnb-2/DS/master/airbnb.csv", index_col=0)
print(df.shape)
print(df.head())
print(df.columns)
DB_NAME = 'onqmgnvx'
DB_USER = 'onqmgnvx'
DB_PASSWORD = 'DXqGX7cJBPZnoIs--boAioJLHlbKVGIu'
DB_HOST = 'lallah.db.elephantsql.com'

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host = DB_HOST)
                   
print("connection:", conn)
cur = conn.cursor()
print("cursor:", cur)

cur.execute('''CREATE TABLE IF NOT EXISTS airbnb_table(Zipcode int,
 Square_Feet decimal, 
 Bedrooms decimal,
 Bathrooms decimal,
 Review_Scores decimal,
 Accommodates decimal,	
 Cleaning_Fee decimal,
 Free_Parking decimal,
 Wireless_Internet decimal, 
 Cable_TV decimal,
 Prop_encoded decimal,
 cancel_encoded decimal,
 Price decimal
  );''')

cur.execute("SELECT * from airbnb_table;")

result_query = cur.fetchall()
print("result_query:",result_query)

cur.close()
conn.commit()
#conn.close()
cur = conn.cursor()
# for loop to insert the whole table
for index, row in df.iterrows():
    cur.execute(f'''INSERT INTO airbnb_table(Zipcode, Square_Feet, Bedrooms, Bathrooms, Review_Scores, Accommodates, Cleaning_Fee, Free_Parking, Wireless_Internet, Cable_TV, Prop_encoded, cancel_encoded, Price)
VALUES 
( 
  {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}
)
    ''')
    cur.close()
    conn.commit()
    #conn.close()
    cur = conn.cursor()  
    print(index)
conn.commit()    
cur.close()
conn.close()

# create the database with sqlite
SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# make the connection with sqlite
# create a function to return a base 
# Later we will inherit from this class to create each of the database models or classes
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()