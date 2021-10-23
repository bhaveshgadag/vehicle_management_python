# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e_add.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 337)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.input_emp_id = QtWidgets.QLineEdit(self.frame)
        self.input_emp_id.setEnabled(False)
        self.input_emp_id.setObjectName("input_emp_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_emp_id)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.input_emp_name = QtWidgets.QLineEdit(self.frame)
        self.input_emp_name.setObjectName("input_emp_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_emp_name)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.input_emp_address = QtWidgets.QTextEdit(self.frame)
        self.input_emp_address.setObjectName("input_emp_address")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_emp_address)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.input_emp_contact = QtWidgets.QLineEdit(self.frame)
        self.input_emp_contact.setObjectName("input_emp_contact")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_emp_contact)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dateEdit_doj = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_doj.setCalendarPopup(True)
        self.dateEdit_doj.setObjectName("dateEdit_doj")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateEdit_doj)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.input_emp_salary = QtWidgets.QLineEdit(self.frame)
        self.input_emp_salary.setObjectName("input_emp_salary")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.input_emp_salary)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_ok = QtWidgets.QPushButton(Dialog)
        self.bt_ok.setObjectName("bt_ok")
        self.horizontalLayout.addWidget(self.bt_ok)
        self.bt_cancel = QtWidgets.QPushButton(Dialog)
        self.bt_cancel.setObjectName("bt_cancel")
        self.horizontalLayout.addWidget(self.bt_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ID"))
        self.input_emp_id.setText(_translate("Dialog", "AUTOMATIC"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_3.setText(_translate("Dialog", "Address"))
        self.label_4.setText(_translate("Dialog", "Contact No."))
        self.label_5.setText(_translate("Dialog", "Date of joining"))
        self.dateEdit_doj.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd"))
        self.label_6.setText(_translate("Dialog", "Salary"))
        self.bt_ok.setText(_translate("Dialog", "OK"))
        self.bt_cancel.setText(_translate("Dialog", "Cancel"))

