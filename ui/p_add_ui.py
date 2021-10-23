# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p_add.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(355, 190)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.label_p_id = QtWidgets.QLabel(Dialog)
        self.label_p_id.setObjectName("label_p_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_p_id)
        self.input_p_id = QtWidgets.QLineEdit(Dialog)
        self.input_p_id.setEnabled(False)
        self.input_p_id.setObjectName("input_p_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_p_id)
        self.label_p_name = QtWidgets.QLabel(Dialog)
        self.label_p_name.setObjectName("label_p_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_p_name)
        self.input_p_name = QtWidgets.QLineEdit(Dialog)
        self.input_p_name.setObjectName("input_p_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_p_name)
        self.label_p_brand = QtWidgets.QLabel(Dialog)
        self.label_p_brand.setObjectName("label_p_brand")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_p_brand)
        self.input_p_brand = QtWidgets.QLineEdit(Dialog)
        self.input_p_brand.setObjectName("input_p_brand")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_p_brand)
        self.label_p_price = QtWidgets.QLabel(Dialog)
        self.label_p_price.setObjectName("label_p_price")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_p_price)
        self.input_p_price = QtWidgets.QLineEdit(Dialog)
        self.input_p_price.setObjectName("input_p_price")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_p_price)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_ok = QtWidgets.QPushButton(self.frame)
        self.bt_ok.setObjectName("bt_ok")
        self.horizontalLayout.addWidget(self.bt_ok)
        self.bt_cancel = QtWidgets.QPushButton(self.frame)
        self.bt_cancel.setObjectName("bt_cancel")
        self.horizontalLayout.addWidget(self.bt_cancel)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_p_id.setText(_translate("Dialog", "ID"))
        self.input_p_id.setText(_translate("Dialog", "AUTOMATIC"))
        self.label_p_name.setText(_translate("Dialog", "Name"))
        self.label_p_brand.setText(_translate("Dialog", "Brand"))
        self.label_p_price.setText(_translate("Dialog", "Price"))
        self.bt_ok.setText(_translate("Dialog", "OK"))
        self.bt_cancel.setText(_translate("Dialog", "Cancel"))

