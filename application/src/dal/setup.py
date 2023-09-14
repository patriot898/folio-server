import os
import psycopg2
from config import config


db_dir = f"{os.getcwd()}/db"
directories = {
	'tables': f"{db_dir}/src/tables",
	'procs': f"{db_dir}/src/procs"
}

def deploy_directory(directory: str):
	""" create tables in the PostgreSQL database"""
	target_directory = directories[directory]
	files = [f"{target_directory}/{file}" for file in os.listdir(target_directory)]
	conn = None
	try:
		# read the connection parameters
		params = config(f"{db_dir}/database.ini")
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
	deploy_directory('tables')
	deploy_directory('procs')
