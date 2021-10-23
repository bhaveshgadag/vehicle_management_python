from PyQt5 import QtGui, QtCore
from mysql.connector import Error
from PyQt5.QtWidgets import *
from conn_db import *

import ui.c_add_ui


class Customer:
    def __init__(self, name, address, contact, email, id=None):
        self.name = name
        self.contact = contact
        self.address = address
        self.email = email
        self.id = id

    def customer_add(self):
        conn = Database()
        sql = "INSERT INTO customer(customer_name,address,contact_no,email) VALUES (%s,%s,%s,%s)"
        values = (self.name, self.address, self.contact, self.email)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()

    def customer_update(self):
        conn = Database()
        sql = "UPDATE customer SET customer_name=%s, address=%s,contact_no=%s,email=%s WHERE customer_id=%s"
        values = (self.name, self.address, self.contact, self.email, self.id)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()

    @staticmethod
    def customer_delete(cust_id):
        conn = Database()
        try:
            conn.cursor.execute("DELETE FROM customer WHERE customer_id = %s", (cust_id,))
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()

    @staticmethod
    def view_all():
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM customer")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def search(s_id):
        conn = Database()
        try:
            conn.cursor.execute("SELECT c.customer_id,c.customer_name,c.address,c.contact_no,c.email"
                                "FROM customer c,vehicle v, service s"
                                "WHERE s.vehicle_id=v.vehicle_id"
                                "AND v.customer_id=c.customer_id"
                                "AND s.service_id=%s;", (s_id,))
            result = conn.cursor.fetchone()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()


class CustomerAddUI(QDialog, ui.c_add_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.bt_cancel.clicked.connect(self.close)
        self.show()
        self.name_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[a-zA-Z '.]+$"))
        self.contact_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{10}"))
        self.email_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[\w._+-%]{1,30}@[\w.-]{2,20}.[A-Za-z]{2,3}"))
        self.input_c_name.setValidator(self.name_validator)
        self.input_c_contact.setValidator(self.contact_validator)
        self.input_c_email.setValidator(self.email_validator)
        self.input_c_email.textChanged.connect(lambda: self.check_state())
        self.input_c_email.textChanged.emit(self.input_c_name.text())

    def cust_ui_add(self):
        print("add ui start")
        self.name = self.input_c_name.text()
        self.address = self.input_c_address.toPlainText()
        self.contact = self.input_c_contact.text()
        self.email = self.input_c_email.text()
        cust_obj = Customer(self.name, self.address, self.contact, self.email)
        cust_obj.customer_add()
        self.close()

    def cust_ui_update(self):
        self.id = self.input_c_id.text()
        self.name = self.input_c_name.text()
        self.address = self.input_c_address.toPlainText()
        self.contact = self.input_c_contact.text()
        self.email = self.input_c_email.text()
        cust_obj = Customer(self.name, self.address, self.contact, self.email, self.id)
        cust_obj.customer_update()
        self.close()

    def check_state(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if state == QtGui.QValidator.Acceptable:
            color = '#c4df9b'  # green
        elif state == QtGui.QValidator.Intermediate:
            color = '#fff79a'  # yellow
        else:
            color = '#f6989d'  # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)
