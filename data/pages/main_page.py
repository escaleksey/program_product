from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import data.CONFIG as CNF
from json import load
from data.utils.language_utils import *
from data.calculate import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('static/ui/main_window.ui', self)  # Загружаем дизайн
        self.list_languages = get_list_languages()
        self.initUi()

    def initUi(self):
        self.setWindowIcon(QIcon('static/images/icon.ico'))  # Иконка
        self.fill_lang_combobox()
        self.translate()
        self.result_button.clicked.connect(lambda: result_calculate(self)) #Подключение функции калькулятора к кнопке
        self.lang_combox.currentIndexChanged.connect(self.apply_settings)
        self.reverse_button.clicked.connect(self.reverse)
        self.check_language()

    def reverse(self):
        before_lang = self.current_lang
        self.list_languages = get_list_languages()
        self.fill_lang_combobox()
        self.current_lang = before_lang
        CNF.LANGUAGE_JSON = self.current_lang
        CNF.LAST_LANGUAGE = CNF.LANGUAGE_JSON
        self.check_language()
        self.output_number1.setText("")
        self.output_number2.setText("")
        self.input_number.setText("")

    def apply_settings(self):
        self.current_lang = self.list_languages[self.lang_combox.currentIndex()]
        self.change_lang()

    def fill_lang_combobox(self):
        self.lang_combox.clear()
        names = get_names_of_languages()
        for lang in names:
            self.lang_combox.addItem(lang)

    def translate(self):  # перевод текста
        with open(f"static/lang/{CNF.LAST_LANGUAGE}.json", "r", encoding='UTF-8') as file:
            self.lang_dict = load(file)
        self.setWindowTitle(self.lang_dict["words"]["title"])
        self.enter_number_text.setText(self.lang_dict["words"]["enter_number_text"])
        self.enter_decimal_text.setText(self.lang_dict["words"]["enter_decimal_text"])
        self.remove_limit.setText(self.lang_dict["words"]["enter_decimal_text_2"])
        self.result_button.setText(self.lang_dict["words"]["result_button"])
        self.comboBox.clear()
        self.comboBox.addItem(self.lang_dict["words"]["comboBox1"])
        self.comboBox.addItem(self.lang_dict["words"]["comboBox2"])
        self.comboBox.addItem(self.lang_dict["words"]["comboBox3"])
        self.error_massage = self.lang_dict["words"]["error"]

    def change_lang(self):
        CNF.LANGUAGE_JSON = self.current_lang
        CNF.LAST_LANGUAGE = CNF.LANGUAGE_JSON
        self.set_json()

    def set_json(self):  # Изменение языка в файле ( чтобы сохранялся после перезахода )
        f = open("static/lang/last_lang.txt", "w")
        f.write(CNF.LAST_LANGUAGE)
        f.close()
        self.translate()

    def check_language(self):
        self.lang_combox.setCurrentIndex(self.list_languages.index(CNF.LAST_LANGUAGE))

