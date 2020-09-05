# -*- coding: UTF-8 -*-

#包
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QVBoxLayout
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt
import sys

class MainWindows(QWidget):
    def __init__(self):
        super().__init__()



        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('Newsroom')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)


        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        Window = QWidget()  # 用户界面父类
        Window.resize(1200, 900)
        Window.move(250, 150)
        Window.setWindowTitle('LYU Newsroom')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = MainWindows()
    Win.show()
    sys.exit(app.exec_())