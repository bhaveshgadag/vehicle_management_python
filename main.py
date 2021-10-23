import sys
from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QTableWidget, QDialog, QTableWidgetItem, QHeaderView, QApplication, QMainWindow, QMessageBox

import ui.MainWindow
import customer, vehicle, parts, employee, service


class MyMainWindow(QMainWindow, ui.MainWindow.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.c_view.clicked.connect(lambda: self.cust_view())
        self.c_add.clicked.connect(lambda: self.cust_add())
        self.c_update.clicked.connect(lambda: self.cust_update())
        self.c_delete.clicked.connect(lambda: self.cust_del())
        self.v_view.clicked.connect(lambda: self.veh_view())
        self.v_add.clicked.connect(lambda: self.veh_add())
        self.v_update.clicked.connect(lambda: self.veh_update())
        self.v_del.clicked.connect(lambda: self.veh_del())
        self.p_view.clicked.connect(lambda: self.part_view())
        self.p_add.clicked.connect(lambda: self.part_add())
        self.p_update.clicked.connect(lambda: self.part_update())
        self.p_delete.clicked.connect(lambda: self.part_del())
        self.e_view.clicked.connect(lambda: self.emp_view())
        self.e_add.clicked.connect(lambda: self.emp_add())
        # self.e_update.clicked.connect()
        self.e_delete.clicked.connect(lambda: self.emp_del())
        self.s_view.clicked.connect(lambda: self.ser_view())
        self.s_add.clicked.connect(lambda: self.ser_add())
        self.s_update.clicked.connect(lambda: self.ser_update())
        self.s_del.clicked.connect(lambda: self.ser_delete())
        self.ser_table.itemDoubleClicked.connect(lambda: self.ser_add_parts())

    def cust_add(self):
        self.dlg = customer.CustomerAddUI()
        self.dlg.bt_ok.clicked.connect(self.dlg.cust_ui_add)
        self.dlg.bt_ok.clicked.connect(self.cust_view)

    def cust_del(self):
        if self.cust_table.currentRow() is not -1:
            cust_id = self.cust_table.item(self.cust_table.currentRow(), 0).text()
            print(cust_id)
            customer.Customer.customer_delete(cust_id)
            self.cust_view()
        else:
            print("not selected")
            self.showdialog()

    def cust_update(self):
        if self.cust_table.currentRow() is not -1:
            self.dlg = customer.CustomerAddUI()
            record = [self.cust_table.item(self.cust_table.currentRow(), i).text()
                      for i in range(self.cust_table.columnCount())]
            self.dlg.input_c_id.setText(record[0])
            self.dlg.input_c_name.setText(record[1])
            self.dlg.input_c_address.setText(record[2])
            self.dlg.input_c_contact.setText(record[3])
            self.dlg.input_c_email.setText(record[4])
            self.dlg.bt_ok.clicked.connect(self.dlg.cust_ui_update)
            self.dlg.bt_ok.clicked.connect(self.cust_view)
        else:
            print("not selected")
            self.showdialog()

    def cust_view(self):
        result = customer.Customer.view_all()
        self.cust_table.setRowCount(len(result))
        self.cust_table.setColumnCount(5)
        row = 0
        for x in result:
            for col in range(0, 5):
                self.cust_table.setItem(row, col, QTableWidgetItem(str(x[col])))
            row += 1
        self.cust_table.resizeColumnToContents(1)

    def veh_add(self):
        print("creating ui")
        self.dlg = vehicle.VehicleUI()
        self.dlg.bt_ok.clicked.connect(self.dlg.veh_ui_add)
        self.dlg.bt_ok.clicked.connect(self.veh_view)

    def veh_update(self):
        if self.veh_table.currentRow() is not -1:
            self.dlg = vehicle.VehicleUI()
            v_id = self.veh_table.item(self.veh_table.currentRow(), 0).text()
            record = vehicle.Vehicle.veh_search(v_id)
            print(record)
            cust = None
            for c_record in self.dlg.cust:
                if c_record[0] is record[6]:
                    cust = c_record
            self.dlg.input_c_name.setText(cust[1])
            self.dlg.input_v_contact.setText(cust[3])
            self.dlg.input_v_id.setText(str(record[0]))
            self.dlg.input_v_reg_no.setText(record[1])
            self.dlg.input_v_company.setText(record[2])
            self.dlg.input_v_model.setText(record[3])
            self.dlg.input_v_type.setText(record[4])
            if record[5] is "manual":
                self.dlg.rbt_v_manual.setChecked(True)
            else:
                self.dlg.rbt_v_auto.setChecked(True)
            self.dlg.bt_ok.setText("Update")
            self.dlg.bt_ok.clicked.connect(lambda: self.dlg.veh_ui_update())
            self.dlg.bt_ok.clicked.connect(lambda: self.veh_view())
        else:
            self.showdialog()

    def veh_del(self):
        if self.veh_table.currentRow() is not -1:
            vid = self.veh_table.item(self.veh_table.currentRow(), 0).text()
            vehicle.Vehicle.delete(vid)
            self.veh_view()
        else:
            print("not selected")
            self.showdialog()

    def veh_view(self):
        result = vehicle.Vehicle.view_all()
        self.veh_table.setRowCount(len(result))
        self.veh_table.setColumnCount(7)
        row = 0
        for x in result:
            for col in range(0, 7):
                self.veh_table.setItem(row, col, QTableWidgetItem(str(x[col])))
            row += 1
        self.veh_table.resizeColumnToContents(0)

    def part_add(self):
        print("creating ui")
        self.dlg = parts.PartUI()
        self.dlg.bt_ok.clicked.connect(self.dlg.part_ui_add)
        self.dlg.bt_ok.clicked.connect(self.part_view)

    def part_update(self):
        if self.part_table.currentRow() is not -1:
            self.dlg = parts.PartUI()
            p_id = self.part_table.item(self.part_table.currentRow(),0).text()
            record = parts.Part.part_search(p_id)
            self.dlg.input_p_id.setText(str(record[0]))
            self.dlg.input_p_name.setText(record[1])
            self.dlg.input_p_brand.setText(record[2])
            self.dlg.input_p_price.setText(str(record[3]))
            self.dlg.bt_ok.setText("Update")
            self.dlg.bt_ok.clicked.connect(lambda: self.dlg.part_ui_update())
            self.dlg.bt_ok.clicked.connect(lambda: self.part_view())
        else:
            self.showdialog()

    def part_del(self):
        if self.part_table.currentRow() is not -1:
            part_id = self.part_table.item(self.part_table.currentRow(), 0).text()
            print(part_id)
            try:
                flag = parts.Part.part_delete(part_id)
                # print(flag)
                if not flag:
                    raise ArithmeticError
            except :
                self.other_table()
            finally:
                self.part_view()
        else:
            print("not selected")
            self.showdialog()

    def part_view(self):
        result = parts.Part.view()
        self.part_table.setRowCount(len(result))
        self.part_table.setColumnCount(4)
        row = 0
        for x in result:
            for col in range(0, 4):
                self.part_table.setItem(row, col, QTableWidgetItem(str(x[col])))
            row += 1
        self.part_table.resizeColumnToContents(1)

    def emp_add(self):
        print("emp_add ui started")
        self.dlg = employee.EmployeeAddUI()
        self.dlg.bt_ok.clicked.connect(lambda: self.dlg.emp_ui_add())
        # self.dlg.bt_ok.clicked.connect(lambda: self.emp_view())

    def emp_del(self):
        if self.emp_table.currentRow() is not -1:
            emp_id = self.emp_table.item(self.emp_table.currentRow(), 0).text()
            print(emp_id)
            try:
                flag = employee.Employee.emp_delete(emp_id)
                # print(flag)
                if not flag:
                    raise ArithmeticError
            except :
                self.other_table()
            finally:
                self.emp_view()
        else:
            print("not selected")
            self.showdialog()

    def emp_view(self):
        result = employee.Employee.view_all()
        self.emp_table.setRowCount(len(result))
        self.emp_table.setColumnCount(6)
        row = 0
        for x in result:
            for col in range(0, 6):
                self.emp_table.setItem(row, col, QTableWidgetItem(str(x[col])))
            row += 1
        self.emp_table.resizeColumnToContents(1)

    def ser_view(self):
        result = service.Service.service_view()
        self.ser_table.setRowCount(len(result))
        self.ser_table.setColumnCount(7)
        row = 0
        for x in result:
            for col in range(0, 7):
                self.ser_table.setItem(row, col, QTableWidgetItem(str(x[col])))
            row += 1
        self.ser_table.resizeColumnToContents(7)

    def ser_add(self):
        self.dlg = service.ServiceAddUI()
        self.dlg.bt_ok.clicked.connect(self.dlg.ser_ui_add)
        self.dlg.bt_ok.clicked.connect(self.ser_view)

    def ser_update(self):
        if self.ser_table.currentRow() is not -1:
            self.dlg = service.ServiceAddUI()
            s_id = self.ser_table.item(self.ser_table.currentRow(), 0).text()
            record = [service.Service.service_search(s_id),
                      service.Service.service_cust_search(s_id),
                      service.Service.service_vehicle_search(s_id),
                      service.Service.service_employee_search(s_id)]
            self.dlg.input_c_name.setText(record[1][1])
            self.dlg.input_address.setText(record[1][2])
            self.dlg.input_contact.setText(str(record[1][3]))
            self.dlg.set_text_customer()
            index = self.dlg.comboBox_reg_no.findText(record[2][1], QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.dlg.comboBox_reg_no.setCurrentIndex(index)
            self.dlg.set_text_vehicle(index)
            date = QDate.fromString(str(record[0][2]), 'yyyy-MM-dd')
            self.dlg.dateEdit_s_date.setDate(date)
            self.dlg.input_job_desc.setText(record[0][1])
            self.dlg.input_dist.setText(str(record[0][3]))
            self.dlg.input_damg.setText(record[0][4])
            index = self.dlg.comboBox_advisor.findText(record[3][0], QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.dlg.comboBox_advisor.setCurrentIndex(index)
            self.dlg.bt_ok.setText("Update")
            self.dlg.bt_ok.clicked.connect(lambda: self.dlg.ser_ui_update(record[0][0]))
            self.dlg.bt_ok.clicked.connect(self.ser_view)
        else:
            print("not selected")
            self.showdialog()

    def ser_delete(self):
        if self.ser_table.currentRow() is not -1:
            ser_id = self.ser_table.item(self.ser_table.currentRow(), 0).text()
            service.Service.service_delete(ser_id)
            self.dlg.bt_ok.clicked.connect(self.ser_view)
        else:
            print("not selected")
            self.showdialog()

    def ser_add_parts(self):
        print("ser_add_part")
        record = [self.ser_table.item(self.ser_table.currentRow(), i).text()
                  for i in range(self.ser_table.columnCount())]
        print("creating billui obj")
        self.dlg = service.BillUI(record[0])
        self.dlg.input_veh.setText(record[4])
        self.dlg.textEdit_desc.setText(record[1])
        self.dlg.input_date.setText(record[2])
        self.dlg.input_advisor.setText(record[6])

    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Error")

        msg.setText("No record selected.")
        msg.exec_()

    def other_table(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Info")

        msg.setText("Can not delete.\nSelected record is used in other table.")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
