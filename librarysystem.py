from PyQt6.QtWidgets import QMainWindow , QDialog
from window import Ui_MainWindow
from addbook import Ui_Dialog
from addmember import Add_Member
from viewbooks import View_Books
from viewmembers import View_Members
class LibrarySystem(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.toolButton_addbook.clicked.connect(self.add_book)
        self.toolButton_addmember.clicked.connect(self.add_member)
        self.toolButton_viewbook.clicked.connect(self.view_books)
        self.toolButton_viewmember.clicked.connect(self.view_member)
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
