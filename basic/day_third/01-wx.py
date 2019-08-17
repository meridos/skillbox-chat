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
    button: wx.Button
    text_box: wx.TextCtrl

    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text_box = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.button = wx.Button(self, label="Test button")

        sizer.Add(self.text_box, flags=wx.SizerFlags(1).Border(wx.ALL, 10).Expand())
        sizer.Add(self.button)

        self.button.Bind(wx.EVT_BUTTON, self.update_text)

        self.SetSizer(sizer)

    def update_text(self, event):
        self.text_box.AppendText(f"Button clicked! {event}")


app = wx.App()
frm = MainWindow(None, title='SkillBox')
frm.Show()
app.MainLoop()
