import os

month = 12
day = 22
year = 2021

def dateStringCreater(currentMonth: int, currentDay: int, currentYear: int)->str:
    dateString = str(currentMonth) + '/' + str(currentDay) + '/' + str(currentYear)
    return dateString
print("_________________________")
print("| Welcome to The Forest |")
print("-------------------------")

print("\nHere you may buy and sell health and wellness items that are natural to return to our bodies most healthy state.")
print(f"\nTodays date is: {dateStringCreater(12, 22, 2021)}")

import os
import sys
import sqlite3
import flask

app = flask.Flask(__name__)


@app.route('/create', methods=['GET', 'POST'])
def create():  # URL: http://127.0.0.1:8001/create
    return flask.render_template('create.html')


@app.route('/form_submit', methods=['POST'])
def submit_form():
    first_name = flask.request.form['fname']
    last_name = flask.request.form['lname']
    emp_id = flask.request.form['id']
    position = flask.request.form['position']

    con = sqlite3.connect('data/company.db')
    cur = con.cursor()

    insertString = "(\'{}\', \'{}\', {}, \'{}\')".format(first_name, last_name, emp_id, position)
    cur.execute("INSERT INTO employees VALUES " + insertString)
    con.commit()
    con.close()

    return flask.render_template('create.html')


@app.route('/view', methods=['GET'])
def display_emp():
    id = flask.request.args.get('emp_id')
    db_dict = {}  # URL:http://127.0.0.1:8001/view?emp_id=12
    con = sqlite3.connect('data/company.db')
    cur = con.cursor()

    dataList = []
    emp_id = 0
    emp = cur.execute(f"SELECT * FROM employees WHERE id = {id}")
    for element in emp.fetchall():
        db_dict.update({element[2]: [element[0], element[1], element[3], element[2]]})
        dataList = db_dict[element[2]]
        emp_id = element[2]
    # print(db_dict)

    employee_id = flask.request.args.get('emp_id')
    # print(f"EMPID: {employee_id}")

    return flask.render_template('display_emp.html', data=dataList, emp_id=employee_id)


@app.route('/view/emp_id/<empid>', methods=['GET', 'POST'])
def display_emp_dynamic(empid):
    con = sqlite3.connect('data/company.db')
    cur = con.cursor()

    db_dict = {}
    dataList = []
    emp_id = 0
    emp = cur.execute(f"SELECT * FROM employees WHERE id = {empid}")
    for element in emp.fetchall():
        db_dict.update({element[2]: [element[0], element[1], element[3], element[2]]})
        dataList = db_dict[element[2]]
        emp_id = element[2]

    return flask.render_template('display_emp.html', data=dataList, emp_id=empid)


@app.route('/delete', methods=['POST'])
def del_emp():
    con = sqlite3.connect('data/company.db')
    cur = con.cursor()

    # employee_id = flask.request.form.get('emp_id')
    employee_id = flask.request.form.get('emp_id')
    print(f"EMPID: {employee_id}")
    # for row in cur.execute(f"SELECT * FROM employees WHERE id = {employee_id}"):
    # print(row)
    emp = cur.execute(f"DELETE FROM employees WHERE id = {employee_id}")
    con.commit()
    con.close

    dataList = [' ', ' ', ' ', ' ']
    return flask.render_template('display_emp.html', data=dataList)


@app.route('/view_all', methods=['GET'])
def display_all():
    con = sqlite3.connect('data/company.db')
    cur = con.cursor()

    employees = cur.execute("SELECT id, first_name, last_name, position FROM employees")

    db_dict = {}
    for employee in employees.fetchall():
        db_dict.update({employee[0]: [employee[1], employee[2], employee[3]]})

    return flask.render_template('viewAll.html', data=db_dict)


if __name__ == '__main__':
    con = sqlite3.connect('data/company.db')
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE if not exists employees (first_name text, last_name text, id integer primary key, position text)")
    con.commit()
    con.close()

    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)

