from PyQt6.QtWidgets import QMainWindow , QDialog ,QMessageBox,QToolBar,QTableWidgetItem
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
        self.toolButton_issuebook.clicked.connect(self.issue_book)
        self.lineEdit_submission.returnPressed.connect(self.load_issue)
        self.toolButton_submit.clicked.connect(self.submmit_book)
        self.toolButton_renew.clicked.connect(self.renew_book)
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
    def issue_book(self):
        b_id = self.lineEdit_bookid.text()
        m_id = self.lineEdit_memberid.text()
        try:
            mydb = sqlite3.connect('DB.db')
            mycursor = mydb.cursor()
            query = "INSERT INTO issue (bookID, memberID) VALUES (?, ?)"
            query2 = "UPDATE addbook SET avail = FALSE WHERE id = ?"

            value = (b_id, m_id)
            mycursor.execute(query, value)
            mycursor.execute(query2, (b_id,))
            mydb.commit()
            mydb.close()
            QMessageBox.about(self, 'Book Issued', 'Book has been issued')
        except sqlite3.Error as error:
            pass
    def load_issue(self):
        issue_id = self.lineEdit_submission.text()
        try:
            mydb = sqlite3.connect('DB.db')
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM issue WHERE bookId = '"+issue_id+"'")
            myresult = mycursor.fetchall()
            mycursor.close()
            self.tableWidget.setRowCount(0)
            for number,data in enumerate(myresult):
                self.tableWidget.insertRow(number)
                for column,value in enumerate(data):
                    self.tableWidget.setItem(number, column, QTableWidgetItem(str(value)))
        except sqlite3.Error as error:
            pass
    def submmit_book(self):
        issue_id = self.lineEdit_submission.text()
        try:
            mydb = sqlite3.connect('DB.db')
            if issue_id=='':
                QMessageBox.about(self, 'Book Submission', 'Please enter book id')
                return
            mycursor = mydb.cursor()
            query = "DELETE FROM issue WHERE bookID = ?"
            query2 = "UPDATE addbook SET avail = TRUE WHERE id = ?"

            mycursor.execute(query, (issue_id,))

            # Execute the UPDATE query
            mycursor.execute(query2, (issue_id,))
            mydb.commit()
            QMessageBox.about(self, "Book Submission", "Book Submitted Successfully")

        except sqlite3.Error as error:
            print(error)
    def renew_book(self):
        issue_id = self.lineEdit_submission.text()
        try:
            mydb = sqlite3.connect('DB.db')
            if issue_id=='':
                QMessageBox.about(self, 'Book Submission', 'Please enter book id')
                return
            mycursor = mydb.cursor()
            query = "UPDATE issue SET issueTime = CURRENT_TIMESTAMP, renewCount=renewCount+1 WHERE bookID  = '" + issue_id + "'  "
            mycursor.execute(query)
            mydb.commit()
            QMessageBox.about(self, "Book Renew", "Book Renewed Successfully")
        except sqlite3.Error as error:
            pass