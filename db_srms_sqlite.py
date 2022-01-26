
import datetime
import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES |
                                                        sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS course (
                        course_id INTEGER NOT NULL PRIMARY KEY,
                        course_name TEXT NOT NULL,
                        course_code TEXT
                        );"""),
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS class (
                        class_id INTEGER NOT NULL PRIMARY KEY,
                        class_name TEXT NOT NULL
                        );"""),
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS student (
                        student_id INTEGER NOT NULL PRIMARY KEY,
                        student_first_name TEXT NOT NULL,
                        student_last_name TEXT NOT NULL,
                        gender TEXT NOT NULL,
                        class_name TEXT NOT NULL,
                        FOREIGN KEY (class_name) REFERENCES class (class_name)
                        );"""),
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS enrollment (
                        enrollment_id INTEGER NOT NULL PRIMARY KEY,
                        course_id INTEGER NOT NULL,
                        student_id INTEGER NOT NULL,
                        class_name TEXT,
                        date TEXT NOT NULL,
                        FOREIGN KEY (course_id) REFERENCES course (course_id),
                        FOREIGN KEY (course_id) REFERENCES student (student_id)
                        );"""),
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS attendance (
                        attendance_id INTEGER NOT NULL PRIMARY KEY,
                        course_id INTEGER NOT NULL,
                        student_id INTEGER NOT NULL,
                        date TEXT NOT NULL,
                        FOREIGN KEY (course_id) REFERENCES course (course_id),
                        FOREIGN KEY (course_id) REFERENCES student (student_id)
                        );"""),
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS assessment (
                        assessment_id INTEGER NOT NULL PRIMARY KEY,
                        course_id INTEGER NOT NULL,
                        student_id INTEGER NOT NULL,
                        assessment_type TEXT NOT NULL,
                        assessment_score INTEGER NOT NULL,
                        date TEXT NOT NULL,
                        FOREIGN KEY (course_id) REFERENCES course (course_id),
                        FOREIGN KEY (course_id) REFERENCES student (student_id)
                        );
                        """),
        self.conn.commit()

    # Course table
    def fetch_course(self):
        self.cur.execute("SELECT * FROM course")
        rows = self.cur.fetchall()
        return rows

    def insert_course(self, course_name, course_code):
        self.cur.execute("INSERT INTO course VALUES (NULL, ?, ?)", (course_name, course_code))
        self.conn.commit()

    def update_course(self, course_id, course_name, course_code):
        self.cur.execute("UPDATE course SET course_name = ?, course_code = ? WHERE course_id= ?", (course_name, course_code, course_id))
        self.conn.commit()

    # I suspect I will have to delete by course_name rather than course_id to be quicker. The current code suggests that the app will have to send fetch course query to obtain course name before knowing which course to delete.
    def remove_course(self, course_id):
        self.cur.execute("DELETE FROM course WHERE course_id= ?", (course_id,))
        self.conn.commit()
    
    # Class table    
    def fetch_class(self):
        self.cur.execute("SELECT * FROM class")
        rows = self.cur.fetchall()
        return rows
    
    def insert_class(self, class_name):
        self.cur.execute("INSERT INTO class VALUES (NULL, ?)", (class_name,))
        self.conn.commit()
        
    def update_class(self, class_id, class_name):
        self.cur.execute("UPDATE class SET class_name = ? WHERE class_id = ?", (class_name, class_id))
        self.conn.commit()
        
    def remove_class(self, class_id):
        self.cur.execute("DELETE FROM class WHERE class_id = ?", (class_id,))
        self.conn.commit()

    # Student table
    def fetch_students_in_course(self, course_name):
        # To account for cases where single teacher teaches multiple courses
        self.cur.execute("SELECT student.student_first_name, student.student_last_name FROM student JOIN enrollment ON student.student_id = enrollment.student_id JOIN course ON course.course_id = enrollment.course_id WHERE course.course_name=?", (course_name,))
        rows = self.cur.fetchall()
        return rows
    
    def fetch_students_in_class(self, class_name):
        self.cur.execute("SELECT student_first_name, student_last_name FROM student WHERE class_name=?", (class_name,))
        rows = self.cur.fetchall()
        return rows
    
    def fetch_student(self):
        self.cur.execute("SELECT * FROM student")
        rows = self.cur.fetchall()
        return rows

    def fetch_student_count_by_gender(self, gender):
        self.cur.execute("SELECT COUNT(student.student_id) FROM student WHERE student.gender = ?", (gender,))
        rows = self.cur.fetchall()
        return rows

    def insert_student(self, student_first_name, student_last_name, gender, class_name):
        self.cur.execute("INSERT INTO student VALUES (NULL, ?, ?, ?, ?)", (student_first_name, student_last_name, gender, class_name))
        self.conn.commit()

    def update_student(self, student_id, student_first_name, student_last_name, gender, class_name):
        self.cur.execute("UPDATE student SET student_first_name = ?, student_last_name = ?, gender = ?, class_name = ? WHERE student_id= ?", (student_first_name, student_last_name, gender, class_name, student_id))
        self.conn.commit()

    def remove_student(self, student_id):
        self.cur.execute("DELETE FROM student WHERE student_id=?", (student_id,))
        self.conn.commit()

    # Enrollment table
    def fetch_enrollment(self, course_id):
        self.cur.execute("SELECT student.student_first_name, student.student_last_name, enrollment.class_name, course.course_name, enrollment.date FROM student JOIN enrollment ON enrollment.student_id = student.student_id JOIN course ON enrollment.course_id = course.course_id WHERE course.course_id =?", (course_id,))
        rows = self.cur.fetchall()
        return rows
    
    def fetch_enrollments_grouped(self, course_id):
        # This query collates all the student enrollments into a class enrollment
        self.cur.execute("SELECT COUNT(student.student_id), enrollment.class_name, course.course_name FROM student JOIN enrollment ON enrollment.student_id = student.student_id JOIN course ON enrollment.course_id = course.course_id WHERE course.course_id = ? GROUP BY enrollment.class_name", (course_id,))
        rows = self.cur.fetchall()
        return rows
    
    def fetch_enrollments(self):
        self.cur.execute("SELECT student.student_first_name, student.student_last_name, enrollment.class_name, course.course_name, enrollment.date FROM student JOIN enrollment ON enrollment.student_id = student.student_id JOIN course ON enrollment.course_id = course.course_id")
        rows = self.cur.fetchall()
        return rows
   
    def insert_enrollment(self, course_id, student_id, class_name, date_time):
        self.cur.execute("INSERT INTO enrollment VALUES (NULL, ?, ?, ?, ?)", (course_id, student_id, class_name, date_time))
        self.conn.commit()

    # Attendance table
            # Attendance is analytics, I'll come back to it along with the other analytics reports. I suspect there will be more than one fetch queries
    def fetch_attendance(self, course_id, class_id):
        self.cur.execute("SELECT student.student_id, student.student_first_name, student.student_last_name, class.class_name, COUNT(attendance_id) FROM class JOIN student ON class.class_id = student.class_id JOIN attendance ON attendance.student_id = student.student_id WHERE attendance.course_id=? AND class.class_id =? GROUP BY student.student_id", (course_id, class_id))
        rows = self.cur.fetchall()
        return rows

        # Leaving the course_id and student_id entry as null with the assumption that secondary schools do not assign student or course ids. Database set to generate it automatically
    def insert_attendance(self, course_id, student_id, datetime):
        self.cur.execute("INSERT INTO attendance VALUES (NULL, ?, ?, ?)", (course_id, student_id, datetime))
        self.conn.commit()

    def remove_attendance(self, attendance_id):
        self.cur.execute("DELETE FROM attendance WHERE attendance.attendance_id=?", (attendance_id,))
        self.conn.commit()

    # Assessment table (For order, these fetch functions are grouped by student, class & course)
        # Student Analytics
    def fetch_assessments(self, student_id):
        # Pull all the different assessment records on a particular student
        self.cur.execute("SELECT student.student_first_name, student.student_last_name, class.class_name, course.course_name, assessment.assessment_type, assessment.assessment_score, assessment.date FROM class JOIN student ON class.class_id = student.class_id JOIN assessment ON assessment.student_id = student.student_id JOIN enrollment ON enrollment.student_id = student.student_id JOIN course on course.course_id = enrollment.course_id WHERE student.student_id=?", (student_id))
        rows = self.cur.fetchall()
        return rows

    def fetch_assessments_all_students(self): # Class An as well
        # Pull all the different assessment records on each student
        self.cur.execute("SELECT student.student_id, student.student_first_name, student.student_last_name, course.course_name, assessment.assessment_type, assessment.assessment_score, assessment.date FROM assessment JOIN student ON assessment.student_id = student.student_id JOIN enrollment ON enrollment.student_id = student.student_id JOIN course on course.course_id = enrollment.course_id GROUP BY student.student_id")
        rows = self.cur.fetchall()
        return rows

    def fetch_total_assessments_one_student(self, course_id, student_id): # Course An as well
        # Pull the total assessment score on a particular student
        self.cur.execute("SELECT student.student_id, student.student_first_name, student.student_last_name, course.course_name, SUM(assessment.assessment_score) FROM assessment JOIN student ON assessment.student_id = student.student_id JOIN enrollment ON enrollment.student_id = student.student_id JOIN course on course.course_id = enrollment.course_id WHERE student.student_id=? AND course.course_id=?", (student_id, course_id))
        rows = self.cur.fetchall()
        return rows

    def fetch_total_assessments_all_students_in_course(self, course_id): # Course An as well
        # Pull the total assessment score on each student
        self.cur.execute("SELECT student.student_id, student.student_first_name, student.student_last_name, course.course_name, SUM(assessment.assessment_score) FROM assessment JOIN student ON assessment.student_id = student.student_id JOIN enrollment ON enrollment.student_id = student.student_id JOIN course on course.course_id = enrollment.course_id WHERE course.course_id=? GROUP BY student.student_id", (course_id,))
        rows = self.cur.fetchall()
        return rows

        # Class Analytics
    def fetch_total_assessments_all_students_in_class(self, class_id):
        # Pull the total assessment score on each student
        self.cur.execute("SELECT student.student_id, student.student_first_name, student.student_last_name, class.class_id, course.course_name, SUM(assessment.assessment_score) FROM class JOIN student ON class.class_id = student.class_id JOIN assessment ON assessment.student_id = student.student_id JOIN enrollment ON enrollment.student_id = student.student_id JOIN course on course.course_id = enrollment.course_id WHERE class.class_id=? GROUP BY student.student_id", (class_id,))
        rows = self.cur.fetchall()
        return rows

        # Drill down on scores. Get a bit more granular with the analytics. Descriptive Statisitcs
    def fetch_class_avg_score_all_classes(self, course_name):
        self.cur.execute("WITH t1 AS (SELECT student.student_id, class.class_name, course.course_name, SUM (assessment_score) AS total_score FROM class JOIN student ON class.class_id = student.class_id JOIN assessment ON assessment.student_id = student.student_id JOIN enrollment ON enrollment.student_id = student.student_id JOIN course on course.course_id = enrollment.course_id WHERE course.course_name=? GROUP BY student.student_id) SELECT course.course_name, class.class_name, AVG (t1.total_score) GROUP BY class.class_name,", (course_name,))
        rows = self.cur.fetchall()
        return rows

        # Case where teacher teaches same course to multiple classes and wants to compare students' performances course-wide

        # Course Analytics
    def fetch_avg_score_by_assessment_type(self, course_id):
        self.cur.execute("SELECT assessment_type, AVG (assessment_score) FROM assessment GROUP BY assessment.type WHERE assessment.course_id=?", (course_id,))
        rows = self.cur.fetchall()
        return rows

    def fetch_min_score_by_assessment_type(self, course_id):
        self.cur.execute("SELECT assessment_type, MIN (assessment_score) FROM assessment WHERE assessment.course_id=? GROUP BY assessment.type", (course_id,))
        rows = self.cur.fetchall()
        return rows

    def fetch_max_score_by_assessment_type(self, course_id):
        self.cur.execute("SELECT assessment_type, MAX (assessment_score) FROM assessment WHERE assessment.course_id=? GROUP BY assessment.type", (course_id,))
        rows = self.cur.fetchall()
        return rows

        # Ideally should return 2 rows male and female with the respective average scores of each gender
    def fetch_avg_score_by_gender(self, course_id, gender):
        self.cur.execute("WITH t1 as (SELECT student.student_id, student.gender, SUM(assessment_score) AS total_score FROM assessment JOIN student ON assessment.student_id = student.student_id JOIN enrollment ON enrollment.student_id = student.student_id JOIN course on course.course_id = enrollment.course_id WHERE course.course_id = ? GROUP BY student.student_id) SELECT t1.gender, AVG (t1.total_score) FROM t1 GROUP BY t1.gender", (course_id,))
        rows = self.cur.fetchall()
        return rows

        # Leaving the course_id and student_id entry as null with the assumption that secondary schools do not assign student or course ids. Database set to generate it automatically
    def insert_assessment(self, course_id, student_id, assessment_type, assessment_score):
        self.cur.execute("INSERT INTO assessment VALUES (NULL, NULL, ?, ?, ?)", (course_id, student_id, assessment_type, assessment_score, datetime.datetime.now()))
        self.conn.commit()

    def update_assessment(self, assessment_id, assessment_type, assessment_score):
        self.cur.execute("UPDATE assessment SET assessment_type = ?, assessment_score = ? WHERE assessment.assessment_id= ?", (assessment_type, assessment_score, assessment_id))
        self.conn.commit()

    def remove_assessment(self, assessment_id):
        self.cur.execute("DELETE FROM assessment WHERE assessment.assessment_id=?", (assessment_id,))
        self.conn.commit()
    
    # Close connection with database
    def __del__(self):
        self.conn.close()

# Instantiate database
def main():
    db=Database('new_single_user3.db')
    
    # To add columns to db, add self.cur.execute functions here and run this program directly
    # Affected tables must have their insert and and update queries adjusted accordingly and select queries if necessary

if __name__ == '__main__':
    main()
