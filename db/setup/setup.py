import os
import psycopg2
from config import config


def create_tables():
	""" create tables in the PostgreSQL database"""
	db_dir = f"{os.getcwd()}/db"
	table_dir = f"{db_dir}/src/tables"
	files = [f"{table_dir}/{file}" for file in os.listdir(table_dir)]
	conn = None
	try:
		# read the connection parameters
		params = config(f"{db_dir}/setup/database.ini")
		# connect to the PostgreSQL server
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		# create table one by one
		for file in files:
			cur.execute(open(file, "r").read())
		# close communication with the PostgreSQL database server
		cur.close()
		# commit the changes
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


if __name__ == '__main__':
	create_tables()
