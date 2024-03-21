"""
程式名稱：form_event.py
程式功能：
1. 視窗本身相關事件了解
"""
import sys
from PySide6.QtGui import QFocusEvent
from PySide6.QtWidgets import (
    QWidget, QApplication)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('form_event.py')
        self.setGeometry(400, 250, 500, 300)
        self.show()

    def changeEvent(self, event):
        print('changeEvent')

    def closeEvent(self, event):
        print('closeEvent')

    def hideEvent(self, event):
        print('hideEvent')

    def moveEvent(self, event):
        print('moveEvent')

    def resizeEvent(self, event):
        print('resizeEvent')

    def showEvent(self, event):
        print('showEvent')

    def paintEvent(self, event):
        print('paintEvent')

if __name__ == '__main__':
    app = QApplication()
    my_app = MyApp()
    sys.exit(app.exec())
