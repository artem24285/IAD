import sys
from PyQt5.QtWidgets import *
from Information import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

if __name__=='__main__':
    form=QApplication([])
    form.setApplicationName('Information method')
    window=MainWindow()
    form.exec_()