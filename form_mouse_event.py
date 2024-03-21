"""
程式名稱：form_mouse_event1.py
程式功能：
1. 視窗滑鼠事件了解
"""
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QApplication)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('form_mouse_event.py')
        self.setGeometry(100, 100, 500, 300)
        #self.setMouseTracking(True)
        self.show()

    def leaveEvent(self, event):
        print('leaveEvent')

    def enterEvent(self, event):
        print('enterEvent')

    def mouseDoubleClickEvent(self, event):
        print('mouseDoubleClickEvent')

    def mousePressEvent(self, event):
        btn_event = event.button()
        match btn_event:
            case Qt.MouseButton.LeftButton:
                print('按了左鍵')
            case Qt.MouseButton.RightButton:
                print('按了右鍵')
            case Qt.MouseButton.MiddleButton:
                print('按了中鍵(滾輪)')
            case _:
                # 如電競滑鼠或其它側邊也有按鈕的滑鼠...
                # 因手邊沒有相關滑鼠，
                # 可能是Qt.MouseButton.ExtraButton(x)，x為數字，
                # 要測試才知道。
                print('按了滑鼠三鍵外的其它鍵')

    def mouseMoveEvent(self, event):
        print('mouseMoveEvent')

    def mouseReleaseEvent(self, event):
        print('mouseReleaseEvent')

    def wheelEvent(self, event):
        print('wheelEvent')

if __name__ == '__main__':
    app = QApplication()
    my_app = MyApp()

    sys.exit(app.exec())
