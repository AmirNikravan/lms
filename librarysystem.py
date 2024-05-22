from PyQt6.QtWidgets import QMainWindow , QDialog
from window import Ui_MainWindow
from addbook import Ui_Dialog
from addmember import Add_Member
class LibrarySystem(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.toolButton_addbook.clicked.connect(self.add_book)
        self.toolButton_addmember.clicked.connect(self.add_member)
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