import sys
from data.pages.main_page import *
from data.logging import *


def main():
    app = QApplication(sys.argv)
    file = QtCore.QFile("static/styles/main.css")  # !!! dark.qss
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())
    window = MainWindow()
    window.show()
    sys.excepthook = exception_hook
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
