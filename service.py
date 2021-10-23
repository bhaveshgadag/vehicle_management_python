from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate

from conn_db import *
from ui import s_add_ui, bill_ui
import customer, vehicle, employee, parts, invoicedemo


class Service:
    def __init__(self, description, date, distance, damages, vehicle_id, employee_id, total_price=0.0, service_id=None):
        self.s_id = service_id
        self.desc = description
        self.date = date
        self.distance = distance
        self.damages = damages
        self.total_price = total_price
        self.veh_id = vehicle_id
        self.emp_id = employee_id

    def service_add(self):
        conn = Database()
        sql = "INSERT INTO service(description,service_date,distance,damages,total_price,vehicle_id,employee_id) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (self.desc, self.date, self.distance, self.damages, self.total_price, self.veh_id, self.emp_id)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()

    def service_update(self):
        conn = Database()
        sql = "UPDATE  service " \
              "SET description=%s, service_date=%s, distance=%s, damages=%s, vehicle_id=%s, employee_id=%s " \
              "WHERE service_id=%s"
        values = (self.desc, self.date, self.distance, self.damages, self.veh_id, self.emp_id, self.s_id)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()

    @staticmethod
    def service_delete(ser_id):
        conn = Database()
        try:
            conn.cursor.execute("DELETE FROM service WHERE service_id = %s", (ser_id,))
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()

    @staticmethod
    def service_price_update(s_id, total_price):
        conn = Database()
        sql = "UPDATE service SET total_price = %s WHERE service_id=%s"
        values = (total_price, s_id)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()


    @staticmethod
    def service_view():
        conn = Database()
        try:
            conn.cursor.execute("SELECT s.service_id, s.description,s.service_date,s.total_price, "
                                "v.registration_no, c.customer_name,e.employee_name "
                                "FROM service s, vehicle v, customer c, employee e "
                                "WHERE s.vehicle_id=v.vehicle_id "
                                "AND v.customer_id=c.customer_id "
                                "AND s.employee_id=e.employee_id "
                                "ORDER BY s.service_date DESC;")
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def service_search(s_id):
        conn = Database()
        try:
            conn.cursor.execute("SELECT * FROM service "
                                "WHERE service_id=%s", (s_id,))
            result = conn.cursor.fetchone()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def service_cust_search(s_id):
        conn = Database()
        try:
            conn.cursor.execute("SELECT c.customer_id,c.customer_name,c.address,c.contact_no,c.email "
                                "FROM customer c,vehicle v, service s "
                                "WHERE s.vehicle_id=v.vehicle_id "
                                "AND v.customer_id=c.customer_id "
                                "AND s.service_id=%s;", (s_id,))
            result = conn.cursor.fetchone()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def service_vehicle_search(s_id):
        conn = Database()
        try:
            conn.cursor.execute("SELECT v.vehicle_id,v.registration_no,v.company,v.model,v.vehicle_type "
                                "FROM vehicle v,service s "
                                "WHERE s.vehicle_id=v.vehicle_id "
                                "AND s.service_id=%s", (s_id,))
            return conn.cursor.fetchone()
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def service_employee_search(s_id):
        conn = Database()
        try:
            conn.cursor.execute("SELECT e.employee_name,e.employee_contact_no "
                                "FROM employee e,service s "
                                "WHERE s.employee_id=e.employee_id "
                                "AND s.service_id=%s", (s_id,))
            return conn.cursor.fetchone()
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def add_part_used(s_id, p_id, qty):
        conn = Database()
        sql = "INSERT INTO parts_used(Service_service_id,Parts_part_id,quantity)" \
              "values(%s,%s,%s)"
        values = (s_id, p_id, qty)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()

    @staticmethod
    def parts_used_view(s_id):
        conn = Database()
        sql = "SELECT pu.Parts_part_id,p.part_name,p.part_price,pu.quantity,(p.part_price*pu.quantity) Amount " \
              "FROM parts_used pu ,parts p ,service s " \
              "WHERE pu.Parts_part_id=p.part_id " \
              "AND pu.Service_service_id=s.service_id " \
              "AND s.service_id=%s"
        values = (s_id,)
        try:
            conn.cursor.execute(sql, values)
            result = conn.cursor.fetchall()
            return result
        except Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def parts_used_del(s_id, p_id):
        conn = Database()
        sql = "DELETE FROM parts_used WHERE Service_service_id=%s AND Parts_part_id=%s"
        values = (s_id, p_id)
        try:
            conn.cursor.execute(sql, values)
            conn.connection.commit()
        except Error as e:
            conn.connection.rollback()
            print(e)
        finally:
            conn.close()


