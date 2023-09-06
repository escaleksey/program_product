from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QAbstractItemView
from .settings_page import *
from data.CONFIG import *
from json import load

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('static/ui/main_window.ui', self)  # Загружаем дизайн
        self.initUi()



    def initUi(self):

        #self.setWindowIcon(QIcon('static/ui/icon.ico'))
        self.settings_button.clicked.connect(self.settings) # соединяем кнопку с функцией
        self.translate()

    def settings(self):
        self.settings_window = SettingWindow(self)
        self.settings_window.show()


    def translate(self): # перевод текста
        with open(f"static/lang/{LAST_LANGUAGE}.json", "r", encoding='UTF-8') as file:
            self.lang_dict = load(file)
        self.setWindowTitle(self.lang_dict["words"]["title"])
        self.enter_number_text.setText(self.lang_dict["words"]["enter_number_text"])
        self.enter_decimal_text.setText(self.lang_dict["words"]["enter_decimal_text"])
        self.enter_decimal_text_2.setText(self.lang_dict["words"]["enter_decimal_text_2"])
        self.result_button.setText(self.lang_dict["words"]["result_button"])

