def user_add(cursor, username: str, password: str):
  cursor.execute("CALL useradd(%s, %s);", (username, password))
