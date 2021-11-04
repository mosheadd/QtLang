import sys
import fs
import ss
import algrthm
import sqlite3
import os

from PyQt5.QtWidgets import QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QLabel, QApplication, QMessageBox


class Change:
    def __init__(self, uid, body, period):
        self.uid = uid
        self.body = body
        self.period = period


class Language:
    def __init__(self, name):
        self.name = name
        self.roots = []
        self.prefixes = []
        self.suffixes = []
        self.endings = []
        self.changes = []

    def addMorpheme(self, morpheme, _type):
        if _type == "root" and morpheme not in self.roots:
            self.roots.append(morpheme)
        if _type == "prefix" and morpheme not in self.prefixes:
            self.prefixes.append(morpheme)
        if _type == "suffix" and morpheme not in self.suffixes:
            self.suffixes.append(morpheme)
        if _type == "ending" and morpheme not in self.endings:
            self.endings.append(morpheme)

    def add_change(self, change):
        if Change(change[0], change[1], change[2]) not in self.changes:
            self.changes.append(Change(change[0], change[1], change[2]))

    def word_alg(self, word):
        ending = ""
        suffix = ""
        root = ""
        prefix = ""
        morphemes = []
        for ltr in word[::-1]:
            ending += ltr
            if ending[::-1] in self.endings:
                ending = ending[::-1]
                break
        if ending == word[::-1]:
            ending = "Нулевое"
            end_gap = 0
        else:
            end_gap = len(ending)
        for ltr in word[-1 - end_gap::-1]:
            suffix += ltr
            if suffix[::-1] in self.suffixes:
                suffix = suffix[::-1]
                break
        if suffix == word[::-1 - end_gap]:
            suffix = "Нет"
            suf_gap = 0
        else:
            suf_gap = len(ending) + len(suffix)
        for ltr in word[-1 - suf_gap::-1]:
            root += ltr
            if root[::-1] in self.roots:
                root = root[::-1]
                break
        root_gap = len(ending) + len(suffix) + len(root)
        for ltr in word[-1 - root_gap::-1]:
            prefix += ltr
            if prefix[::-1] in self.prefixes:
                prefix = prefix[::-1]
                break
        if prefix == "":
            prefix = "Нет"
        return [root, prefix, suffix, ending]


