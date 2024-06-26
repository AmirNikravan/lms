# Form implementation generated from reading ui file '.\window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 542)
        MainWindow.setStyleSheet("background-color: rgb(217, 218, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 196, 199);")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalWidget = QtWidgets.QWidget(parent=self.tab_1)
        self.horizontalWidget.setStyleSheet("QWidget{\n"
"\n"
"    background-color: rgb(243, 255, 196);\n"
"\n"
"\n"
"}")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_bookid = QtWidgets.QLineEdit(parent=self.horizontalWidget)
        self.lineEdit_bookid.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_bookid.setStyleSheet("QLineEdit{border-radius:5px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(255, 215, 238);\n"
"}\n"
"")
        self.lineEdit_bookid.setObjectName("lineEdit_bookid")
        self.horizontalLayout.addWidget(self.lineEdit_bookid)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_bookname = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_bookname.setFont(font)
        self.label_bookname.setObjectName("label_bookname")
        self.verticalLayout_2.addWidget(self.label_bookname)
        self.label_bookauthor = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_bookauthor.setFont(font)
        self.label_bookauthor.setObjectName("label_bookauthor")
        self.verticalLayout_2.addWidget(self.label_bookauthor)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout_4.addWidget(self.horizontalWidget)
        self.horizontalWidget_2 = QtWidgets.QWidget(parent=self.tab_1)
        self.horizontalWidget_2.setStyleSheet("QWidget{\n"
"\n"
"    background-color: rgb(243, 255, 196);\n"
"\n"
"\n"
"}")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_memberid = QtWidgets.QLineEdit(parent=self.horizontalWidget_2)
        self.lineEdit_memberid.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_memberid.setStyleSheet("QLineEdit{border-radius:5px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(255, 215, 238);\n"
"}\n"
"")
        self.lineEdit_memberid.setObjectName("lineEdit_memberid")
        self.horizontalLayout_2.addWidget(self.lineEdit_memberid)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.widget1 = QtWidgets.QWidget(parent=self.horizontalWidget_2)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_membername = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_membername.setFont(font)
        self.label_membername.setObjectName("label_membername")
        self.verticalLayout_3.addWidget(self.label_membername)
        self.label_contactinfo = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_contactinfo.setFont(font)
        self.label_contactinfo.setObjectName("label_contactinfo")
        self.verticalLayout_3.addWidget(self.label_contactinfo)
        self.horizontalLayout_2.addWidget(self.widget1)
        self.verticalLayout_4.addWidget(self.horizontalWidget_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.toolButton_issuebook = QtWidgets.QToolButton(parent=self.tab_1)
        self.toolButton_issuebook.setStyleSheet("QToolButton{border-radius:11px;\n"
"\n"
"\n"
"background-color: rgb(255, 110, 185);\n"
"\n"
"}\n"
"QToolButton:hover{\n"
"\n"
"\n"
"\n"
"    background-color: rgb(34, 133, 255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/issuebook.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_issuebook.setIcon(icon)
        self.toolButton_issuebook.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_issuebook.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_issuebook.setObjectName("toolButton_issuebook")
        self.horizontalLayout_3.addWidget(self.toolButton_issuebook)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_submission = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_submission.setMaximumSize(QtCore.QSize(16777215, 80))
        self.lineEdit_submission.setStyleSheet("QLineEdit{border-radius:5px;\n"
"background-color: rgb(217, 255, 193);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(255, 215, 238);\n"
"}\n"
"")
        self.lineEdit_submission.setObjectName("lineEdit_submission")
        self.verticalLayout_5.addWidget(self.lineEdit_submission)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.tab_2)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 227, 194);")
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(295)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.toolButton_renew = QtWidgets.QToolButton(parent=self.tab_2)
        self.toolButton_renew.setStyleSheet("QToolButton{border-radius:11px;\n"
"\n"
"\n"
"background-color: rgb(255, 110, 185);\n"
"\n"
"}\n"
"QToolButton:hover{\n"
"\n"
"\n"
"\n"
"    background-color: rgb(34, 133, 255);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/renew.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_renew.setIcon(icon1)
        self.toolButton_renew.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_renew.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_renew.setObjectName("toolButton_renew")
        self.horizontalLayout_4.addWidget(self.toolButton_renew)
        self.toolButton_submit = QtWidgets.QToolButton(parent=self.tab_2)
        self.toolButton_submit.setStyleSheet("QToolButton{border-radius:11px;\n"
"\n"
"\n"
"background-color: rgb(255, 110, 185);\n"
"\n"
"}\n"
"QToolButton:hover{\n"
"\n"
"\n"
"\n"
"    background-color: rgb(34, 133, 255);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/submission.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_submit.setIcon(icon2)
        self.toolButton_submit.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_submit.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_submit.setObjectName("toolButton_submit")
        self.horizontalLayout_4.addWidget(self.toolButton_submit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton_addbook = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton_addbook.setMaximumSize(QtCore.QSize(145, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.toolButton_addbook.setFont(font)
        self.toolButton_addbook.setStyleSheet("QToolButton{border-radius:11px;\n"
"background-color: rgb(146, 193, 255);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/addbook.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_addbook.setIcon(icon3)
        self.toolButton_addbook.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_addbook.setCheckable(False)
        self.toolButton_addbook.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_addbook.setObjectName("toolButton_addbook")
        self.verticalLayout.addWidget(self.toolButton_addbook)
        self.toolButton_addmember = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton_addmember.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.toolButton_addmember.setFont(font)
        self.toolButton_addmember.setStyleSheet("QToolButton{border-radius:11px;\n"
"background-color: rgb(146, 193, 255);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/addmember.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_addmember.setIcon(icon4)
        self.toolButton_addmember.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_addmember.setCheckable(False)
        self.toolButton_addmember.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_addmember.setObjectName("toolButton_addmember")
        self.verticalLayout.addWidget(self.toolButton_addmember)
        self.toolButton_viewbook = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton_viewbook.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.toolButton_viewbook.setFont(font)
        self.toolButton_viewbook.setStyleSheet("QToolButton{border-radius:11px;\n"
"background-color: rgb(146, 193, 255);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/viewbook .png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_viewbook.setIcon(icon5)
        self.toolButton_viewbook.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_viewbook.setCheckable(False)
        self.toolButton_viewbook.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_viewbook.setObjectName("toolButton_viewbook")
        self.verticalLayout.addWidget(self.toolButton_viewbook)
        self.toolButton_viewmember = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton_viewmember.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.toolButton_viewmember.setFont(font)
        self.toolButton_viewmember.setStyleSheet("QToolButton{border-radius:11px;\n"
"background-color: rgb(146, 193, 255);\n"
"}\n"
"QToolButton:hover{\n"
"background-color: rgb(255, 166, 139);\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/viewmembers.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_viewmember.setIcon(icon6)
        self.toolButton_viewmember.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_viewmember.setCheckable(False)
        self.toolButton_viewmember.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_viewmember.setObjectName("toolButton_viewmember")
        self.verticalLayout.addWidget(self.toolButton_viewmember)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LMS"))
        self.lineEdit_bookid.setPlaceholderText(_translate("MainWindow", "Please Enter Book ID"))
        self.label_bookname.setText(_translate("MainWindow", "Book Name"))
        self.label_bookauthor.setText(_translate("MainWindow", "Book Author"))
        self.lineEdit_memberid.setPlaceholderText(_translate("MainWindow", "Please Enter Member ID"))
        self.label_membername.setText(_translate("MainWindow", "Member Name"))
        self.label_contactinfo.setText(_translate("MainWindow", "Contact Info"))
        self.toolButton_issuebook.setText(_translate("MainWindow", "Issue Book"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Issue_book"))
        self.lineEdit_submission.setPlaceholderText(_translate("MainWindow", "Please Enter Book ID"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Member ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Issue Time"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "RenewCount"))
        self.toolButton_renew.setText(_translate("MainWindow", "Renew Book"))
        self.toolButton_submit.setText(_translate("MainWindow", "Submit Book"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Renew/Submission Book"))
        self.toolButton_addbook.setText(_translate("MainWindow", "Add Book"))
        self.toolButton_addmember.setText(_translate("MainWindow", "Add Member"))
        self.toolButton_viewbook.setText(_translate("MainWindow", "View Book"))
        self.toolButton_viewmember.setText(_translate("MainWindow", "View Member"))


