from PyQt6.QtWidgets import QMainWindow , QDialog
from window import Ui_MainWindow
from addbook import Ui_Dialog
from addmember import Add_Member
from viewbooks import View_Books
from viewmembers import View_Members
import sqlite3
class LibrarySystem(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.toolButton_addbook.clicked.connect(self.add_book)
        self.toolButton_addmember.clicked.connect(self.add_member)
        self.toolButton_viewbook.clicked.connect(self.view_books)
        self.toolButton_viewmember.clicked.connect(self.view_member)
        self.lineEdit_bookid.returnPressed.connect(self.book_id)
        self.lineEdit_memberid.returnPressed.connect(self.member_id)
    def add_book(self):
        dialog = QDialog(self)
        ui = Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec()
    def add_member(self):
        dialog = QDialog(self)
        ui = Add_Member()
        ui.setupUi(dialog)
        dialog.exec()
    def view_books(self):
        dialog = QDialog(self)
        ui = View_Books()
        ui.setupUi(dialog)
        dialog.exec()
    def view_member(self):
        dialog = QDialog(self)
        ui = View_Members()
        ui.setupUi(dialog)
        dialog.exec()
    def book_id(self):
        id = self.lineEdit_bookid.text()
        try:
            mydb = sqlite3.connect('DB.db')
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM addbook WHERE id = '"+id+"'")
            myresult = mycursor.fetchall()
            for row in myresult:
                self.label_bookname.setText(f"Book Name :{row[0]}")
                self.label_bookauthor.setText(f"Author :{row[1]}")
        except sqlite3.Error as error:
            pass

    def member_id(self):
        member = self.lineEdit_memberid.text()
        try:
            mydb = sqlite3.connect('DB.db')
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM addmember WHERE id = '" + member + "'")
            myresult = mycursor.fetchall()
            for row in myresult:
                self.label_membername.setText(f"Member Name :{row[1]}")
                self.label_contactinfo.setText(f"Contact Info :{row[3]}")
        except sqlite3.Error as error:
            pass