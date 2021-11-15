import sys
import fs
import ss
import algrthm
import txt
import sqlite3
import os

from PyQt5.QtWidgets import QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QLabel, QApplication, QMessageBox


def word_alg(word, part):
    ending = ""
    suffix = ""
    prefix = ""
    gender = "Нет"
    form = "Нет"
    do_break = False
    for ltr in word[::-1]:
        ending += ltr
        for morpheme in ex.language.morphemes:
            if ending[::-1] == morpheme.body and morpheme._type[:6] == "ending" and morpheme.part == part:
                ending = ending[::-1]
                if morpheme.part in ("noun", "adjective"):
                    gender = ex.language.endings_gender[ending][:4]
                    form = ex.language.endings_gender[ending][5:]
                do_break = True
                break
        if do_break:
            break
    do_break = False
    if ending == word[::-1]:
        ending = "Нулевое"
        end_gap = 0
    else:
        end_gap = len(ending)
    for ltr in word[-1 - end_gap::-1]:
        suffix += ltr
        for morpheme in ex.language.morphemes:
            if suffix[::-1] == morpheme.body and morpheme._type == "suffix" and morpheme.part == part:
                suffix = suffix[::-1]
                do_break = True
                break
        if do_break:
            break
    if suffix == word[-1 - end_gap::-1]:
        suffix = "Нет"
        suf_gap = 0
    else:
        suf_gap = len(suffix)
    do_break = False
    for ltr in word:
        prefix += ltr
        for morpheme in ex.language.morphemes:
            if prefix == morpheme.body and morpheme._type == "prefix":
                do_break = True
                break
        if do_break:
            break
    if prefix == word:
        prefix = "Нет"
        pre_gap = 0
    else:
        pre_gap = len(prefix)
    root = word[pre_gap:len(word) - suf_gap - end_gap]
    ipa_word = "["
    for letter in word.lower():
        for k, v in ex.language.alphabet.items():
            if k == letter:
                ipa_word += v
    return [root, prefix, suffix, ending, ipa_word + "]", form, gender]


class Change:
    def __init__(self, uid, body, period):
        self.uid = uid
        self.body = body
        self.period = period


class Morpheme:
    def __init__(self, body, _type, part):
        self.body = body
        self._type = _type
        self.part = part



class Language:
    def __init__(self, name):
        self.name = name
        self.roots = []
        self.morphemes = []
        self.morphemes_bodies = []
        self.prefixes = []
        self.suffixes = []
        self.endings_gender = {}
        self.changes = []
        self.alphabet = {}

    def addMorpheme(self, morpheme, _type, part):
        if Morpheme(morpheme, _type, part) not in self.morphemes:
            self.morphemes.append(Morpheme(morpheme, _type, part))
        if _type[:6] == "ending" and len(_type) > 6:
            self.endings_gender[morpheme] = _type[7:11] + ":" + _type[12:]


    def add_change(self, change):
        if Change(change[0], change[1], change[2]) not in self.changes:
            self.changes.append(Change(change[0], change[1], change[2]))

    def add_letter(self, letter):
        if letter[1] not in self.alphabet.keys():
            self.alphabet[letter[1]] = letter[2]


