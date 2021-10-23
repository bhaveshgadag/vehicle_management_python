from mysql.connector import Error
from conn_db import Database
from PyQt5 import QtGui, QtCore

from PyQt5.QtWidgets import *

import customer, ui.v_add_ui


class Vehicle:
    def __init__(self,  registration_no, company, model, v_type, transmission, customer_id, v_id=None):
        self.v_id = v_id
        self.reg_no = registration_no
        self.company = company
        self.model = model
        self.type = v_type
        self.transmission = transmission
        self.c_id = customer_id

    def add(self):
        conn = Database()
        sql = "INSERT INTO vehicle(registration_no,company,model,vehicle_type,transmission,customer_id) VALUES (%s," \
              "%s,%s,%s,%s,%s) "
        values = (self.reg_no, self.company, self.model, self.type, self.transmission, self.c_id)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()

    def veh_update(self):
        conn = Database()
        sql = "UPDATE vehicle " \
              "SET registration_no=%s,company=%s,model=%s,vehicle_type=%s,transmission=%s,customer_id=%s " \
              "WHERE vehicle_id=%s "
        values = (self.reg_no, self.company, self.model, self.type, self.transmission, self.c_id, self.v_id)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()

    @staticmethod
    def delete(vid):
        conn = Database()
        try:
            conn.cursor.execute("DELETE FROM vehicle WHERE vehicle_id = %s", (vid,))
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
            conn.cursor.execute("SELECT A.vehicle_id,A.registration_no,A.company,A.model,"
                                "A.vehicle_type,A.transmission,B.customer_name "
                                "from `vehicle` AS A "
                                "LEFT JOIN `customer` AS B "
                                "ON B.`customer_id` = A.`customer_id`")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def veh_search(v_id):
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM vehicle "
                                "WHERE vehicle_id=%s", (v_id,))
            result = conn.cursor.fetchone()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def search_by_cust(c_id):
        conn = Database()
        try:
            conn.cursor.execute("SELECT *FROM vehicle where customer_id = %s", (c_id,))
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()


class VehicleUI(QDialog, ui.v_add_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()
        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.rbt_v_auto)
        self.btn_group.addButton(self.rbt_v_manual)
        self.cust = customer.Customer.view_all()
        self.cust_name = [record [1] for record in self.cust]
        completer = QCompleter(self.cust_name, self.input_c_name)
        self.input_c_name.setCompleter(completer)
        self.reg_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}"))
        self.input_v_reg_no.setValidator(self.reg_validator)
        self.input_c_name.returnPressed.connect(lambda: self.set_text())
        self.bt_cancel.clicked.connect(self.close)

    def set_text(self):
        record = self.cust[self.cust_name.index(self.input_c_name.text())]
        self.input_v_contact.setText(str(record[3]))

    def veh_ui_add(self):
        print("add ui started")
        self.reg_no = self.input_v_reg_no.text()
        self.company = self.input_v_company.text()
        self.model = self.input_v_model.text()
        self.type = self.input_v_type.text()
        self.transmission = self.btn_group.checkedButton().text()
        print(self.transmission)
        self.record = []
        for i in self.cust:
            if str(i[3]) == self.input_v_contact.text():
                self.record = i
                break
##        veh_obj = Vehicle(self.reg_no, self.company, self.model, self.type, self.transmission, self.record[0])
##        veh_obj.add()
        self.close()

    def veh_ui_update(self):
        self.v_id = self.input_v_id.text()
        self.reg_no = self.input_v_reg_no.text()
        self.company = self.input_v_company.text()
        self.model = self.input_v_model.text()
        self.type = self.input_v_type.text()
        self.transmission = self.btn_group.checkedButton().text()
        print(self.v_id,self.reg_no,self.transmission)
        self.record = []
        for i in self.cust:
            if str(i[3]) == self.input_v_contact.text():
                self.record = i
                break
        veh_obj = Vehicle(self.reg_no, self.company, self.model, self.type, self.transmission, self.record[0],self.v_id)
        veh_obj.veh_update()
        self.close()
