import sys, fs, ss

from PyQt5.QtWidgets import QMainWindow, QRadioButton, QTableWidget, QTableWidgetItem, QLabel, QApplication


class FirstSep(fs.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SecondSep(ss.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SecondSep()
    ex.show()
    ex2 = FirstSep()
    ex2.show()
    sys.exit(app.exec())
