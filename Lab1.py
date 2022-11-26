import sys
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Information import Ui_MainWindow
import methods_deductions

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        global being_xi
        global N
        global massive
        global end_xi
        global g
        # self.pushButton.clicked.connect()
        # self.lineEdit.setText(str(first_meaning))
        # self.lineEdit_2.setText(str(first_meaning))
        def display(self):
            self.lcdNumber.display(self.stack[-1])

         #Класс Artem
        methods_deductions.methods(self,being_xi=being_xi,N=N,massive=massive)


        #Класс Marat



if __name__=='__main__':
    app=QApplication(sys.argv)
    window = MainWindow()
    app.setApplicationName('Information method')
    window.show()
    app.exec_()