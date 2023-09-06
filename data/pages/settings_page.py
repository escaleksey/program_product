import sys

from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox
from data.CONFIG import *

class SettingWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUi()


    def initUi(self):
        uic.loadUi('static/ui/settings.ui', self)
        self.setWindowTitle('Настройки')
        self.check_lang()
        self.buttonBox.accepted.connect(self.change_lang)
        self.ru.toggled.connect(self.onClicked)
        self.en.toggled.connect(self.onClicked)
        self.ch.toggled.connect(self.onClicked)
        self.sp.toggled.connect(self.onClicked)


    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.current_lang = radioButton.objectName()
            print(self.current_lang)

    def change_lang(self):
        global LAST_LANGUAGE
        LAST_LANGUAGE = self.current_lang

    def check_lang(self):  # Делает радио кнопку выбранного языка активной

        if LAST_LANGUAGE == 'ru':
            self.ru.setChecked(True)
            self.current_lang = 'ru'
        elif LAST_LANGUAGE == 'en':
            self.en.setChecked(True)
            self.current_lang = 'en'
        elif LAST_LANGUAGE == 'sp':
            self.sp.setChecked(True)
            self.current_lang = 'sp'
        elif LAST_LANGUAGE == 'ch':
            self.ch.setChecked(True)
            self.current_lang = 'ch'