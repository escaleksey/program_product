from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QAbstractItemView
from .settings_page import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('static/ui/main_window.ui', self)  # Загружаем дизайн
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Вычисление корня')
        #self.setWindowIcon(QIcon('static/ui/icon.ico'))
        self.settings_button.clicked.connect(self.settings) # соединяем кнопку с функцией

    def settings(self):
        SettingWindow(self).show()