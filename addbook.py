# Form implementation generated from reading ui file '.\addbook.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 450)
        Dialog.setStyleSheet("background-color: rgb(255, 218, 174);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_title = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_title.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit_title.setText("")
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.verticalLayout.addWidget(self.lineEdit_title)
        self.lineEdit_id = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_id.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit_id.setText("")
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.verticalLayout.addWidget(self.lineEdit_id)
        self.lineEdit_author = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_author.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit_author.setText("")
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.verticalLayout.addWidget(self.lineEdit_author)
        self.lineEdit_publisher = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_publisher.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit_publisher.setText("")
        self.lineEdit_publisher.setObjectName("lineEdit_publisher")
        self.verticalLayout.addWidget(self.lineEdit_publisher)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Book"))
        self.lineEdit_title.setPlaceholderText(_translate("Dialog", "Please Enter Title"))
        self.lineEdit_id.setPlaceholderText(_translate("Dialog", "Please Enter ID"))
        self.lineEdit_author.setPlaceholderText(_translate("Dialog", "Please Enter Author"))
        self.lineEdit_publisher.setPlaceholderText(_translate("Dialog", "Please Enter Publisher"))
        self.pushButton.setText(_translate("Dialog", "Add Book"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec())
