from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///week7_database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    estudent_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)

@app.route("/")
def index():
    students = Student.query.all()
    return render_template("index.html", students=students)

@app.route("/student/create", methods=["GET", "POST"])
def create_student():
    if request.method == "GET":
        return render_template("create_student.html")
    roll = request.form["roll"]
    f_name = request.form["f_name"]
    l_name = request.form["l_name"]
    if Student.query.filter_by(roll_number=roll).first():
        return render_template("exists_student.html")
    student = Student(roll_number=roll, first_name=f_name, last_name=l_name)
    db.session.add(student)
    db.session.commit()
    return redirect("/")

@app.route("/student/<int:student_id>/update", methods=["GET", "POST"])
def update_student(student_id):
    student = Student.query.get(student_id)
    courses = Course.query.all()
    if request.method == "GET":
        return render_template("update_student.html", student=student, courses=courses)
    student.first_name = request.form["f_name"]
    student.last_name = request.form["l_name"]
    selected_course_id = int(request.form["course"])
    db.session.add(Enrollment(estudent_id=student_id, ecourse_id=selected_course_id))
    db.session.commit()
    return redirect("/")

@app.route("/student/<int:student_id>/delete")
def delete_student(student_id):
    Enrollment.query.filter_by(estudent_id=student_id).delete()
    Student.query.filter_by(student_id=student_id).delete()
    db.session.commit()
    return redirect("/")

@app.route("/student/<int:student_id>")
def view_student(student_id):
    student = Student.query.get(student_id)
    enrollments = Enrollment.query.filter_by(estudent_id=student_id).all()
    course_ids = [e.ecourse_id for e in enrollments]
    courses = Course.query.filter(Course.course_id.in_(course_ids)).all() if course_ids else []
    return render_template("student_detail.html", student=student, courses=courses)

@app.route("/student/<int:student_id>/withdraw/<int:course_id>")
def withdraw_course(student_id, course_id):
    Enrollment.query.filter_by(estudent_id=student_id, ecourse_id=course_id).delete()
    db.session.commit()
    return redirect("/")

@app.route("/courses")
def course_home():
    courses = Course.query.all()
    return render_template("courses.html", courses=courses)

@app.route("/course/create", methods=["GET", "POST"])
def create_course():
    if request.method == "GET":
        return render_template("create_course.html")
    code = request.form["code"]
    name = request.form["c_name"]
    desc = request.form["desc"]
    if Course.query.filter_by(course_code=code).first():
        return render_template("exists_course.html")
    course = Course(course_code=code, course_name=name, course_description=desc)
    db.session.add(course)
    db.session.commit()
    return redirect("/courses")

@app.route("/course/<int:course_id>/update", methods=["GET", "POST"])
def update_course(course_id):
    course = Course.query.get(course_id)
    if request.method == "GET":
        return render_template("update_course.html", course=course)
    course.course_name = request.form["c_name"]
    course.course_description = request.form["desc"]
    db.session.commit()
    return redirect("/courses")

@app.route("/course/<int:course_id>/delete")
def delete_course(course_id):
    Enrollment.query.filter_by(ecourse_id=course_id).delete()
    Course.query.filter_by(course_id=course_id).delete()
    db.session.commit()
    return redirect("/")

@app.route("/course/<int:course_id>")
def view_course(course_id):
    course = Course.query.get(course_id)
    enrollments = Enrollment.query.filter_by(ecourse_id=course_id).all()
    student_ids = [e.estudent_id for e in enrollments]
    students = Student.query.filter(Student.student_id.in_(student_ids)).all() if student_ids else []
    return render_template("course_detail.html", course=course, students=students)

if __name__ == "__main__":
    app.run(debug=True)
