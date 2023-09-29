import os
import psycopg2
from config import config
from typing import Optional

db_dir = f"{os.getcwd()}/db"

class DBConnector:
  def __init__(self):
    pass

  def _connect(self):
    conn = None
    try:
      # read the connection parameters
      params = config(f"{db_dir}/database.ini")
      # connect to the PostgreSQL server
      conn = psycopg2.connect(**params)
      return conn
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)

  def _extract_row(self, cursor):
     return cursor.fetchone() if cursor.description is not None else None

  def _extract_resultset(self, cursor):
      return (cursor.fetchall()) if cursor.description is not None else None

  def _extract_resultsets(self, cursor):
    resultsets = []
    while cursor.description is not None:
        resultsets.append(cursor.fetchall())
        cursor.nextset()
    return resultsets

  def connectAndCall(self, procedure):
    try:
      conn = self._connect()
      cur = conn.cursor()
      cur.execute(procedure)
      row = self._extract_row(cur)
      cur.close()
      conn.commit()
      return row
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
    finally:
	    if conn is not None:
		    conn.close()
