from PyQt6.QtWidgets import QMainWindow , QDialog
from window import Ui_MainWindow
from addbook import Ui_Dialog
class LibrarySystem(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.toolButton_addbook.clicked.connect(self.add_book)
    def add_book(self):
        dialog = QDialog(self)
        ui = Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec()
 