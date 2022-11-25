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

        # self.lineEdit.pressed.connect(self.label)
        # self.lineEdit_2.pressed.connect(self.label_2)
        # self.pushButton.pressed.connect(self.operations)
        # self.show()

        def display(self):
            self.lcdNumber.display(self.stack[-1])

        def operations(self):
            self.c=2+5
            self.display()

        def disc(self):
            pass

if __name__=='__main__':
    app=QApplication(sys.argv)
    window = MainWindow()
    app.setApplicationName('Information method')
    window.show()
    app.exec_()