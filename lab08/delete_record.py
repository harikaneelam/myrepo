#!/usr/bin/env python3
# Turn on debug mode
import cgitb
import cgi
cgitb.enable()

import pymysql

# Connect to the database (Update the credentials)
my_con = pymysql.connect(
    db='student_db',
    user='root',
    passwd='password',
    host='localhost'
)
c = my_con.cursor()

form = cgi.FieldStorage()
fullname = form.getvalue('fullname')

   
try:
    # Check if the record exists in the database
    check_sql = 'SELECT COUNT(*) FROM student_grades WHERE fullname = %s'
    c.execute(check_sql, (fullname,))
    record_count = c.fetchone()[0]

    if record_count > 0:
        # Delete the record from the database
        delete_sql = 'DELETE FROM student_grades WHERE fullname = %s'
        c.execute(delete_sql, (fullname,))
        my_con.commit()

        print("Content-Type: text/html")
        print()
        print(f"Record with fullname '{fullname}' deleted successfully.")
    else:
        print("Content-Type: text/html")
        print()
        print("No record found.")
except pymysql.Error as e:
    print("Content-Type: text/html")
    print()
    print(f"Error deleting the record: {e}")
