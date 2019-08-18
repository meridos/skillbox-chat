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
    """Основное окно приложения Qt"""

    def __init__(self):
        """Конструктор окна"""

        super().__init__()  # вызываем родительский конструктор
        self.setupUi(self)  # вызываем метод построения интерфейса (из класс window.Ui_MainWindow)

        # привязываем событие по нажатию на кнопку
        self.pushButton.clicked.connect(self.update_text)

    def update_text(self, event):
        """Изменение текста при нажатии на кнопку"""

        self.plainTextEdit.appendPlainText(f"Text updated: {event}")


# создаем приложение
app = QtWidgets.QApplication(sys.argv)
# создаем окно
window = ExampleApp()
# показываем окно
window.show()
# запускаем бесконечный цикл для показа приложения
app.exec_()
