import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic
import matplotlib.pyplot as plt
import tkinter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
# import Lookup_2

form_class = uic.loadUiType("a.ui")[0] # ui 연결해주기

class look_up(QMainWindow, form_class) :  # 화면을 띄우는데 사용되는 Class 선언
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.idx = 0                             # 검색의 기본 값은 0으로 고정
        self.setWindowTitle('전남폐기물 매립시설')  # 프로그램의 타이틀

        f = open("20210906.csv", "r")
        self.reader = csv.reader(f)     # csv파일을 읽어온뒤 저장하기
        self.empty = []                 # 비어있는 리스트 만들어주기
        for i in self.reader:           # 이중리스트를 위한 for문
            self.empty.append(i)        # 리스트에 저장
        f.close()
        # print(empty)

        self.lookup.setRowCount(len(self.empty))                  # csv파일길이만큼 행추가
        self.push_b.clicked.connect(self.search_f)                # 검색하기 클릭시
        self.total_b.clicked.connect(self.total_f)                # 전제보기 클릭시
        self.search_b.returnPressed.connect(self.search_f)        # 검색후 엔터시
        self.select_comboBox.currentIndexChanged.connect(self.select_combo)  # 콤보박스 선택시
        self.add_b.clicked.connect(self.add_f)                   # 추가하기 클릭시
        self.del_b.clicked.connect(self.del_f)                   # 삭제하기 클릭시

        # ----------------그래프
        flie = open("Rubbish.csv", "r")
        flie_list = csv.reader(flie)
        flie.close()

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.graph_verticalLayout.addWidget(self.canvas)
        x = np.arange(0, 100, 1)
        y = np.sin(x)

        ax = self.fig.add_subplot(111)
        ax.plot(x, y, label="sin")
        ax.set_xlabel("x")
        ax.set_xlabel("y")

        ax.set_title("Annual Garbage")
        ax.legend()
        self.canvas.draw()
        #-----------------------------

    def total_f(self):                                          # 전체보기 버튼을 눌렀을때 데이터 전체출력
        for i in range(len(self.empty) - 1):                    # 리스트의 길이만큼
            for j in range(len(self.empty[i]) - 1):             # 리스트속 1개의 데이터 길이만큼
                self.lookup.setItem(i, j, QTableWidgetItem(str(self.empty[i + 1][j + 1])))

    def select_combo(self): # 콤보박스 선택시
        self.idx = self.select_comboBox.currentIndex()

    def search_f(self):                     # 검색하기 메서드
        self.lookup.clearContents()         # 테이블위젯 초기화
        show_search = self.search_b.text()
        search_list = []                    # 검색한 목록의 저장을 위해
        for i in self.empty:                # 전체 항목 검색할 때
            if self.idx == 0:
                if (show_search in i[0]) or (show_search in i[1]) or (show_search in i[2]) or (show_search in i[3]) or \
                   (show_search in i[4]) or (show_search in i[5]) or (show_search in i[6]) or (show_search in i[7]):
                    search_list.append(i)

            else:                           # 원하는 항목만 검사할 때
                if (show_search in i[0]) or (show_search in i[1]) or (show_search in i[2]) or (show_search in i[3]) or \
                   (show_search in i[4]) or (show_search in i[5]) or (show_search in i[6]) or (show_search in i[7]):
                    search_list.append(i)

        for i in range(len(search_list)):                  # 테이블 위젯의 행과 열에 데이터 넣어줌
            for j in range(len(search_list[i])-1):         # i번째 줄의 j번째 칸에 데이터를 넣어줌
                self.lookup.setItem(i, j, QTableWidgetItem(search_list[i][j+1]))


    def add_f(self): # 추가하기
      pass


    def del_f(self): # 삭제하기
        pass

# form_secondwindow = uic.loadUiType("b.ui")[0]
#
# class secondwindow (QMainWindow, form_secondwindow): # 데이터 추가창
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = secondwindow()
#     myWindow.show()
#     app.exec_()


if __name__ == "__main__" :         # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)    # WindowClass의 인스턴스 생성
    myWindow = look_up()            # 프로그램 화면을 보여주는 코드
    myWindow.show()
    app.exec_()                     # 이거뭔데 이거없다고 창이 나타났다 사라짐