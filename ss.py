# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_sep.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(510, 280, 151, 23))
        self.pushButton_7.setObjectName("pushButton_7")
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
