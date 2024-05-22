# Form implementation generated from reading ui file '.\viewmembers.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView, QAbstractItemView

class View_Members(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(571, 412)
        Dialog.setStyleSheet("background-color: rgb(153, 149, 136);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setStyleSheet("background-color: rgb(212, 255, 146);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(139)
        self.tableWidget.verticalHeader().setDefaultSectionSize(31)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.pushButton.setStyleSheet("QPushButton{border-radius:11px;\n"
"background-color: rgb(146, 193, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.view_members)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def view_members(self):
        try:
            mydb = sqlite3.connect("DB.db")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM addmember")
            myresult = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number , row_data in enumerate(myresult):
                self.tableWidget.insertRow(row_number)
                for col_number , col_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,col_number,QTableWidgetItem(str(col_data)))
        except sqlite3.Error as e:
            pass
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Members"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Moblie"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Email"))
        self.pushButton.setText(_translate("Dialog", "View Members"))


