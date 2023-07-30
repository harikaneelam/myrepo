#!/usr/bin/env python3
#Turn on debug mode
import  cgitb
cgitb.enable()

import  pymysql
# Connect to the database
my_con=pymysql.connect(
    db='student_db',
    user = 'root',
    passwd = 'password',
    host = 'localhost'
)
c = my_con.cursor()
# Fetch all records from the database
sql = "SELECT fullname, (midterm_exam_1 + midterm_exam_2 + 2 * final_exam) / 4 AS average_score FROM student_grades"
c.execute(sql)
records = c.fetchall()


# Print HTML content
print("Content-type: text/html\n")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("    <title>Student Records</title>")
print("</head>")
print("<body>")
print("    <h1>Student Records</h1>")
print("    <table>")
print("        <tr>")
print("            <th>Fullname</th>")
print("            <th>Average Score</th>")
print("        </tr>")
for record in records:
    fullname, average_score = record
    print("        <tr>")
    print(f"            <td>{fullname}</td>")
    print(f"            <td>{average_score:.2f}</td>")
    print("        </tr>")
print("    </table>")
print("    <br>")
print('    <a href="student.html">Back to Main Page</a>')
print("</body>")
print("</html>")
