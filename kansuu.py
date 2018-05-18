import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt
import numpy as np


class Kansuu(QWidget):

    def __init__(self):
        super().__init__()

        self.mainUI()

    def mainUI(self):

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('かんすうくん')
        self.setWindowIcon(QIcon('img\icon.png'))

        self.radio1 = QRadioButton('一次関数')
        self.radio2 = QRadioButton('二次関数')

        self.group = QButtonGroup()
        self.group.addButton(self.radio1,1)
        self.group.addButton(self.radio2,2)
        self.radio1.toggle()
        
        hbox0 = QHBoxLayout()
        hbox0.addWidget(self.radio1)
        hbox0.addWidget(self.radio2)

        lbl_a = QLabel('aの値')
        self.a = QLineEdit(self)
        lbl_b = QLabel('bの値')
        self.b = QLineEdit(self)
        lbl_c = QLabel('cの値')
        self.c = QLineEdit(self)

        button = QPushButton("関数作成！", self)
        button.clicked.connect(self.buttonClicked)

        hbox = QHBoxLayout()
        hbox.addWidget(lbl_a)
        hbox.addWidget(self.a)
        hbox.addWidget(lbl_b)
        hbox.addWidget(self.b)
        hbox.addWidget(lbl_c)
        hbox.addWidget(self.c)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox)
        vbox.addWidget(button)
                
        self.setLayout(vbox)
        self.show()

    def buttonClicked(self):
        if self.radio1.isChecked()  == True:
            intA1 = int(self.a.text())
            intC1 = int(self.c.text())
            x1 = np.arange(0,10,0.1)
            y1 = intA1*x1 + intC1
            plt.scatter(x1,y1, label="y = " + str(intA1) + "x + " + str(intC1))
            plt.legend()
            plt.plot(x1,y1)
            plt.show()


        elif self.radio2.isChecked() == True:
            intA2 = int(self.a.text())
            intB2 = int(self.b.text())
            intC2 = int(self.c.text())
            x2 = np.arange(0,10,0.1)
            y2 = intA2*x2**2 + intB2*x2 + intC2
            plt.scatter(x2,y2, label="y = " + str(intA2) + "x^2 + " + str(intB2) + "x + " + str(intC2))
            plt.legend()
            plt.plot(x2,y2)
            plt.show()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    kansuu = Kansuu()
    sys.exit(app.exec_())

