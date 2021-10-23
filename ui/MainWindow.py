# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 815)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.Service = QtWidgets.QWidget()
        self.Service.setObjectName("Service")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Service)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_6 = QtWidgets.QFrame(self.Service)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.s_view = QtWidgets.QPushButton(self.frame_6)
        self.s_view.setObjectName("s_view")
        self.horizontalLayout_4.addWidget(self.s_view)
        self.s_add = QtWidgets.QPushButton(self.frame_6)
        self.s_add.setObjectName("s_add")
        self.horizontalLayout_4.addWidget(self.s_add)
        self.s_update = QtWidgets.QPushButton(self.frame_6)
        self.s_update.setObjectName("s_update")
        self.horizontalLayout_4.addWidget(self.s_update)
        self.s_del = QtWidgets.QPushButton(self.frame_6)
        self.s_del.setObjectName("s_del")
        self.horizontalLayout_4.addWidget(self.s_del)
        self.verticalLayout_11.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.Service)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.ser_table = QtWidgets.QTableWidget(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ser_table.sizePolicy().hasHeightForWidth())
        self.ser_table.setSizePolicy(sizePolicy)
        self.ser_table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ser_table.setFont(font)
        self.ser_table.setAutoFillBackground(False)
        self.ser_table.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.ser_table.setAlternatingRowColors(True)
        self.ser_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ser_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ser_table.setObjectName("ser_table")
        self.ser_table.setColumnCount(7)
        self.ser_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ser_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ser_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ser_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ser_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ser_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ser_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ser_table.setHorizontalHeaderItem(6, item)
        self.ser_table.horizontalHeader().setCascadingSectionResizes(True)
        self.ser_table.horizontalHeader().setStretchLastSection(True)
        self.ser_table.verticalHeader().setVisible(True)
        self.ser_table.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout_10.addWidget(self.ser_table)
        self.verticalLayout_11.addWidget(self.frame_5)
        self.tabWidget.addTab(self.Service, "")
        self.Customer = QtWidgets.QWidget()
        self.Customer.setObjectName("Customer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Customer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.Customer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 61))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.c_view = QtWidgets.QPushButton(self.frame_4)
        self.c_view.setObjectName("c_view")
        self.horizontalLayout_2.addWidget(self.c_view)
        self.c_add = QtWidgets.QPushButton(self.frame_4)
        self.c_add.setObjectName("c_add")
        self.horizontalLayout_2.addWidget(self.c_add)
        self.c_update = QtWidgets.QPushButton(self.frame_4)
        self.c_update.setObjectName("c_update")
        self.horizontalLayout_2.addWidget(self.c_update)
        self.c_delete = QtWidgets.QPushButton(self.frame_4)
        self.c_delete.setObjectName("c_delete")
        self.horizontalLayout_2.addWidget(self.c_delete)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.Customer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cust_table = QtWidgets.QTableWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cust_table.sizePolicy().hasHeightForWidth())
        self.cust_table.setSizePolicy(sizePolicy)
        self.cust_table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cust_table.setFont(font)
        self.cust_table.setAutoFillBackground(False)
        self.cust_table.setAlternatingRowColors(True)
        self.cust_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.cust_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cust_table.setObjectName("cust_table")
        self.cust_table.setColumnCount(5)
        self.cust_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cust_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cust_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cust_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cust_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cust_table.setHorizontalHeaderItem(4, item)
        self.cust_table.horizontalHeader().setCascadingSectionResizes(True)
        self.cust_table.horizontalHeader().setStretchLastSection(True)
        self.cust_table.verticalHeader().setVisible(False)
        self.cust_table.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout_6.addWidget(self.cust_table)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.tabWidget.addTab(self.Customer, "")
        self.Vehicle = QtWidgets.QWidget()
        self.Vehicle.setObjectName("Vehicle")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Vehicle)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.Vehicle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.v_view = QtWidgets.QPushButton(self.frame)
        self.v_view.setObjectName("v_view")
        self.horizontalLayout.addWidget(self.v_view)
        self.v_add = QtWidgets.QPushButton(self.frame)
        self.v_add.setObjectName("v_add")
        self.horizontalLayout.addWidget(self.v_add)
        self.v_update = QtWidgets.QPushButton(self.frame)
        self.v_update.setObjectName("v_update")
        self.horizontalLayout.addWidget(self.v_update)
        self.v_del = QtWidgets.QPushButton(self.frame)
        self.v_del.setObjectName("v_del")
        self.horizontalLayout.addWidget(self.v_del)
        self.verticalLayout_4.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.Vehicle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.veh_table = QtWidgets.QTableWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.veh_table.sizePolicy().hasHeightForWidth())
        self.veh_table.setSizePolicy(sizePolicy)
        self.veh_table.setMaximumSize(QtCore.QSize(9504685, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.veh_table.setFont(font)
        self.veh_table.setAutoFillBackground(False)
        self.veh_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.veh_table.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.veh_table.setAlternatingRowColors(True)
        self.veh_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.veh_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.veh_table.setObjectName("veh_table")
        self.veh_table.setColumnCount(7)
        self.veh_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.veh_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.veh_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.veh_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.veh_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.veh_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.veh_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.veh_table.setHorizontalHeaderItem(6, item)
        self.veh_table.horizontalHeader().setCascadingSectionResizes(True)
        self.veh_table.horizontalHeader().setDefaultSectionSize(125)
        self.veh_table.horizontalHeader().setHighlightSections(False)
        self.veh_table.horizontalHeader().setStretchLastSection(True)
        self.veh_table.verticalHeader().setVisible(False)
        self.veh_table.verticalHeader().setCascadingSectionResizes(False)
        self.veh_table.verticalHeader().setDefaultSectionSize(43)
        self.veh_table.verticalHeader().setHighlightSections(False)
        self.veh_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.veh_table)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.tabWidget.addTab(self.Vehicle, "")
        self.Parts = QtWidgets.QWidget()
        self.Parts.setObjectName("Parts")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Parts)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.Parts)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.p_view = QtWidgets.QPushButton(self.frame_7)
        self.p_view.setObjectName("p_view")
        self.horizontalLayout_3.addWidget(self.p_view)
        self.p_add = QtWidgets.QPushButton(self.frame_7)
        self.p_add.setObjectName("p_add")
        self.horizontalLayout_3.addWidget(self.p_add)
        self.p_update = QtWidgets.QPushButton(self.frame_7)
        self.p_update.setObjectName("p_update")
        self.horizontalLayout_3.addWidget(self.p_update)
        self.p_delete = QtWidgets.QPushButton(self.frame_7)
        self.p_delete.setObjectName("p_delete")
        self.horizontalLayout_3.addWidget(self.p_delete)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.frame_10 = QtWidgets.QFrame(self.Parts)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.part_table = QtWidgets.QTableWidget(self.frame_10)
        self.part_table.setAlternatingRowColors(True)
        self.part_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.part_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.part_table.setObjectName("part_table")
        self.part_table.setColumnCount(4)
        self.part_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.part_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.part_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.part_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.part_table.setHorizontalHeaderItem(3, item)
        self.part_table.horizontalHeader().setStretchLastSection(True)
        self.part_table.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.part_table)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.tabWidget.addTab(self.Parts, "")
        self.Employee = QtWidgets.QWidget()
        self.Employee.setObjectName("Employee")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Employee)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_8 = QtWidgets.QFrame(self.Employee)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.e_view = QtWidgets.QPushButton(self.frame_8)
        self.e_view.setObjectName("e_view")
        self.horizontalLayout_5.addWidget(self.e_view)
        self.e_add = QtWidgets.QPushButton(self.frame_8)
        self.e_add.setObjectName("e_add")
        self.horizontalLayout_5.addWidget(self.e_add)
        self.e_update = QtWidgets.QPushButton(self.frame_8)
        self.e_update.setObjectName("e_update")
        self.horizontalLayout_5.addWidget(self.e_update)
        self.e_delete = QtWidgets.QPushButton(self.frame_8)
        self.e_delete.setObjectName("e_delete")
        self.horizontalLayout_5.addWidget(self.e_delete)
        self.verticalLayout_9.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.Employee)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.emp_table = QtWidgets.QTableWidget(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.emp_table.setFont(font)
        self.emp_table.setAlternatingRowColors(True)
        self.emp_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.emp_table.setObjectName("emp_table")
        self.emp_table.setColumnCount(6)
        self.emp_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.emp_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.emp_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.emp_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.emp_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.emp_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.emp_table.setHorizontalHeaderItem(5, item)
        self.emp_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_8.addWidget(self.emp_table)
        self.verticalLayout_9.addWidget(self.frame_9)
        self.tabWidget.addTab(self.Employee, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setMinimumSize(QtCore.QSize(2, 2))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.s_view.setText(_translate("MainWindow", "View"))
        self.s_add.setText(_translate("MainWindow", "Add"))
        self.s_update.setText(_translate("MainWindow", "Update"))
        self.s_del.setText(_translate("MainWindow", "Delete"))
        item = self.ser_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.ser_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        item = self.ser_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Service Date"))
        item = self.ser_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total Price"))
        item = self.ser_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Vehicle"))
        item = self.ser_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Customer"))
        item = self.ser_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Service Advisor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Service), _translate("MainWindow", "Service"))
        self.c_view.setText(_translate("MainWindow", "View"))
        self.c_add.setText(_translate("MainWindow", "Add"))
        self.c_update.setText(_translate("MainWindow", "Update"))
        self.c_delete.setText(_translate("MainWindow", "Delete"))
        item = self.cust_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.cust_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.cust_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address"))
        item = self.cust_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Contact"))
        item = self.cust_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Customer), _translate("MainWindow", "Customer"))
        self.v_view.setText(_translate("MainWindow", "View"))
        self.v_add.setText(_translate("MainWindow", "Add"))
        self.v_update.setText(_translate("MainWindow", "Update"))
        self.v_del.setText(_translate("MainWindow", "Delete"))
        item = self.veh_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.veh_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Reg. No."))
        item = self.veh_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Company"))
        item = self.veh_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Model"))
        item = self.veh_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Type"))
        item = self.veh_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Transmission"))
        item = self.veh_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Customer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Vehicle), _translate("MainWindow", "Vehicle"))
        self.p_view.setText(_translate("MainWindow", "View"))
        self.p_add.setText(_translate("MainWindow", "Add"))
        self.p_update.setText(_translate("MainWindow", "Update"))
        self.p_delete.setText(_translate("MainWindow", "Delete"))
        self.part_table.setSortingEnabled(True)
        item = self.part_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.part_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.part_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Brand"))
        item = self.part_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Parts), _translate("MainWindow", "Parts"))
        self.e_view.setText(_translate("MainWindow", "View"))
        self.e_add.setText(_translate("MainWindow", "Add"))
        self.e_update.setText(_translate("MainWindow", "Update"))
        self.e_delete.setText(_translate("MainWindow", "Delete"))
        item = self.emp_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.emp_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.emp_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address"))
        item = self.emp_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Contact no"))
        item = self.emp_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date of joining"))
        item = self.emp_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Salary"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Employee), _translate("MainWindow", "Employee"))
