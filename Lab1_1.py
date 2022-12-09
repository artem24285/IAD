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
        self.Methods_middle_squares.clicked.connect(lambda: self.methods_2(self.Methods_middle_squares.text()))
        self.Test_1.clicked.connect( self.test_1)
        self.Test_2.clicked.connect(lambda: self.test_2(self.Test_2.text()))
        self.Clear.clicked.connect(lambda: self.methods_2(self.Clear.text()))
        self.Exit.clicked.connect(self.exit)


    @QtCore.pyqtSlot()
    def methods_1(self):
        deductions=methods_deductions.Deductions()
        methods=deductions.method(0.025,50)
        self.textEdit_data.setText(str(methods))


    def methods_2(self,text):
        self.textEdit_data_2.setText(text)


    def test_1(self):
        text = "Этот текст должен быть в окне приложение, а не консоли"
        self.textEdit_data_3.setText(text)


    def test_2(self, text):
        self.textEdit_data_4.setText(text)

    def clear(self):
        pass

    def exit(self):
        exit()




def main():
    app = QApplication(sys.argv)
    window = Methods_and_Test()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()