class ServiceAddUI(QDialog, s_add_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.bt_cancel.clicked.connect(self.close)
        self.veh = []
        self.cust = customer.Customer.view_all()
        self.c_name = [record[1] for record in self.cust]
        self.completer = QCompleter(self.c_name, self.input_c_name)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.input_c_name.setCompleter(self.completer)
        self.input_c_name.returnPressed.connect(self.set_text_customer)
        self.dateEdit_s_date.setDate(QDate.currentDate())
        self.emp = employee.Employee.view_all()
        for record in self.emp:
            self.comboBox_advisor.addItem(record[1])
        self.comboBox_reg_no.activated[int].connect(self.set_text_vehicle)
        self.show()

    def set_text_customer(self):
        index = self.c_name.index(self.input_c_name.text())
        self.input_address.setText(self.cust[index][2])
        self.input_contact.setText(str(self.cust[index][3]))
        self.comboBox_reg_no.clear()
        self.veh = vehicle.Vehicle.search_by_cust(self.cust[index][0])
        for v_record in self.veh:
            self.comboBox_reg_no.addItem(v_record[1])
        # self.input_model.clear()
        # self.input_type.clear()
        self.set_text_vehicle(0)

    def set_text_vehicle(self, param):
        record = self.veh[param]
        self.input_type.setText(str(record[4]))
        self.input_model.setText(str(record[3]))

    def ser_ui_add(self):
        date = self.dateEdit_s_date.text()
        job_desc = self.input_job_desc.toPlainText()
        advisor = self.emp[self.comboBox_advisor.currentIndex()][0]
        distance = self.input_dist.text()
        damages = self.input_damg.toPlainText()
        veh_id = self.veh[self.comboBox_reg_no.currentIndex()][0]
        ser_obj = Service(job_desc, date, distance, damages, veh_id, advisor)
        ser_obj.service_add()
        self.close()

    def ser_ui_update(self, s_id):
        date = self.dateEdit_s_date.text()
        job_desc = self.input_job_desc.toPlainText()
        advisor = self.emp[self.comboBox_advisor.currentIndex()][0]
        distance = self.input_dist.text()
        damages = self.input_damg.toPlainText()
        veh_id = self.veh[self.comboBox_reg_no.currentIndex()][0]
        ser_obj = Service(job_desc, date, distance, damages, veh_id, advisor, service_id=s_id)
        ser_obj.service_update()
        print(date, job_desc,advisor,distance,damages,veh_id, s_id)


class BillUI(QDialog, bill_ui.Ui_Dialog):
    def __init__(self, s_id):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()
        self.total = 0
        self.s_id = s_id
        self.parts_used_view()
        self.part = parts.Part.view()
        self.p_name = [record[1] for record in self.part]
        completer = QCompleter(self.p_name, self.input_part)
        self.input_part.setCompleter(completer)
        self.bt_add.clicked.connect(self.bill_add_part)
        self.bt_add.clicked.connect(self.parts_used_view)
        self.bt_delete.clicked.connect(self.bill_del_part)
        self.bt_bill.clicked.connect(lambda: self.bill_gen())

    def bill_add_part(self):
        index = self.p_name.index(self.input_part.text())
        p_id = self.part[index][0]
        qty = self.input_qty.text()
        Service.add_part_used(self.s_id, p_id, qty)
        self.input_part.clear()
        self.input_qty.clear()

    def bill_del_part(self):
        if self.parts_use_table.currentRow() != -1:
            p_id = self.parts_use_table.item(self.parts_use_table.currentRow(), 0).text()
            Service.parts_used_del(self.s_id, p_id)
            self.parts_used_view()
            self.parts_use_table.reset()

    def parts_used_view(self):
        result = Service.parts_used_view(self.s_id)
        self.parts_use_table.setRowCount(len(result))
        self.parts_use_table.setColumnCount(5)
        row = 0
        for x in result:
            for col in range(0, 5):
                self.parts_use_table.setItem(row, col, QTableWidgetItem(str(x[col])))
            self.total += float(x[4])
            row += 1
        Service.service_price_update(self.s_id, self.total)

    def bill_gen(self):
        print("bill gen def")
        service_details = Service.service_search(self.s_id)
        part_used = Service.parts_used_view(self.s_id)
        customer_details = Service.service_cust_search(self.s_id)
        vehicle_details = Service.service_vehicle_search(self.s_id)
        employee_details = Service.service_employee_search(self.s_id)
        invoicedemo.Bill(service_details, part_used, customer_details, vehicle_details, employee_details)
