import pymysql
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *


# uic 연결
form_secondwindow = uic.loadUiType("data/town.ui")[0]

# # 데이터 파일 불러오기
# cursor.execute('SELECT * FROM gwangju_ath')

# 화면 연결
class town(QMainWindow, form_secondwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('잘살아보자 우리동네찾기')  # 프로그램의 타이틀
        self.comboBox.currentTextChanged.connect(self.show1)
        self.comboBox_2.currentTextChanged.connect(self.show2)
        self.comboBox_3.currentTextChanged.connect(self.show3)
        self.comboBox_4.currentTextChanged.connect(self.show4)
        self.tablelist = [self.tableWidget,self.tableWidget_2,self.tableWidget_3,self.tableWidget_4] # 데이터리스트

        # mysql 연결
        db = pymysql.connect(host='localhost', port=3306, user='root', password='0000', db='test', charset='utf8')
        self.cursor = db.cursor()

# 콤보박스선택에 따른 함수---------------------------------------------------------------------------

    # 문화시설 선택시
    def gal_f(self,num):
            self.cursor.execute('SELECT * FROM gwangju_gal')
            self.gal = self.cursor.fetchall()
            self.tablelist[num].setRowCount(len(self.gal))         # 행추가
            self.tablelist[num].setColumnCount(len(self.gal))      # 열추가
            for i in range(len(self.gal)):                         # 리스트의 길이만큼
                for j in range(len(self.gal[i])):                  # 리스트속 1개의 데이터 길이만큼
                    self.tablelist[num].setItem(i, j,QTableWidgetItem(str(self.gal[i][j])))
    # 체육시설 선택시
    def ath_f(self,num):
            self.cursor.execute('SELECT * FROM gwangju_ath')
            self.ath = self.cursor.fetchall()
            self.tablelist[num].setRowCount(len(self.ath))
            self.tablelist[num].setColumnCount(len(self.ath))
            for i in range(len(self.ath)):
                for j in range(len(self.ath[i])):
                    self.tablelist[num].setItem(i, j, QTableWidgetItem(str(self.ath[i][j])))
    # 편의시설 선택시
    def park_f(self,num):
            self.cursor.execute('SELECT * FROM gwangju_small_park')
            self.park = self.cursor.fetchall()
            self.tablelist[num].setRowCount(len(self.park))
            self.tablelist[num].setColumnCount(len(self.park))
            for i in range(len(self.park)):
                for j in range(len(self.park[i])):
                    self.tablelist[num].setItem(i, j, QTableWidgetItem(str(self.park[i][j])))
    # 학교선택시
    def school_f(self,num):
            self.cursor.execute('SELECT * FROM schoollist_ele')
            self.school = self.cursor.fetchall()
            self.tablelist[num].setRowCount(len(self.school))
            self.tablelist[num].setColumnCount(len(self.school))
            for i in range(len(self.school)):
                for j in range(len(self.school[i])):
                    self.tablelist[num].setItem(i, j, QTableWidgetItem(str(self.school[i][j])))

#-------------------------------------------------------------------------------------------

    # # 콤보박스 삭제하기
    # def del_ComboBox(self):
    #     self.delidx = self.ComboBox.currentIndex()
    #     self.cmb_Test.removeItem(self.delidx)
    #     self.cmb_second.removeItem(self.delidx)
    #     print("Item Deleted")

    # 1순위 선택
    def show1(self, item):
        self.tableWidget.clearContents() # 초기화
        self.lineEdit_3.setText(item)
        show = self.lineEdit_3.text()
        # print(show)
        if show == '문화시설':
            self.gal_f(0)
        elif show == '체육시설':
            self.ath_f(0)
        elif show == '편의시설':
            self.park_f(0)
        elif show == '학교':
            self.school_f(0)

    # 2순위 선택
    def show2(self, item):
        self.tableWidget_2.clearContents()  # 초기화
        self.lineEdit_4.setText(item)
        show = self.lineEdit_4.text()
        print(show)
        if show == '문화시설':
            self.gal_f(1)
        elif show == '체육시설':
            self.ath_f(1)
        elif show == '편의시설':
            self.park_f(1)
        elif show == '학교':
            self.school_f(1)

    # 3순위 선택
    def show3(self, item):
        self.tableWidget_3.clearContents()  # 초기화
        self.lineEdit_6.setText(item)
        show = self.lineEdit_6.text()
        print(show)
        if show == '문화시설':
            self.gal_f(2)
        elif show == '체육시설':
            self.ath_f(2)
        elif show == '편의시설':
            self.park_f(2)
        elif show == '학교':
            self.school_f(2)

    # 4순위 선택
    def show4(self, item):
        self.tableWidget_4.clearContents()  # 초기화
        self.lineEdit_5.setText(item)
        show = self.lineEdit_5.text()
        print(show)
        if show == '문화시설':
            self.gal_f(3)
        elif show == '체육시설':
            self.ath_f(3)
        elif show == '편의시설':
            self.park_f(3)
        elif show == '학교':
            self.school_f(3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = town()
    myWindow.show()
    app.exec_()