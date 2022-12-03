import os
import sys

import PyQt5.QtSvg
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi

import methods_deductions

class Methods_and_Test(QDialog):
    def __init__(self):
        super(Methods_and_Test,self).__init__()
        loadUi('IAD.ui',self)
        self.Return=0
        self.setWindowTitle('Методы')

        self.Methods_deductions.clicked.connect(self.methods_1)
        self.Methods_middle_squares.clicked.connect(self.methods_2)


    @QtCore.pyqtSlot()
    def methods_1(self):
        deductions=methods_deductions.Deductions()
        xi = 0.25
        N = 25
        self.groupBox.setText("Hello!")

    def methods_2(self):
        pass




def main():
    app = QApplication(sys.argv)
    window = Methods_and_Test()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()