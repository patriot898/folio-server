import os

db_dir = f"{os.getcwd()}/db"
directories = {
	'tables': f"{db_dir}/src/tables",
	'procs': f"{db_dir}/src/procs"
}

def deploy_directory(cursor, directory: str):
	""" create tables in the PostgreSQL database"""
	target_directory = directories[directory]
	files = [f"{target_directory}/{file}" for file in os.listdir(target_directory)]
	for file in files:
		cursor.execute(open(file, "r").read())