class Algorithm(algrthm.Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_7.clicked.connect(self.load_changes)
        self.pushButton_9.clicked.connect(self.apply)
        self.language = None

    def load_changes(self):
        name = self.lineEdit.text()
        is_there = False
        if not name:
            QMessageBox.warning(self, 'Ошибка', "Вы не ввели название языка.", QMessageBox.Ok)
            return -1
        for lang in languages:
            if name == lang.name:
                is_there = True
                for chng in lang.changes:
                    print(chng.uid)
                    self.comboBox.addItem(str(chng.uid))
                self.language = lang
                break
        if not is_there:
            QMessageBox.warning(self, 'Ошибка', "Язык с таким названием не найден", QMessageBox.Ok)
            return -1

    def apply(self):
        name = self.lineEdit.text()
        if not self.language:
            is_there = False
            for lang in languages:
                if name == lang.name:
                    is_there = True
                    self.language = lang
                    break
            if not is_there:
                QMessageBox.warning(self, 'Ошибка', "Язык с таким названием не найден", QMessageBox.Ok)
                return -1
        morphemes = self.language.word_alg(self.lineEdit_3.text())
        self.lineEdit_4.setText(morphemes[0])
        self.lineEdit_5.setText(morphemes[1])
        self.lineEdit_6.setText(morphemes[3])
        self.lineEdit_7.setText(morphemes[2])


class FirstSep(fs.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SecondSep(ss.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.base_connection = None
        self.pushButton.clicked.connect(self.deleteRow)
        self.pushButton_2.clicked.connect(self.getTable)
        self.pushButton_3.clicked.connect(lambda: self.addRow(1, [self.tableWidget.rowCount() + 1]))
        self.pushButton_4.clicked.connect(self.save)
        self.pushButton_5.clicked.connect(self.sort_byId)
        self.pushButton_6.clicked.connect(self.unload_table)
        self.pushButton_7.clicked.connect(self.show_alg)
        self.pushButton_8.clicked.connect(self.quit)
        self.tableWidget.itemChanged.connect(self.change_item)
        self.modified = {}
        self.titles = []
        self.base_name = ""
        self.table_name = ""
        self.adding_row = False
        self.deleting_row = False
        self.new_table = False
        self.algorithm = None

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
        self.label_18.setText("")
        self.label_4.setText(self.base_name)
        select_table = cursor.execute("SELECT * FROM " + self.table_name)
        self.new_table = True
        self.tableWidget.setRowCount(0)
        columns_names = list(map(lambda x: x[0], cursor.description))
        self.tableWidget.setColumnCount(len(columns_names))
        self.tableWidget.setHorizontalHeaderLabels(columns_names)
        for e in select_table:
            self.tableWidget.itemChanged.connect(self.change_item)
            self.addRow(len(columns_names), e)
        self.new_table = False
        self.titles = [description[0] for description in cursor.description]
        if Language(self.base_name) not in languages:
            languages.append(Language(self.base_name))
        select_morphemes = cursor.execute("SELECT body, type FROM Morphemes")
        for morpheme in select_morphemes:
            languages[-1].addMorpheme(morpheme[0], morpheme[1])
        select_changes = cursor.execute("SELECT * FROM Changes")
        for change in select_changes:
            languages[-1].add_change(change)


    def addRow(self, column_count, row_cells):
        if self.base_connection is None:
            QMessageBox.warning(self, 'Ошибка', "Таблица не открыта", QMessageBox.Ok)
            return -1
        self.adding_row = True
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        for e in range(column_count):
            self.tableWidget.setItem(row_count, e, QTableWidgetItem(str(row_cells[e])))
        self.adding_row = False

    def change_item(self, item):
        if self.titles and not self.new_table:
            if self.adding_row:
                self.modified["addRow" + item.text()] = item.text()
            elif self.deleting_row:
                self.modified["delRow"] = item.text()
            else:
                self.modified[self.titles[item.column()] + ":" + str(item.row() + 1)] = item.text()

    def save(self):
        if self.base_connection is None:
            QMessageBox.warning(self, 'Ошибка', "Таблица не открыта", QMessageBox.Ok)
            return -1
        if self.modified:
            valid = QMessageBox.question(
                self, 'Сохранение', "Вы уверены, что хотите сохранить изменения?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                print(self.modified)
                cursor = self.base_connection.cursor()
                titles_str = " ("
                titles_str += ",".join(i for i in self.titles)
                titles_str += ") "
                for i, v in self.modified.items():
                    if i[:6] == "addRow":
                        values = "VALUES(" + v + ","
                        for title in range(len(self.titles) - 2):
                            values += "'',"
                        values += "'')"
                        print("INSERT INTO " + self.table_name + titles_str + values)
                        cursor.execute("INSERT INTO " + self.table_name + titles_str + values)
                    elif i == "delRow":
                        cursor.execute("DELETE FROM " + self.table_name + " WHERE id = ?", (v,))
                    else:
                        cursor.execute("UPDATE " + self.table_name + " SET '" + i[:i.find(":")] +
                                       "' = ? WHERE id = ?", (v, i[i.find(":") + 1:]))
                    self.base_connection.commit()
                self.modified = {}
        else:
            QMessageBox.warning(self, 'Ошибка', "Изменений не обнаружено", QMessageBox.Ok)
            return -1

    def deleteRow(self):
        if self.tableWidget.currentRow() == -1:
            QMessageBox.warning(self, 'Ошибка', "Вы не выбрали строку", QMessageBox.Ok)
            return -1
        if self.titles:
            deleting = QMessageBox.question(
                self, 'Удаление', "Вы уверены, что хотите удалить выбранную строку?",
                QMessageBox.Yes, QMessageBox.No)
            if deleting == QMessageBox.Yes:
                self.deleting_row = True
                cursor = self.base_connection.cursor()
                current_row = self.tableWidget.currentRow()
                self.modified["delRow"] = self.tableWidget.item(current_row, 0).text()
                self.tableWidget.removeRow(self.tableWidget.currentRow())
                # print(self.modified)
                self.deleting_row = False
        else:
            QMessageBox.warning(self, 'Ошибка', "Таблица не открыта", QMessageBox.Ok)
            return -1

    def sort_byId(self):
        for row in range(self.tableWidget.rowCount()):
            self.modified["id:" + self.tableWidget.item(row, 0).text()] = str(row + 1)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(row + 1)))

    def load_changes(self):
        if self.base_connection is None:
            QMessageBox.warning(self, 'Ошибка', "Таблица не открыта", QMessageBox.Ok)
            return -1
        cursor = self.base_connection.cursor()
        select_changes = cursor.execute("SELECT id FROM Changes")
        for change in select_changes:
            self.comboBox.addItem(str(change[0]))

    def unload_table(self):
        if self.base_connection is None:
            QMessageBox.warning(self, 'Ошибка', "Таблица не открыта", QMessageBox.Ok)
            return -1
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.base_connection.close()
        self.base_connection = None
        self.table_name = ""
        self.base_name = ""

    def quit(self):
        does_quit = QMessageBox.question(
            self, 'Выход', "Вы уверены, что хотите выйти?",
            QMessageBox.Yes, QMessageBox.No)
        if does_quit == QMessageBox.Yes:
            if self.base_connection:
                self.base_connection.close()
                self.base_connection = None
            sys.exit(app.exec())

    def show_alg(self):
        if not self.algorithm:
            self.algorithm = Algorithm()
        self.algorithm.show()


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


languages = []
sys.excepthook = exception_hook
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SecondSep()
    ex.show()
    sys.exit(app.exec())
