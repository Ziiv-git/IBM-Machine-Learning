#sql data imports
import sqlite3 as sqlite3
import pandas as pd
#initialise path to sqlite databse
path = 'data/classic_rock.db'
#create connection to sql database
con = sq3.Connection(path)
#write query
query = ''' SELECT * FROM rock_songs;'''
#execute query
data = pd.read_sql(query, con)



 #reading from nosql database (unstructured databse)
 #imports
 from pymongo import MongoClient
 #creste Connection
 con = MongoClient()
 #choose database
 db = con.database_name #display available databases
 #create a cursor object using a query
 cursor = db.collection_name.find(query)
 #expand cursor and construct dataframe
 df = pd.DataFrame(list(cursor))


 #api
 data_url = ''
 df = pd.read_csv(data_url, header=None)
