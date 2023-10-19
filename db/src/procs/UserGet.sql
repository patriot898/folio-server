CREATE OR REPLACE FUNCTION UserGet
  (
    pUsername VARCHAR(50),
    pPassword VARCHAR(50)
  )
RETURNS TABLE (user_id integer, user_name VARCHAR(50), user_password VARCHAR(50)) AS $$
BEGIN
    RETURN QUERY
    SELECT u.UserID, u.Username, u.Password
    FROM Users u
    WHERE u.Username = pUsername AND u.Password = pPassword;
END;
$$ LANGUAGE plpgsql;
