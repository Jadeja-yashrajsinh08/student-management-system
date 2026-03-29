from connection import get_connection

def update_student():
    conn = get_connection()
    cursor = conn.cursor()

    id = int(input("Enter ID to update: "))

    name = input("New Name: ")
    age = int(input("New Age: "))
    course = input("New Course: ")

    m1 = int(input("Marks 1: "))
    m2 = int(input("Marks 2: "))
    m3 = int(input("Marks 3: "))

    total = m1 + m2 + m3
    percentage = total / 3

    cursor.execute("""
    UPDATE students
    SET name=?, age=?, course=?, marks1=?, marks2=?, marks3=?, total=?, percentage=?
    WHERE id=?
    """, (name, age, course, m1, m2, m3, total, percentage, id))

    conn.commit()
    conn.close()

    print("Updated successfully ✅")