import sys
import fs
import ss
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QRadioButton, QTableWidget, QTableWidgetItem, QLabel, QApplication


class FirstSep(fs.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SecondSep(ss.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.getTable)

    def getTable(self):
        base_name = self.lineEdit.text()
        table_name = self.lineEdit_2.text()
        base_connection = sqlite3.connect("DataBases\\" + base_name + ".sqlite")
        cursor = base_connection.cursor()
        select_table = cursor.execute("SELECT * FROM " + table_name)
        self.tableWidget.setRowCount(0)
        columns_names = list(map(lambda x: x[0], cursor.description))
        print(len(columns_names))
        self.tableWidget.setColumnCount(len(columns_names))
        self.tableWidget.setHorizontalHeaderLabels(columns_names)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SecondSep()
    ex2 = FirstSep()
    ex2.show()
    ex.show()
    sys.exit(app.exec())
