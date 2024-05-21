from PyQt6.QtWidgets import QApplication
import sys
from librarysystem import LibrarySystem
app = QApplication(sys.argv)
library = LibrarySystem()
sys.exit(app.exec())