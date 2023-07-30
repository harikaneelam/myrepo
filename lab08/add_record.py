#!/usr/bin/env python3
# Turn on debug mode
import cgitb
import cgi
cgitb.enable()

import pymysql
# Database connection 
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "password"
DB_NAME = "student_db"

my_con=pymysql.connect(
    db='student_db',
    user = 'root',
    passwd = 'password',
    host = 'localhost'
)
c = my_con.cursor()

def calculate_average(midterm1, midterm2, final):
    return (midterm1 + midterm2 + 2 * final) / 4

def main():
    print("Content-type: text/html\n")

    form = cgi.FieldStorage()
    name = form.getvalue("fullname")
    midterm1 = int(form.getvalue("midterm1"))
    midterm2 = int(form.getvalue("midterm2"))
    final = int(form.getvalue("final_exam"))

    average = calculate_average(midterm1, midterm2, final)

    try:
        query = f"INSERT INTO student_grades (fullname, midterm_exam_1, midterm_exam_2, final_exam) VALUES ('{name}', {midterm1}, {midterm2}, {final})"
        c.execute(query)

        my_con.commit()
        my_con.close()

        print("<h2>Record Added Successfully</h2>")

    except Exception as e:
        print(f"<h2>Error occurred: {e}</h2>")

if __name__ == "__main__":
    main()
