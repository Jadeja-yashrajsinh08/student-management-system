from connection import get_connection

def add_student():
    conn = get_connection()
    cursor = conn.cursor()

    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    m1 = int(input("Marks 1: "))
    m2 = int(input("Marks 2: "))
    m3 = int(input("Marks 3: "))

    total = m1 + m2 + m3
    percentage = total / 3

    cursor.execute("""
    INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (id, name, age, course, m1, m2, m3, total, percentage))

    conn.commit()
    conn.close()

    print("Student added successfully ✅")