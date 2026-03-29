from flask import Flask, render_template, request, redirect,session
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
app.secret_key="secret123"


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # hash password
        hashed_password = generate_password_hash(password)

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )
            conn.commit()
            conn.close()
            return redirect("/login")
        except:
            conn.close()
            return "User already exists ❌"

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):
            session["user"] = user[1]
            return redirect("/")
        else:
            return "Invalid username or password ❌"

    return render_template("login.html")


def get_connection():
    return sqlite3.connect("students.db")


@app.route("/")
def index():
    if "user" not in session :
        return redirect("/login")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return render_template("index.html", students=data, user=session["user"])


@app.route("/add", methods=["GET", "POST"])
def add():
    if "user" not in session :
        return redirect("/login")
    
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        m1 = int(request.form["m1"])
        m2 = int(request.form["m2"])
        m3 = int(request.form["m3"])

        total = m1 + m2 + m3
        percentage =total / 3

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students (name, age, course, marks1, marks2, marks3, total, percentage)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, age, course, m1, m2, m3, total, percentage))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if "user" not in session :
        return redirect("/login")
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        m1 = int(request.form["m1"])
        m2 = int(request.form["m2"])
        m3 = int(request.form["m3"])

        total = m1 + m2 + m3
        percentage = total / 3

        cursor.execute("""
        UPDATE students
        SET name=?, age=?, course=?, marks1=?, marks2=?, marks3=?, total=?, percentage=?
        WHERE id=?
        """, (name, age, course, m1, m2, m3, total, percentage, id))

        conn.commit()
        conn.close()

        return redirect("/")

    # GET request (fetch existing data)
    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cursor.fetchone()
    conn.close()

    return render_template("edit.html", s=student)

@app.route("/delete/<int:id>")
def delete(id):
    if "user" not in session :
        return redirect("/login")
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/search")
def search():
    if "user" not in session :
        return redirect("/login")
    query = request.args.get("query")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM students
    WHERE name LIKE ? OR id LIKE ?
    """, ('%' + query + '%', '%' + query + '%'))

    data = cursor.fetchall()
    conn.close()

    return render_template("index.html", students=data)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

def show_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    print("Users Table Data 👇")
    for user in users:
        print(user)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        course TEXT,
        marks1 INTEGER,
        marks2 INTEGER,
        marks3 INTEGER,
        total INTEGER,
        percentage REAL
    )
    """)

    # users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()



# def insert_admin():
#     conn=get_connection()
#     cursor=conn.cursor()

#     password=generate_password_hash("ykjadeja")


#     try:
#         cursor.execute("INSERT INTO users (username,password) VALUES (?, ?)",("admin",password))
#         conn.commit()
#         print("Admin created successfully")
#     except:
#         print("Admin already exist")
#     conn.close()

if __name__ == "__main__":
    create_tables()
    # show_users()
    app.run(debug=True)

