CREATE OR REPLACE FUNCTION UserAdd
  (
  pUsername VARCHAR(50),
  pPassword VARCHAR(30),
  OUT pUserID int
  )
LANGUAGE plpgsql
-- 2 dollar signs indicate the beginning of a SQL string
AS $$
  BEGIN
    INSERT INTO Users
      (
        Username,
        Password
      )
    VALUES
    (
      pUsername,
      pPassword
    )
  RETURNING UserID INTO pUserID;

END $$;
