import sys
import fs
import ss
import sqlite3
import os

from PyQt5.QtWidgets import QMainWindow, QRadioButton, QTableWidget, QTableWidgetItem, QLabel, QApplication


class FirstSep(fs.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SecondSep(ss.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.base_connection = None
        self.pushButton_2.clicked.connect(self.getTable)
        self.pushButton_3.clicked.connect(self.addRow)

    def getTable(self):
        if self.base_connection:
            self.base_connection.close()
        base_name = self.lineEdit.text()
        table_name = self.lineEdit_2.text()
        if not base_name or not table_name:
            self.label_18.setText("Вы ничего не ввели в одном/двух полях")
            return -1
        if not os.path.isfile("DataBases\\" + base_name + ".sqlite"):
            self.label_18.setText("База данных с таким названием не нашлась")
            return -1
        self.base_connection = sqlite3.connect("DataBases\\" + base_name + ".sqlite")
        cursor = self.base_connection.cursor()
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + table_name + "'")
        if cursor.fetchone()[0] == 0:
            self.label_18.setText("Таблица с таким названием не нашлась")
            return -1
        self.label_4.setText(base_name)
        select_table = cursor.execute("SELECT * FROM " + table_name)
        self.tableWidget.setRowCount(0)
        columns_names = list(map(lambda x: x[0], cursor.description))
        self.tableWidget.setColumnCount(len(columns_names))
        self.tableWidget.setHorizontalHeaderLabels(columns_names)

    def addRow(self):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        self.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(row_count + 1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SecondSep()
    ex2 = FirstSep()
    ex2.show()
    ex.show()
    sys.exit(app.exec())
