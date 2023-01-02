import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


form_secondwindow = uic.loadUiType("b.ui")[0]

class secondwindow (QMainWindow, form_secondwindow): # 데이터 추가창
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = secondwindow()
    myWindow.show()
    app.exec_()