class FirstSep(fs.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SecondSep(ss.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.base_connection = sqlite3.connect("DataBases\\Test.sqlite")
        self.pushButton.clicked.connect(self.deleteRow)
        self.pushButton_2.clicked.connect(self.getTable)
        self.pushButton_3.clicked.connect(lambda: self.addRow(1, [self.tableWidget.rowCount() + 1]))
        self.pushButton_4.clicked.connect(self.save)
        self.pushButton_5.clicked.connect(self.sort_byId)
        self.pushButton_6.clicked.connect(self.unload_table)
        self.pushButton_7.clicked.connect(self.show_alg)
        self.pushButton_8.clicked.connect(self.quit)
        self.pushButton_10.clicked.connect(self.loadLanguage)
        self.action.triggered.connect(self.getTable)
        self.action_2.triggered.connect(self.unload_table)
        self.action_id.triggered.connect(self.sort_byId)
        self.action_6.triggered.connect(self.addRow)
        self.action_7.triggered.connect(self.deleteRow)
        self.action_4.triggered.connect(self.save)
        self.action_5.triggered.connect(self.loadLanguage)
        self.action_8.triggered.connect(self.show_alg)
        self.action_10.triggered.connect(self.quit)
        self.tableWidget.itemChanged.connect(self.change_item)
        self.modified = {}
        self.titles = []
        self.base_name = ""
        self.table_name = ""
        self.adding_row = False
        self.deleting_row = False
        self.new_table = False
        self.algorithm = None
        self.text = None
        self.language = None

    def setLanguage(self):
        self.language = Language("Test")

    def loadLanguage(self):
        self.setLanguage()
        cursor = self.base_connection.cursor()
        select_alphabet = cursor.execute("SELECT * FROM Alphabet")
        for ltr in select_alphabet:
            self.language.add_letter(ltr)

    def getTable(self):
        self.setLanguage()
        self.table_name = self.lineEdit_2.text()
        if not self.table_name:
            self.label_18.setText("Вы ничего не ввели в поле")
            return -1
        cursor = self.base_connection.cursor()
        cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + self.table_name + "'")
        if cursor.fetchone()[0] == 0:
            self.label_18.setText("Таблицы с таким названием нет")
            return -1
        self.label_18.setText("")
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
        select_morphemes = cursor.execute("SELECT body, type, part FROM Morphemes")
        for morpheme in select_morphemes:
            self.language.addMorpheme(morpheme[0], morpheme[1], morpheme[2])
        select_alphabet = cursor.execute("SELECT * FROM Alphabet")
        for ltr in select_alphabet:
            self.language.add_letter(ltr)


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
        if not self.lineEdit_2.text():
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
                current_row = self.tableWidget.currentRow()
                self.modified["delRow"] = self.tableWidget.item(current_row, 0).text()
                self.tableWidget.removeRow(self.tableWidget.currentRow())
                self.deleting_row = False
        else:
            QMessageBox.warning(self, 'Ошибка', "Таблица не открыта", QMessageBox.Ok)
            return -1

    def sort_byId(self):
        for row in range(self.tableWidget.rowCount()):
            self.modified["id:" + self.tableWidget.item(row, 0).text()] = str(row + 1)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(row + 1)))

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


