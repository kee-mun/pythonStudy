import sys
from PyQt5.QtWidgets import *

class myWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('이자율 계산기')
        self.move(300,300)
        self.resize(400,200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myWin()
    win.show()

    sys.exit(app.exec_())