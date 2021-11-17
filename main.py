import sys
import fs
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
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
            if suffix[::-1] == morpheme.body and (morpheme._type == "suffix" or morpheme._type == "all")\
                    and morpheme.part == part:
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
            if prefix == morpheme.body and (morpheme._type == "prefix" or morpheme._type == "all"):
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 0, 41, 16))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 481, 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(520, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 10, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(230, 10, 221, 31))
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(510, 50, 271, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(510, 110, 271, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(600, 570, 75, 41))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 63, 5);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(510, 170, 271, 61))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(510, 280, 271, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuTable = QtWidgets.QMenu(self.menubar)
        self.menuTable.setObjectName("menuTable")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_id = QtWidgets.QAction(MainWindow)
        self.action_id.setObjectName("action_id")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.menuTable.addAction(self.action)
        self.menuTable.addAction(self.action_2)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.action_id)
        self.menuTable.addAction(self.action_6)
        self.menuTable.addAction(self.action_7)
        self.menuTable.addAction(self.action_5)
        self.menuTable.addAction(self.action_4)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.action_10)
        self.menu.addAction(self.action_8)
        self.menubar.addAction(self.menuTable.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Таблица"))
        self.label_12.setText(_translate("MainWindow", "Работа с данными"))
        self.pushButton_2.setText(_translate("MainWindow", "Найти/обновить"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить строку"))
        self.pushButton_4.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_5.setText(_translate("MainWindow", "Сортировать id"))
        self.pushButton.setText(_translate("MainWindow", "Удалить выбранную строку"))
        self.pushButton_8.setText(_translate("MainWindow", "Выйти"))
        self.pushButton_6.setText(_translate("MainWindow", "Выгрузить таблицу"))
        self.pushButton_10.setText(_translate("MainWindow", "Загрузить данные языка"))
        self.label_5.setText(_translate("MainWindow", "Функции"))
        self.pushButton_7.setText(_translate("MainWindow", "Морфологический анализ"))
        self.pushButton_9.setText(_translate("MainWindow", "Анализ текста"))
        self.menuTable.setTitle(_translate("MainWindow", "Таблица"))
        self.menu.setTitle(_translate("MainWindow", "Функции"))
        self.action.setText(_translate("MainWindow", "Загрузить таблицу"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_2.setText(_translate("MainWindow", "Выгрузить таблицу"))
        self.action_2.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.action_id.setText(_translate("MainWindow", "Сортировать id"))
        self.action_id.setShortcut(_translate("MainWindow", "Shift+S"))
        self.action_4.setText(_translate("MainWindow", "Сохранить"))
        self.action_4.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_6.setText(_translate("MainWindow", "Добавить строку"))
        self.action_6.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.action_7.setText(_translate("MainWindow", "Удалить выбранную строку"))
        self.action_7.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.action_8.setText(_translate("MainWindow", "Морфологический анализ"))
        self.action_8.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.action_10.setText(_translate("MainWindow", "Выход"))
        self.action_3.setText(_translate("MainWindow", "Обновить таблицу"))
        self.action_3.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_5.setText(_translate("MainWindow", "Загрузить данные языка"))
        self.action_5.setShortcut(_translate("MainWindow", "Ctrl+L"))


class Alg_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(324, 330)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setEnabled(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_9.addWidget(self.lineEdit_8)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_6.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_4.addWidget(self.lineEdit_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_10.addWidget(self.lineEdit_9)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_11.addWidget(self.lineEdit_10)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Морфологический анализ"))
        self.label_6.setText(_translate("Form", "Слово"))
        self.label_2.setText(_translate("Form", "Часть речи"))
        self.label_7.setText(_translate("Form", "Корень"))
        self.label_8.setText(_translate("Form", "Приставка"))
        self.label_9.setText(_translate("Form", "Окончание"))
        self.label_10.setText(_translate("Form", "Суффикс"))
        self.label_11.setText(_translate("Form", "МФА"))
        self.label_3.setText(_translate("Form", "Число"))
        self.label_4.setText(_translate("Form", "Род"))
        self.pushButton_9.setText(_translate("Form", "Применить"))
        self.pushButton_7.setText(_translate("Form", "Загрузить в язык"))


class Text_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(478, 243)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 451, 111))
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 121, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 170, 111, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "                   Анализ текста."))
        self.label_2.setText(_translate("Form", "Количество слов:"))
        self.pushButton.setText(_translate("Form", "Провести анализ"))


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


class SecondSep(Ui_MainWindow, QMainWindow):
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
        select_morphemes = cursor.execute("SELECT body, type, part FROM Morphemes")
        for morpheme in select_morphemes:
            self.language.addMorpheme(morpheme[0], morpheme[1], morpheme[2])

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

    def check_if_letter(self, string):
        for ltr in self.language.alphabet.keys():
            if ltr in string:
                return True
        return False

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


class Algorithm(Alg_Form, QWidget):
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


class Text(Text_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.text_analysis)

    def text_analysis(self):
        text = self.lineEdit.text().split()
        words_count = 0
        for word in text:
            if ex.check_if_letter(word):
                words_count += 1
        self.label_2.setText("Количество слов: " + str(words_count))


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
