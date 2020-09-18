
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


from MainWindows import Ui_MainWindow


if __name__=="__main__":
    app = QApplication(sys.argv)
    # 创建主窗口对象
    window = QMainWindow()
    # 创建主窗口界面对象
    ui = Ui_MainWindow()
    # 传递主窗口对象
    ui.setupUi(window)
    # 调用show方法显示主窗口
    window.show()
    sys.exit(app.exec())