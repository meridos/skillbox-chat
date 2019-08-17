#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Графический интерфейс PyQt 5
#
#  https://www.qt.io/
#  https://pypi.org/project/PyQt5/
#  https://build-system.fman.io/qt-designer-download
#
#  Пример простой формы на PyQt 5 с обработчиками
#
#  1. pip install PyQt5 - установка пакета
#  2. pip install qt5reactor - установка пакета
#  3. from PyQt5 import QtWidgets - подключить в файле .py
#
import sys
from PyQt5 import QtWidgets
from basic.day_third.design import window


class ExampleApp(QtWidgets.QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.update_text)

    def update_text(self, event):
        self.plainTextEdit.appendPlainText(f"Text updated: {event}")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
