from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

import data.CONFIG as CNF
from json import load

from data.calculate import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('static/ui/main_window.ui', self)  # Загружаем дизайн
        self.initUi()

    def initUi(self):
        self.setWindowIcon(QIcon('static/images/icon.ico'))  # Иконка
        self.check_lang()  # проверяем текущий язык
        self.ru.toggled.connect(self.onClicked)  # подключаем radiobutton
        self.en.toggled.connect(self.onClicked)
        self.ch.toggled.connect(self.onClicked)
        self.sp.toggled.connect(self.onClicked)



        self.translate()
        self.result_button.clicked.connect(lambda: result_calculate(self)) #Подключение функции калькулятора к кнопке
        '''В self.input_number будет приходить значение пользователя,
            В self.output_number оно должно выводиться Это QLineEdit, погугли как брать текст из них и как вписывать
            В self.decimal_places значение цифр после запятой, при -1 ограничение убирается QSpinBox погугли)
            Комбобокс возвращает индекс self.comboBox
            '''

    def translate(self):  # перевод текста
        with open(f"static/lang/{CNF.LAST_LANGUAGE}.json", "r", encoding='UTF-8') as file:
            self.lang_dict = load(file)
        self.setWindowTitle(self.lang_dict["words"]["title"])
        self.enter_number_text.setText(self.lang_dict["words"]["enter_number_text"])
        self.enter_decimal_text.setText(self.lang_dict["words"]["enter_decimal_text"])
        self.enter_decimal_text_2.setText(self.lang_dict["words"]["enter_decimal_text_2"])
        self.result_button.setText(self.lang_dict["words"]["result_button"])
        self.comboBox.clear()
        self.comboBox.addItem(self.lang_dict["words"]["comboBox1"])
        self.comboBox.addItem(self.lang_dict["words"]["comboBox2"])
        self.comboBox.addItem(self.lang_dict["words"]["comboBox3"])


    def onClicked(self):  # запускается при выборе нового языка
        radioButton = self.sender()
        if radioButton.isChecked():
            self.current_lang = radioButton.objectName()
            self.change_lang()

    def change_lang(self):
        CNF.LANGUAGE_JSON = self.current_lang
        CNF.LAST_LANGUAGE = CNF.LANGUAGE_JSON
        self.set_json()

    def set_json(self):  # Изменение языка в файле ( чтобы сохранялся после перезахода )
        f = open("static/lang/last_lang.txt", "w")
        f.write(CNF.LAST_LANGUAGE)
        f.close()
        self.translate()

    def check_lang(self):  # Делает радио кнопку выбранного языка активной
        if CNF.LAST_LANGUAGE == 'ru':
            self.ru.setChecked(True)
            self.current_lang = 'ru'
        elif CNF.LAST_LANGUAGE == 'en':
            self.en.setChecked(True)
            self.current_lang = 'en'
        elif CNF.LAST_LANGUAGE == 'sp':
            self.sp.setChecked(True)
            self.current_lang = 'sp'
        elif CNF.LAST_LANGUAGE == 'ch':
            self.ch.setChecked(True)
            self.current_lang = 'ch'

