def user_add(connector, username: str, password: str):
  row = connector.connectAndCall(f"SELECT useradd('{username}', '{password}');")
  print(row)


def user_get(connector, username: str, password: str):
  row = connector.connectAndCall(f"SELECT userget('{username}', '{password}');")
  print(row[0])
