import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

class myWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.time = "Month"
        self.setWindowTitle('이자율 계산기')
        self.move(300,300)
        self.resize(400,200)

        #####기간 선택하기 (월/년)
        self.lbl = QLabel(self)
        self.lbl.setText("1.  기간 :")
        self.lbl.move(0,0)
        self.lbl.resize(70,20)

        self.tiEdit = QLineEdit("",self)
        self.tiEdit.move(75,0)
        self.tiEdit.resize(45,20)
        self.tiEdit.textChanged.connect(self.setTi)

        self.opcb = QComboBox(self)
        self.opcb.move(125,0)
        self.opcb.addItem("Month")
        self.opcb.addItem("Year")
        self.opcb.currentIndexChanged.connect(self.setTime)

        #####이자율 입력
        self.lbl2 = QLabel(self)
        self.lbl2.setText("2. 연이율 :")
        self.lbl2.move(0,25)
        self.lbl2.resize(80,20)

        self.tiEdit2 = QLineEdit("",self)
        self.tiEdit2.move(85,25)
        self.tiEdit2.resize(45,20)
        self.tiEdit2.textChanged.connect(self.setInterestRate)

        self.lbl2_2 = QLabel(self)
        self.lbl2_2.setText("%")
        self.lbl2_2.move(135,25)
        self.lbl2_2.resize(80,20)

        exbtn1 = QPushButton("닫기", self)
        exbtn1.move(190, 150)
        exbtn1.resize(exbtn1.sizeHint())
        exbtn1.clicked.connect(QCoreApplication.instance().quit)

        exbtn2 = QPushButton("계산", self)
        exbtn2.move(110, 150)
        exbtn2.resize(exbtn2.sizeHint())
        exbtn2.clicked.connect(self.calc)

    def setTime(self):
        self.time = self.opcb.currentText()

    def setTi(self):
        self.Ti = int(self.tiEdit.text())

    def setInterestRate(self):
        self.interestRate = int(self.tiEdit2.text())

    def calc(self):
        print(self.interestRate, self.time, self.Ti)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myWin()
    win.show()

    sys.exit(app.exec_())