import os
import psycopg2
from config import config

db_dir = f"{os.getcwd()}/db"

class DBConnector:
  def __init__(self):
    pass

  def __connect(self):
    conn = None
    try:
      # read the connection parameters
      params = config(f"{db_dir}/database.ini")
      # connect to the PostgreSQL server
      conn = psycopg2.connect(**params)
      return conn
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)

  def connectAndCall(self, procedure, **params):
    try:
      conn = self.__connect()
      cur = conn.cursor()
      procedure(cur, **params)
      cur.close()
      conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
    finally:
	    if conn is not None:
		    conn.close()
