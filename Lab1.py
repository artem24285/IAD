import sys
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Information import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        global being_xi
        global N
        # self.pushButton.clicked.connect()
        # self.lineEdit.setText(str(first_meaning))
        # self.lineEdit_2.setText(str(first_meaning))
        def display(self):
            self.lcdNumber.display(self.stack[-1])
        class methods_deductions():
            def __init__(self):
                pass
        class methods_the_middle_of_the_squares():
            def __init__(self):
                pass

if __name__=='__main__':
    app=QApplication(sys.argv)
    window = MainWindow()
    app.setApplicationName('Information method')
    window.show()
    app.exec_()