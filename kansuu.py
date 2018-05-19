import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from matplotlib.font_manager import FontProperties
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
        self.radio3 = QRadioButton('三次関数')

        self.group = QButtonGroup()
        self.group.addButton(self.radio1,1)
        self.group.addButton(self.radio2,2)
        self.group.addButton(self.radio3,3)
        self.radio1.toggle()

        lbl_a = QLabel('aの値')
        self.a = QLineEdit(self)
        lbl_b = QLabel('bの値')
        self.b = QLineEdit(self)
        lbl_c = QLabel('cの値')
        self.c = QLineEdit(self)
        lbl_d = QLabel('dの値')
        self.d = QLineEdit(self)

        hbox0 = QHBoxLayout()
        hbox0.addWidget(self.radio1)
        hbox0.addWidget(self.radio2)
        hbox0.addWidget(self.radio3)

        button = QPushButton("関数作成！", self)
        button.clicked.connect(self.buttonClicked)

        hbox = QHBoxLayout()
        hbox.addWidget(lbl_a)
        hbox.addWidget(self.a)
        hbox.addWidget(lbl_b)
        hbox.addWidget(self.b)
        hbox.addWidget(lbl_c)
        hbox.addWidget(self.c)
        hbox.addWidget(lbl_d)
        hbox.addWidget(self.d)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox)
        vbox.addWidget(button)
                
        self.setLayout(vbox)
        self.show()

    def buttonClicked(self):

        fp = FontProperties(fname=r'C:\WINDOWS\Fonts\HGRSMP.TTF',size=14)

        if self.radio1.isChecked()  == True:
            intA = int(self.a.text())
            intC = int(self.c.text())
            x = np.arange(-10,10,0.1)
            y = intA*x + intC
            plt.title(u'一次関数のグラフ', fontproperties=fp)
            plt.plot(x,y, label="y=" + str(intA) + "x+" + str(intC))
            plt.legend()
            plt.show()

        elif self.radio2.isChecked() == True:
            intA = int(self.a.text())
            intB = int(self.b.text())
            intC = int(self.c.text())
            x = np.arange(-10,10,0.1)
            y = intA*x**2 + intB*x + intC
            plt.title(u'二次関数のグラフ', fontproperties=fp)
            plt.plot(x,y, label="y=" + str(intA) + "x^2+" + str(intB) + "x+" + str(intC))
            plt.legend()
            plt.show()

        elif self.radio3.isChecked() == True:
            intA = int(self.a.text())
            intB = int(self.b.text())
            intC = int(self.c.text())
            intD = int(self.d.text())
            x = np.arange(-10,10,0.1)
            y = intA*x**3 + intB*x**2 + intC*x + intD
            plt.title(u'三次関数のグラフ', fontproperties=fp)
            plt.plot(x,y, label="y=" + str(intA) + "x^3+" + str(intB) + "x^2+" + str(intC) + "x+" + str(intD))
            plt.legend()
            plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    kansuu = Kansuu()
    sys.exit(app.exec_())

