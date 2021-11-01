import sys
import fs
import ss
import sqlite3
import os

from PyQt5.QtWidgets import QMainWindow, QRadioButton, QTableWidget, QTableWidgetItem, QLabel, QApplication, QMessageBox


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
        self.pushButton_3.clicked.connect(lambda: self.addRow(1, [self.tableWidget.rowCount() + 1]))
        self.pushButton_4.clicked.connect(self.save)
        self.tableWidget.itemChanged.connect(self.change_item)
        self.modified = {}
        self.titles = []
        self.base_name = ""
        self.table_name = ""
        self.adding_row = False

    def getTable(self):
        if self.base_connection:
            self.base_connection.close()
        self.base_name = self.lineEdit.text()
        self.table_name = self.lineEdit_2.text()
        if not self.base_name or not self.table_name:
            self.label_18.setText("Вы ничего не ввели в одном/двух полях")
            return -1
        if not os.path.isfile("DataBases\\" + self.base_name + ".sqlite"):
            self.label_18.setText("Базы данных с таким названием нет")
            return -1
        self.base_connection = sqlite3.connect("DataBases\\" + self.base_name + ".sqlite")
        cursor = self.base_connection.cursor()
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + self.table_name + "'")
        if cursor.fetchone()[0] == 0:
            self.label_18.setText("Таблицы с таким названием нет")
            return -1
        self.label_4.setText(self.base_name)
        select_table = cursor.execute("SELECT * FROM " + self.table_name)
        self.tableWidget.setRowCount(0)
        columns_names = list(map(lambda x: x[0], cursor.description))
        self.tableWidget.setColumnCount(len(columns_names))
        self.tableWidget.setHorizontalHeaderLabels(columns_names)
        for e in select_table:
            self.tableWidget.itemChanged.connect(self.change_item)
            self.addRow(len(columns_names), e)
        self.titles = [description[0] for description in cursor.description]

    def addRow(self, column_count, row_cells):
        self.adding_row = True
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        for e in range(column_count):
            self.tableWidget.setItem(row_count, e, QTableWidgetItem(str(row_cells[e])))
        self.adding_row = False

    def change_item(self, item):
        if self.titles:
            if self.adding_row:
                self.modified["addRow"] = item.text()
            else:
                self.modified[self.titles[item.column()] + ":" + str(item.row())] = item.text()
            print(self.modified)

    def save(self):
        if self.modified:
            valid = QMessageBox.question(
                self, 'Сохранение', "Вы уверены, что хотите сохранить изменения?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                cursor = self.base_connection.cursor()
                titles_str = " ("
                for i in self.titles:
                    titles_str += i
                titles_str += ") "
                for i, v in self.modified.items():
                    if i == "addRow":
                        cursor.execute("INSERT INTO " + self.table_name + titles_str + "VALUES(" + v + ",'','')")
                        self.base_connection.commit()
                    else:
                        cursor.execute("UPDATE " + self.table_name + " SET " + i[:i.find(":")] + " = " + v
                                        + " WHERE id = " + i[i.find(":") + 1:])
                self.modified = {}
        else:
            QMessageBox.warning(self, 'Ошибка', "Изменений не обнаружено", QMessageBox.Ok)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SecondSep()
    ex2 = FirstSep()
    ex2.show()
    ex.show()
    sys.exit(app.exec())
