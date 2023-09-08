CREATE OR REPLACE PROCEDURE UserAdd
  (
  username VARCHAR(50),
  password VARCHAR(30)
  )
LANGUAGE plpgsql
AS $$
 BEGIN
  INSERT INTO Users
    (
      Username,
      Password
    )
  VALUES
  (
    username,
    password
  );

END $$;
