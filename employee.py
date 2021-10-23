from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from conn_db import *

import ui.e_add_ui


class Employee:
    def __init__(self, name, address, contect_no, date, salary, e_id=None):
        self.id = e_id
        self.name = name
        self.address = address
        self.contact_no = contect_no
        self.date = date
        self.salary = salary

    def emp_add(self):
        conn = Database()
        sql = "INSERT INTO employee(employee_name, employee_address, " \
              "employee_contact_no, date_of_joining, salary) " \
              "VALUES (%s, %s, %s, %s, %s)"
        values = (self.name, self.address, self.contact_no, self.date, self.salary)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()

    @staticmethod
    def emp_delete(emp_id):
        conn = Database()
        try:
            conn.cursor.execute("DELETE FROM customer WHERE customer_id = %s", (emp_id,))
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e, "rollback")
        finally:
            conn.close()


    @staticmethod
    def view_all():
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM employee")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()


class EmployeeAddUI(QDialog, ui.e_add_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.bt_cancel.clicked.connect(self.close)
        self.name_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[a-zA-Z '.]+$"))
        self.contact_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{10}"))
        self.input_emp_name.setValidator(self.name_validator)
        self.input_emp_contact.setValidator(self.contact_validator)
        self.dateEdit_doj.setDate(QDate.currentDate())
        print("ui done")
        self.show()

    def emp_ui_add(self):
        print("add ui start")
        name = self.input_emp_name.text()
        address = self.input_emp_address.toPlainText()
        contact = self.input_emp_contact.text()
        date = self.dateEdit_doj.text()
        salary = self.input_emp_salary.text()
        print(name, address, contact, date, salary)
        emp_obj = Employee(name, address, contact, date, salary)
        emp_obj.emp_add()
        self.close()


