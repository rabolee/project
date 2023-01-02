import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic
import matplotlib.pyplot as plt
import tkinter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import random


form_class = uic.loadUiType("bmi.ui")[0] # ui 연결해주기

class bmi(QMainWindow, form_class) :  # 화면을 띄우는데 사용되는 Class 선언
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.idx = 0                             # 검색의 기본 값은 0으로 고정
        self.setWindowTitle('전남폐기물 매립시설')  # 프로그램의 타이틀

        # csv 데이터파일 만들기
        file = open("human.txt", "w")
        file.write("이름,키,몸무게\n")
        for i in range(100):  # 100명의 데이터
            name = list("가나다라마바사아자차카타파하")
            full_name = random.choice(name) + random.choice(name) + random.choice(name)  # 이름 지정해주기
            key = random.randrange(120, 200)    # 키 지정해주기
            weight = random.randrange(40, 150)  # 몸무게 지정해주기
            file.write(f'{full_name},{key},{weight}\n')
        file.close()
        #
        # f = open("human.txt", "r")
        # self.reader = csv.reader(f)     # csv파일을 읽어온뒤 저장하기
        # self.empty = []                 # 비어있는 리스트 만들어주기
        # for i in self.reader:           # 이중리스트를 위한 for문
        #     self.empty.append(i)        # 리스트에 저장
        # f.close()
        # print(self.empty)


# csv 파일 가공하기
# file = open("human.csv", "r")
# for i in file:
#     # 다중할당을 활용해 변수에 바로 저장해주기
#     # 공백없애주기, ,로 구분지어 리스트로 불러오기
#     full_name,key,weight = i.strip().split(",")
#     # 첫번째줄의 헤더가 문자일때 넘겨주기
#     if not weight.isdigit():
#         continue
#     key = int(key)
#     weight = int(weight)
#     # bmi 구하는 공식 round함수로 소수점 2번째 까지 출력
#     bmi = round(weight / (key/100) ** 2,2)
#     result = '' # 결과출력용
#     if 25 <= bmi:
#         result = '과체중'
#     elif 18.5 <= bmi:
#         result = '정상체중'
#     else:
#         result = '저체중'
#
#     print('\n'.join([
#            f'이름: {full_name}',
#            f'키: {key}',
#            f'몸무게: {weight}',
#            f'bmi: {bmi}',
#            f'결과: {result}','']))
# file.close()


if __name__ == "__main__" :         # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)    # WindowClass의 인스턴스 생성
    myWindow = bmi()            # 프로그램 화면을 보여주는 코드
    myWindow.show()
    app.exec_()                     # 이거뭔데 이거없다고 창이 나타났다 사라짐