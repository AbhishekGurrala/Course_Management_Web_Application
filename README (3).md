# Student–Course Management Web Application

A Flask-based web application for managing students, courses, and enrollments with full Create, Read, Update, and Delete (CRUD) functionality.  
Built as part of the BSCCS2003 Application Development course (Week-7 Lab Assignment).

---

## Features

- **Student Management** – Add, view, update, and delete student records.
- **Course Management** – Add, view, update, and delete course records.
- **Enrollment Management** – Assign courses to students, view enrollment details, and withdraw from courses.
- **Relational Data Display** – Cross-linked student–course pages for easy navigation.
- **Validation** – Prevents duplicate roll numbers or course codes with appropriate feedback.
- **Responsive Templates** – HTML5 and Jinja2-based dynamic pages.

---

## Tech Stack

- **Backend:** Python 3, Flask, Flask-SQLAlchemy
- **Frontend:** HTML5, CSS, Jinja2 Templates
- **Database:** SQLite3

---

## Project Structure

```
.
├── app.py                # Main Flask application
├── templates/            # HTML templates
│   ├── index.html
│   ├── student_form.html
│   ├── course_form.html
│   ├── student_detail.html
│   ├── course_detail.html
│   └── ...
├── static/               # CSS, images (if any)
└── week7_database.sqlite3 # SQLite database (not included in submission)
```

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000/`

---

## Usage

- **Home Page:** View all students, add new students, update/delete records, and navigate to course management.
- **Courses Page:** View all courses, add new courses, update/delete records, and navigate to student management.
- **Enrollment:** Assign courses to students and withdraw as needed.
- **Detail Views:** Click on roll number or course code to view associated details.

---

## Screenshots

*(You can add screenshots of the UI here for better visualization)*

---

## License

This project is developed for academic purposes as part of the BSCCS2003 course assignment.
