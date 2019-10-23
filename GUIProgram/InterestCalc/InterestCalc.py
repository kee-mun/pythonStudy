import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

class myWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('이자율 계산기')
        self.move(300,300)
        self.resize(400,200)

        exbtn = QPushButton("닫기", self)
        exbtn.move(150, 150)
        exbtn.resize(exbtn.sizeHint())
        exbtn.clicked.connect(QCoreApplication.instance().quit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myWin()
    win.show()

    sys.exit(app.exec_())