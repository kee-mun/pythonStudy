import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

class myWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.time = "Month"
        self.result = 0
        self.setWindowTitle('이자율 계산기')
        self.move(300,300)
        self.resize(400,200)

        #####기간 선택하기 (월/년)
        self.lbl = QLabel(self)
        self.lbl.setText("1.   기간 :")
        self.lbl.move(0,0)
        self.lbl.resize(70,20)

        self.tiEdit = QLineEdit("",self)
        self.tiEdit.move(85,0)
        self.tiEdit.resize(55,20)
        self.tiEdit.textChanged.connect(self.setTi)

        self.opcb = QComboBox(self)
        self.opcb.move(145,0)
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
        self.tiEdit2.resize(55,20)
        self.tiEdit2.textChanged.connect(self.setInterestRate)

        self.lbl2_2 = QLabel(self)
        self.lbl2_2.setText("%")
        self.lbl2_2.move(145,25)
        self.lbl2_2.resize(80,20)

        #####월 납입액
        self.lbl3 = QLabel(self)
        self.lbl3.setText("3. 납입액 :")
        self.lbl3.move(0,50)
        self.lbl3.resize(80,20)

        self.tiEdit3 = QLineEdit("",self)
        self.tiEdit3.move(85,50)
        self.tiEdit3.resize(55,20)
        self.tiEdit3.textChanged.connect(self.setMoney)

        self.lbl3_2 = QLabel(self)
        self.lbl3_2.setText("원")
        self.lbl3_2.move(145,50)
        self.lbl3_2.resize(80,20)

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

    def setMoney(self):
        self.money = int(self.tiEdit3.text())

    def showResult(self):
        msg = QMessageBox()
        msg.setWindowTitle("원금 및 이자")
        message = "만기시 : {0} 원".format(int(self.result))
        msg.setText(message)

        x = msg.exec_()

    def calc(self):
        if self.time == "Month":
            interestRate = self.interestRate / 1200
            self.result = self.money * self.Ti  + self.money * interestRate * ((self.Ti + 1) * self.Ti / 2)
            self.showResult()
        else:
            Ti = self.Ti * 12
            interestRate = self.interestRate / 1200
            self.result = self.money * Ti  + self.money * interestRate * ((Ti + 1) * Ti / 2)
            self.showResult()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myWin()
    win.show()

    sys.exit(app.exec_())