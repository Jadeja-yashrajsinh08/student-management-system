import mysql.connector

# connect to MySQL
conn = mysql.connector.connect(
    host="localhost",   # or "127.0.0.1"
    user="root",
    password="",
    database="t20worldcup2026" # XAMPP default
)

# check connection
if conn.is_connected():
    print("Connected to MySQL successfully ✅")

# close connection
conn.close()