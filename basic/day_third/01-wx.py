#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Графический интерфейс wxPython
#
#  https://wxpython.org/
#  https://pypi.org/project/wxPython/
#
#  Пример простой формы на wxWidgets с обработчиками
#
#  1. pip install wxPython - установка пакета
#  2. import wx - подключить в файле .py
#
import wx


class MainWindow(wx.Frame):
    """Основнок окно приложения wx"""

    button: wx.Button  # кнопка для изменения текста
    text_box: wx.TextCtrl  # поле для показа текста

    def __init__(self, *args, **kw):
        """Конструктор создания нового окна"""

        super(MainWindow, self).__init__(*args, **kw)  # вызываем родительский конструктор

        sizer = wx.BoxSizer(wx.VERTICAL)  # создаем Sizer для расстановки элементов

        # создаем кнопку и текстовое поле
        self.text_box = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.button = wx.Button(self, label="Test button")

        # добавляем элементы на Sizer с указанием параметров расположения
        sizer.Add(self.text_box, flags=wx.SizerFlags(1).Border(wx.ALL, 10).Expand())
        sizer.Add(self.button)

        # привязываем событие на нажатие кнопки
        self.button.Bind(wx.EVT_BUTTON, self.update_text)

        # размещаем Sizer в нашем окне
        self.SetSizer(sizer)

    def update_text(self, event):
        """Изменение текста в поле по нажатию на кнопку"""

        self.text_box.AppendText(f"Button clicked! {event}")


# создаем приложение
app = wx.App()
# создаем окно
frm = MainWindow(None, title='SkillBox')
# показываем окно
frm.Show()
# запускаем бесконечный цикл для отображения программы
app.MainLoop()
