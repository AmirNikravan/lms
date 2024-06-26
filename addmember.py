# Form implementation generated from reading ui file '.\addmember.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from msilib import Dialog

from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3

class Add_Member(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(367, 377)
        Dialog.setStyleSheet("background-color: rgb(153, 149, 136);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_id = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_id.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit_id.setStyleSheet("QLineEdit{border-radius:5px;\n"
"background-color: rgb(217, 255, 193);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(255, 215, 238);\n"
"}\n"
"")
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.verticalLayout.addWidget(self.lineEdit_id)
        self.lineEdit_name = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_name.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit_name.setStyleSheet("QLineEdit{border-radius:5px;\n"
"background-color: rgb(217, 255, 193);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(255, 215, 238);\n"
"}\n"
"")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        self.lineEdit_mobile = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_mobile.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit_mobile.setStyleSheet("QLineEdit{border-radius:5px;\n"
"background-color: rgb(217, 255, 193);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(255, 215, 238);\n"
"}\n"
"")
        self.lineEdit_mobile.setObjectName("lineEdit_mobile")
        self.verticalLayout.addWidget(self.lineEdit_mobile)
        self.lineEdit_email = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_email.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit_email.setStyleSheet("QLineEdit{border-radius:5px;\n"
"background-color: rgb(217, 255, 193);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(255, 215, 238);\n"
"}\n"
"")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.verticalLayout.addWidget(self.lineEdit_email)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
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
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton.clicked.connect(self.inser_member)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def inser_member(self):
        try:
            mydb = sqlite3.connect('DB.db')
            mycursor = mydb.cursor()
            id = self.lineEdit_id.text()
            name = self.lineEdit_name.text()
            mobile = self.lineEdit_mobile.text()
            email = self.lineEdit_email.text()
            if id == '' or name == '' or mobile == '' or email == '':
                self.label.setText('please fill all fields')
                self.label.setStyleSheet("color: red;")
                return
            query = 'INSERT INTO addmember (id, name, mobile, email) VALUES (?, ?, ?, ?)'
            values = (id, name, mobile, email)
            mycursor.execute(query, values)
            mydb.commit()
            mydb.close()
            self.label.setText("Member Inserted")
            self.label.setStyleSheet("color: green")
            self.lineEdit_id.setText('')
            self.lineEdit_name.setText('')
            self.lineEdit_mobile.setText('')
            self.lineEdit_email.setText('')
        except sqlite3.Error as error:
            self.label.setStyleSheet("color: red")
            self.label.setText(f"Error{error}")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Member"))
        self.lineEdit_id.setPlaceholderText(_translate("Dialog", "Please Enter Member ID"))
        self.lineEdit_name.setPlaceholderText(_translate("Dialog", "Please Enter Member Name"))
        self.lineEdit_mobile.setPlaceholderText(_translate("Dialog", "Please Enter Member Mobile"))
        self.lineEdit_email.setPlaceholderText(_translate("Dialog", "Please Enter Member Email"))
        self.pushButton.setText(_translate("Dialog", "Add Member"))


