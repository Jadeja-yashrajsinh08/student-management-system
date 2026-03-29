# from connection import get_connection

# def view_students():
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM students")
#     data = cursor.fetchall()

#     print("\nID | Name | Age | Course | Total | %")
#     print("-------------------------------------")

#     for row in data:
#         print(row[0], row[1], row[2], row[3], row[7], round(row[8], 2))

#     conn.close()