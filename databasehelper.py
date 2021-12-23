import os
import sys
import sqlite3

sys.path.append(".")


def insertStudent(student1: Student):
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()
    cur.execute(f"SELECT id FROM students WHERE id = {student1.studentID};")
    data = cur.fetchall()
    if len(data):
        raise KeyError(f"Student ID: {student1.studentID}, already exisits in the students table")
    else:
        insertString = '(\'{}\', \'{}\', {}, \'{}\')'.format(student1.firstName, student1.lastName, student1.studentID,
                                                             student1.emailID)
        cur.execute("INSERT INTO students VALUES " + insertString)
        con.commit()

    con.close()


def getStudentsByName(lastname: str):
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM students WHERE last_name=:lname;", {"lname": lastname})
    data = cur.fetchall()
    if len(data):
        return data
    else:
        return (f"No students have the last name: {lastname}")


def updateID(student1: Student, ID: int):
    con = sqlite3.connect('data/database.db')
    cur = con.cursor()
    cur.execute(f"SELECT id FROM students WHERE id = {ID};")
    data = cur.fetchall()
    if len(data):
        raise KeyError(f"Student ID: {ID}, already exisits in the students table")
    else:
        insertString = '(\'{}\', \'{}\', {}, \'{}\')'.format(student1.firstName, student1.lastName, student1.studentID,
                                                             student1.emailID)
        cur.execute(f"UPDATE students SET id = {ID} WHERE id = {student1.studentID};")
        con.commit()

    con.close()


if __name__ == "__main__":
    print("Database Helper")
    s1 = Student('Nathan', 'Puch', 1234)
    s2 = Student('Caroline', 'Puch', 4321)
    s3 = Student('Mathew', 'Clary', 1235)
    s4 = Student('Dean', 'DalSanto', 1236)

    con = sqlite3.connect('data/database.db')
    cur = con.cursor()

    # Create table
    cur.execute(
        "CREATE TABLE if not exists students (first_name text, last_name text, id integer primary key, email text)")
    con.commit()
    con.close()

    # insertStudent(s1)
    # insertStudent(s2)
    # insertStudent(s3)
    # insertStudent(s4)

    print(getStudentsByName('Puch'))
    print(getStudentsByName('Smith'))

    updateID(s1, '6234')
