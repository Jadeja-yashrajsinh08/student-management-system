# Student Management System

This is a simple student management web application built using Flask and SQLite.
The main goal of this project was to understand how backend, frontend, and database work together in a real application.

---

## About the Project

In this project, I created a system where users can manage student data easily.
It includes features like adding new students, updating their details, deleting records, and searching quickly.

I also implemented a login system so that only authorized users can access the dashboard.

---

## Features

* User registration and login
* Add new student details
* Update existing records
* Delete students
* Search functionality
* Automatic calculation of total and percentage
* Pagination for better data handling

---

## Tech Stack

* Python (Flask)
* SQLite
* HTML, CSS
* Werkzeug (for password hashing)

---

## How it Works

The application follows a simple flow:

* User interacts with the browser
* Flask handles the request
* Data is stored/retrieved from SQLite database
* Results are displayed back to the user

---

## Project Structure

```
app.py
templates/
static/
.gitignore
```

---

## How to Run

1. Clone the repository
2. Open the project folder
3. Install Flask:

```
pip install flask
```

4. Run the application:

```
python app.py
```

5. Open in browser:

```
http://127.0.0.1:5000/
```

---

## What I Learned

While building this project, I understood:

* How Flask handles routing and requests
* How to connect Python with a database
* Basics of authentication and session handling
* How frontend and backend communicate

---

## Future Improvements

* Improve UI design
* Add role-based access (admin/user)
* Export data functionality
* Use a more advanced database like MySQL

---

## Author

Yashrajsinh Jadeja
