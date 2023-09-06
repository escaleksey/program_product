import sys
from data.pages.main_page import *
from data.logging import *

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.excepthook = exception_hook
    sys.exit(app.exec())


if __name__ == '__main__':
    main()