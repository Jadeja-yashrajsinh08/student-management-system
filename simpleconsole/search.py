from connection import get_connection

def search_student():
    conn = get_connection()
    cursor = conn.cursor()

    id = int(input("Enter ID to search: "))

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    data = cursor.fetchone()

    if data:
        print("\nStudent Found:", data)
    else:
        print("Student not found ❌")

    conn.close()