class Russian(SecondSep):
    def __init__(self):
        super().__init__()
        self.pushButton_7.clicked.connect(self.show_alg)
        self.pushButton_9.clicked.connect(self.show_text)
        self.base_connection = sqlite3.connect("DataBases\\Russian.sqlite")

    def setLanguage(self):
        self.language = Language("Russian")

    def loadLanguage(self):
        self.setLanguage()
        cursor = self.base_connection.cursor()
        select_morphemes = cursor.execute("SELECT body, type, part FROM Morphemes")
        for morpheme in select_morphemes:
            self.language.addMorpheme(morpheme[0], morpheme[1], morpheme[2])
        select_alphabet = cursor.execute("SELECT * FROM Alphabet")
        for ltr in select_alphabet:
            self.language.add_letter(ltr)


    def word_alg(self, word, part):
        ending = ""
        suffix = ""
        prefix = ""
        gender = "Нет"
        form = "Нет"
        do_break = False
        for ltr in word[::-1]:
            ending += ltr
            for morpheme in self.language.morphemes:
                if ending[::-1] == morpheme.body and morpheme._type[:6] == "ending" and morpheme.part == part:
                    ending = ending[::-1]
                    if morpheme.part in ("noun", "adjective"):
                        gender = self.endings_gender[ending][:4]
                        form = self.endings_gender[ending][5:]
                    do_break = True
                    break
            if do_break:
                break
        do_break = False
        if ending == word[::-1]:
            ending = "Нулевое"
            end_gap = 0
        else:
            end_gap = len(ending)
        for ltr in word[-1 - end_gap::-1]:
            suffix += ltr
            for morpheme in self.language.morphemes:
                if suffix[::-1] == morpheme.body and morpheme._type == "suffix" and morpheme.part == part:
                    suffix = suffix[::-1]
                    do_break = True
                    break
            if do_break:
                break
        if suffix == word[-1 - end_gap::-1]:
            suffix = "Нет"
            suf_gap = 0
        else:
            suf_gap = len(suffix)
        do_break = False
        for ltr in word:
            prefix += ltr
            for morpheme in self.language.morphemes:
                if prefix == morpheme.body and morpheme._type == "prefix":
                    do_break = True
                    break
            if do_break:
                break
        if prefix == word:
            prefix = "Нет"
            pre_gap = 0
        else:
            pre_gap = len(prefix)
        root = word[pre_gap:len(word) - suf_gap - end_gap]
        ipa_word = "["
        for letter in word.lower():
            for k, v in self.alphabet.items():
                if k == letter:
                    ipa_word += v
        return [root, prefix, suffix, ending, ipa_word + "]", form, gender]

    def show_alg(self):
        if not self.algorithm:
            self.algorithm = Algorithm()
        self.algorithm.show()

    def show_text(self):
        if not self.text:
            self.text = Text()
        self.text.show()


class Algorithm(algrthm.Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_7.clicked.connect(self.load_to_lang)
        self.pushButton_9.clicked.connect(self.apply)
        self.language = None

    def load_to_lang(self):
        connection = sqlite3.connect("DataBases\\Russian.sqlite")
        cursor = connection.cursor()
        w_id = len(cursor.execute("SELECT * FROM Words").fetchall()) + 1
        word = self.lineEdit_3.text()
        part = self.lineEdit_8.text()
        root = self.lineEdit_4.text()
        prefix = self.lineEdit_5.text()
        ending = self.lineEdit_6.text()
        suffix = self.lineEdit_7.text()
        ipa = self.lineEdit_2.text()
        form = self.lineEdit_9.text()
        gender = self.lineEdit_10.text()
        cursor.execute("INSERT INTO Words(id,word,partofspeech,ipa,root,prefix,suffix,ending,gender,form) VALUES"
                       " (?,?,?,?,?,?,?,?,?,?)", (w_id, word, part, ipa, root, prefix, suffix, ending, gender,
                                                  form)).fetchall()
        connection.commit()
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_5.setDisabled(True)
        self.lineEdit_6.setDisabled(True)
        self.lineEdit_7.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_9.setDisabled(True)
        self.lineEdit_10.setDisabled(True)

    def apply(self):
        part = self.lineEdit_8.text()
        word = self.lineEdit_3.text()
        morphemes = word_alg(word, part)
        self.lineEdit_4.setText(morphemes[0])
        self.lineEdit_5.setText(morphemes[1])
        self.lineEdit_6.setText(morphemes[3])
        self.lineEdit_7.setText(morphemes[2])
        self.lineEdit_2.setText(morphemes[4])
        self.lineEdit_9.setText(morphemes[5])
        self.lineEdit_10.setText(morphemes[6])
        self.lineEdit_4.setDisabled(False)
        self.lineEdit_5.setDisabled(False)
        self.lineEdit_6.setDisabled(False)
        self.lineEdit_7.setDisabled(False)
        self.lineEdit_2.setDisabled(False)
        self.lineEdit_9.setDisabled(False)
        self.lineEdit_10.setDisabled(False)


class Text(txt.Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.text_analysis)

    def text_analysis(self):
        text = self.lineEdit.text().split()
        self.label_2.setText("Количество слов: " + str(len(text)))


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


languages = []
sys.excepthook = exception_hook
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Russian()
    ex.show()
    sys.exit(app.exec())
