import os
import psycopg2
from config import config

db_dir = f"{os.getcwd()}/db"
directories = {
	'tables': f"{db_dir}/src/tables",
	'procs': f"{db_dir}/src/procs"
}

class DBConnector:
  def __init__(self):
    pass

  connection = None
  cursor = None

  def _connect(self):
    try:
      # read the connection parameters
      params = config(f"{db_dir}/database.ini")
      # connect to the PostgreSQL server
      self.connection = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)

  def close_connection(self):
    if self.connection is not None:
      self.connection.close()
      self.connection = None

  def close_cursor(self):
    if self.cursor is not None:
      self.cursor.close()
      self.cursor = None

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

  def deploy_directory(self, directory: str):
    """ create tables in the PostgreSQL database"""
    target_directory = directories[directory]
    files = [f"{target_directory}/{file}" for file in os.listdir(target_directory)]
    self._connect()
    self.get_cursor()
    for file in files:
      self.cursor.execute(open(file, "r").read())
    self.close_cursor()
    self.connection.commit()
    self.close_connection()

  def get_cursor(self):
     self.cursor = self.connection.cursor()

  def connectAndCall(self, procedure):
    try:
      self._connect()
      self.get_cursor()
      self.cursor.execute(procedure)
      row = self._extract_row(self.cursor)
      self.close_cursor()
      self.connection.commit()
      return row
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
    finally:
	    self.close_connection()
