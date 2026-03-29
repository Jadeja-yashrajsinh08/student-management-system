from connection import get_connection

def delete_student():
    conn = get_connection()
    cursor = conn.cursor()

    id = int(input("Enter ID to delete: "))

    cursor.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()
    conn.close()

    print("Deleted successfully ✅")