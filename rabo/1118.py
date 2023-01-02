# a = "hobby"
# l = ",".join(a)
#
# print(",".join(a)) # 리스트변환
# print(l) # 변수로 리스트출력
#
# print(a.upper()) #대문자
# print(a.count('h'),a.find('h'))
# print(a.count('o'),a.find('o'))
# print(a.count('b'),a.find('b'))
# print(a.count('b'),a.find('b'))
# print(a.count('y'),a.find('y'))
#
#
# abc ="abcdefghijklmnopqrstuvwxyz"
# a = list(abc)
# print(list(a))
#
# for i in a:
#     print(f"{i}의 위치: {a.index(i)}번째")
#     print(f"{i}의 갯수: {a.count(i)}개")
#
#
#
#
# a=['a','c','  b']
# a.sort()
# a.reverse()
# print(a)
# import random

# # # treehit = 0
# while treehit < 10:
#     treehit = treehit +1
#     print("나무를 %d번 찍었습니다."% treehit)
#     if treehit == 10:
#         print("나무 넘어갑니다.")
#
#
# i = 0
# while i<5:
#     i += 1
#     print("*"*i)



# 직각삼각형

# i = 0
# while i<5:   #크...c와는 다르게 짧디 짧다 크...
#     i += 1
#     print("*"*i)


# 거꾸로 삼각형

# i = 5
# while i>0:
#     i -= 1
#     print("*"*i)


# 피라미드

# i = 1 # 별
# a = 5 # 공백
# while a>0:
#
#     a -= 1
#     print(" "*a, end="")  # 자동줄바꿈 좋은데 별찍기할때는 안나왔으면
#     print("*"*i)  # 강제개행 반대하긔 end=""꼭 넣어주기
#     i += 2 # 위치 중요 위에서부터 내려오기때문에 아래로 내려줘야한다

# 피라미드 거꾸로

# i = 5 # 별
# a = 0 # 공백
# while a<5:
#
#     a += 1
#     print(" "*a, end="")  # 자동줄바꿈 좋은데 별찍기할때는 안나왔으면
#     print("*"*i, end="")  # 강제개행 반대하긔 end=""꼭 넣어주기
#     i -= 1  # 위치 중요 위에서부터 내려오기 때문에 아래로 내려줘야 한다
#     print("*"*i)

# 피라미드 합치기

# i = 1 # 별
# a = 5 # 공백
# while a>0:
#     a -= 1
#     print(" "*a, end="")
#     print("*"*i)
#     i += 2
#
# i = 7 #변수초기화 아랫줄 첫번째 별개수
# while a<5:
#     a += 1 #위치중요하다
#     print(" "*a, end="")
#     print("*"*i, end="")
#     print(" "*a)
#     i -= 2

#
# # 모래시계
#
# a = 1 #공백
# i = 9 #별
# while a<5:
#     a += 1 #위치중요하다
#     print(" "*a, end="")
#     i -= 2
#     print("*"*i)
#
# i = 1  # 별
# a = 5  # 공백
# while a > 0:
#     print(" " * a, end="")
#     a -= 1
#     print("*" * i)
#     i += 2
#


# # 바람개비 만들기
# s = 0
# b = 10
# while s <10 :
#
#     s += 1
#     print("*"*s, end="") # end사용할때도 공백 조심 바람개비 꼭지점이 맞지 않습니다
#     print(" "*b, end="")
#     print("*"*b)
#     b -= 1
# b = 10
# s = 0
# while s < 10:
#
#     print(" " * b, end="")
#     s += 1
#     print("*" * s, end="")
#     print(" " * s, end="")
#     print("*" * b)
#
#     b -= 1
#
#
#
# # # 밑변받아 바람개비 만들기
#
# num =input("밑변입력: ")
# num=int(num)
#
# s = 0
# b = num
# while s <num:
#
#     s += 1
#     print("*"*s, end="") # end사용할때도 공백 조심 바람개비 꼭지점이 맞지 않습니다
#     print(" "*b, end="")
#     print("*"*b)
#     b -= 1
#
# b = num
# s = 0
# while s < num:
#
#     print(" " * b, end="")
#     s += 1
#     print("*" * s, end="")
#     print(" " * s, end="")
#     print("*" * b)
#     b -= 1
#

# 형제의 난
# print("====================================")
# print("           형  제  의  난    ")
# print("====================================")
# team = random.randrange(1,3) #팀을 나눠주기위한 랜덤함수 (1,2)
# # print(team)    # 팀 랜덤이 잘나오는지 확인
#
# if team == 1: # 랜덤함수를 넣어준 이름을 if 넣어준다
#     print("""'성일,의용', '재일,연재' 한팀이 되었습니다.""")
#
#     siyy = 0
#     jiyj = 0
#     while True:
#         total = random.randrange(1, 4) #승부랜덤이 잘 나오는지 확인
#
#         if total == 1: #성일의용승리
#             print("성일,의용팀 승")
#             siyy += 1
#             print("성일,의용팀이 %d번 승리" %siyy)
#         if siyy == 10:
#             print("성일,의용팀이 승리하였습니다.")
#             break
#
#         if total == 2:
#             print("재일,연재팀 승")
#             jiyj += 1
#             print("재일,연재팀이 %d번 승리" %jiyj)
#         if  jiyj == 10:
#             print("재일,연재팀이 승리하였습니다.")
#             break
#
#         if total == 3:
#             print("무승부입니다.")
#
#     count = siyy + jiyj
#     print("성일,의용팀의 승률 : %.1f%%"%((siyy/count)*100))  #소수점 출력시 %f 잊지말라고
#     print("재일,연재팀의 승률 : %.1f%%"%((jiyj/count)*100))  #소수점 n번째 자리까지  %.1f (원하는 숫자넣어주기)
#
# else:
#     print("""'성일,연재', '재일,의용' 한팀이 되었습니다.""")
#
#     siyj = 0
#     jiyy = 0
#     while True:
#         total = random.randrange(1, 4)
#
#         if total == 1: #성일연재승리
#             print("성일,연재팀 승")
#             siyj += 1
#             print("성일,연재팀이 %d번 승리" %siyj)
#         if siyj == 10:
#             print("성일,연재팀이 승리하였습니다.")
#             break
#
#         if total == 2:
#             print("재일,의용팀 승")
#             jiyy += 1
#             print("재일,의용팀이 %d번 승리" %jiyy)
#         if  jiyy == 10:
#             print("재일,의용팀이 승리하였습니다.")
#             break
#
#         if total == 3:
#             print("무승부입니다.")
#
#     count = siyj + jiyy
#     print("성일,연재팀의 승률 : %.1f%%"%((siyj/count)*100))
#     print("재일,의용팀의 승률 : %.1f%%"%((jiyy/count)*100))
#
#
# 포켓몬마스터
# print("***포켓몬 100개를 오박사에게 지급받았다***")
# print("************************************")
#
# pica = 0
# pairi = 0
# kkobuk = 0
# meta = 0
# for i in range (100):
#     poket = random.randrange(1, 5)  # 1~4까지의 랜덤함수출력
#     if poket == 1:
#         print("피카츄")
#         pica += 1
#     if poket == 2:
#         print("파이리")
#         pairi += 1
#     if poket == 3:
#         print("꼬부기")
#         kkobuk += 1
#     if poket == 4:
#         print("메타몽")
#         meta += 1
#
# print("피카츄:%d마리" %pica)
# print("파이리:%d마리" %pairi)
# print("꼬부기:%d마리" %kkobuk)
# print("메타몽:%d마리" %meta)
#
# print("************************************")
# print("      메   타   몽    변   신   ")
# print("************************************")
#
# Mpica = 0 #변신피카츄
# Mpairi = 0 #변신파이리
# Mkkobuk = 0 #변신꼬부기
# Mmeta = 0 #변신메타몽
#
# for i in range(meta):
#     poket = random.randrange(1, 5)  # 1~4까지의 랜덤함수출력
#     if poket == 1:
#         print("피카츄")
#         Mpica += 1
#     if poket == 2:
#         print("파이리")
#         Mpairi += 1
#     if poket == 3:
#         print("꼬부기")
#         Mkkobuk += 1
#     if poket == 4:
#         print("메타몽")
#         Mmeta += 1
#
# print("변신피카츄:%d마리" %Mpica)
# print("변신파이리:%d마리" %Mpairi)
# print("변신꼬부기:%d마리" %Mkkobuk)
# print("변신메타몽:%d마리" %Mmeta)
#

# 1개씩 포켓몬마스터
# print("***포켓몬 100개를 오박사에게 지급받았다***")
# print("************************************")
# open = 0
# pica = 0
# pairi = 0
# kkobuk = 0
# meta = 0
# for i in range(10):
#     input("숫자를 누르면 포켓몬 오픈")
#     for i in range(10):
#         open = (pica + pairi + kkobuk + meta +1) #포켓몬마리수
#         poket = random.randrange(1, 5)  # 1~4까지의 랜덤함수출력
#         if poket == 1:
#             print("피카츄")
#             pica += 1
#             print("현재 포켓몬은:%d" % open)
#         if poket == 2:
#             print("파이리")
#             pairi += 1
#             print("현재 포켓몬은:%d" % open)
#         if poket == 3:
#             print("꼬부기")
#             kkobuk += 1
#             print("현재 포켓몬은:%d" % open)
#         if poket == 4:
#             print("메타몽")
#             meta += 1
#             print("현재 포켓몬은:%d" % open)
#         break
#
# print("피카츄:%d마리" %pica)
# print("파이리:%d마리" %pairi)
# print("꼬부기:%d마리" %kkobuk)
# print("메타몽:%d마리" %meta)
#
# print("************************************")
# print("      메   타   몽    변   신   ")
# print("************************************")
#
# Mpica = 0 #변신피카츄
# Mpairi = 0 #변신파이리
# Mkkobuk = 0 #변신꼬부기
# Mmeta = 0 #변신메타몽
#
# for i in range(meta):
#     input("메타몽변신 숫자입력")
#
#     for i in range(meta):
#         poket = random.randrange(1, 5)  # 1~4까지의 랜덤함수출력
#         if poket == 1:
#             print("피카츄")
#             Mpica += 1
#             break
#         if poket == 2:
#             print("파이리")
#             Mpairi += 1
#             break
#         if poket == 3:
#             print("꼬부기")
#             Mkkobuk += 1
#             break
#         if poket == 4:
#             print("메타몽")
#             Mmeta += 1
#             break
#
# print("변신피카츄:%d마리" %Mpica)
# print("변신파이리:%d마리" %Mpairi)
# print("변신꼬부기:%d마리" %Mkkobuk)
# print("변신메타몽:%d마리" %Mmeta)

# 류키우기
# total = 2 # 류진스 커플
# print("******************************************")
# print("            류네상스 S2 류진스")
# print("           금붕어 키우기 start!")
# print("******************************************")
# baby = random.randrange(1,6) # 금붕어 5쌍태어나기 랜덤
# print("류네상스S2류진스의 새끼금붕어가 %d쌍 태어났습니다." %baby)
# print("******************************************")
# total = int(total+baby*2) #
#
# while total<1000:
#     for i in range(total//2): # 그냥  /는 나누기 // 몫 받은수를 정수로 변경
#         Bbaby = random.randrange(1, 6)  # 금붕어 5쌍태어나기 랜덤
#         total = total+Bbaby*2
#         print("새끼금붕어 %d쌍 태어났습니다." %Bbaby)
#         break
#     die = random.randrange(1, 6)  # 금붕어 5쌍죽기 랜덤
#     print("새끼금붕어 %d쌍이 죽었습니다." %die)
#     total = total+die*2
#     print("금붕어는 총 %d마리" % total)    # 2턴 종료 금붕어 죽기시작
#
#
# 코카콜라
# "숫자"를 쌍따옴표안에 넣으면 문자취급
# sel = {1:["콜라",1200],2:["우주맛콜라",1900],3:["제로콜라",1200],4:["환타",900],5:["닥터페퍼",1100],6:["몬스터",1800],7:["파워웨이드",1900],8:["네스티",1600],9:["글라소비타민워터",2100],
# 10:["미닛메이드",1700],11:["조지아커피",900],12:["암바사",900],13:["마테차",1700],14:["스프라이트",1100]}
#
# print("******************************************")
# print("   시   원   한   얼   음   자   판   기")
# print("******************************************")
#
# select = 0
# money = int(input("돈을 넣어주세요")) #정수로 변환
#
# while True:
#     for key, value in sel.items():    #딕셔너리 호출을 위한 for문
#         print(key,value)  # *은 대괄호와 따옴표를 없애준다. #딕셔너리속 키값만 출력
#     select = int(input("음료를 선택하세요")) # 정수로 변환해준다 리스트에 있는 자료출력을 위하여
#     print(sel[select],"선택")
#
#     money = money - sel[select][1]  # 남은돈을 계산하기 위하여
#
#     if sel[select][1] < money:
#         print("　　　　　　　　　| ")
#         print("　　　　　　　　　| ")
#         print("　       　　　 ﾉ,,∧ ")
#         print("　돈더줘..　　 ／/･ω･`) ")
#         print("　　　　　　／　/⊂ノ")
#         print(" 　　　　　　＼ /ーJ ")
#         print(" ￣￣￣￣￣￣￣")
#         print("***********************")
#         print("돈이 부족합니다. 종 료")
#         print("***********************")
#         break
#
#     if  money < 0:
#         print("　　　　　　　　　| ")
#         print("　　　　　　　　　| ")
#         print("　       　　　 ﾉ,,∧ ")
#         print("　돈더줘..　　 ／/･ω･`) ")
#         print("　　　　　　／　/⊂ノ")
#         print(" 　　　　　　＼ /ーJ ")
#         print(" ￣￣￣￣￣￣￣")
#         print("***********************")
#         print("돈이 부족합니다. 종 료")
#         print("***********************")
#         break
#
#     else:
#         print("|∧∧       ┏┓     ")
#         print("| ' ω')   ┗┛    ")
#         print("|⊂ノ    옛-다   ")
#         print("|")
#         print("***********************")
#         print("남은 금액은 :%d "%money)
#         print("***********************")


#  10만 유튜버 이상혁
# print("""유튜버 '이상혀기'개설되었습니다.""")
# print("*******************************")
# lsh = 0
# for i in range(20):
#     print("오늘의 컨텐츠 '파이썬 파헤치기' 방송시작 !")
#     viewers = random.randrange(50, 2500) #시청자수 50~2500랜덤
#     print(viewers,"명 시청중.") #1초 시청자수
#     sub = random.randrange(1,6)
#     # print(sub)   #구독자수 1~5 나누기
#     silver = (viewers*10)//sub #  나누기'//' 몫 출력
#     print(silver,"명 구독중")
#     lsh += silver # 합계더하기
#
# print("총 구독자: %d명" %lsh) # 구독자수 출력
# if lsh < 100000:
#     print("도전 실패! 유튜브 폭파")
#     print("＼(º □ º l|l)/")
# else:
#     print("""'실버버튼 증정'""")
#     print("|￣￣￣￣￣￣￣|")
#     print("|  실버버튼   |")
#     print("|＿＿＿＿＿＿＿|")
#     print("(\__/) ||")
#     print("(•ㅅ•).||")
#     print("/ . . . .づ")
#
# 소문자를 대문자로
# change = input('>>>')
# cchange = change.upper()
# print(cchange) # 이걸 한줄로 줄일수 있는 방법은 없을까?
#
# # Hello World를 대문사 소문자 구분하여 아스키코드 숫자로 출력
# change = "Hello World"
# for i in change: #변환할 문자의 길이만큼 반복문을 돌려준다.
#     print(ord(i), end=',') #파이썬은 강제개행되기때문에 끝에 end를 넣어준다
#
# # 영어를 받으면 아스키코드 출력되기
# change = input("영어를 입력하세요") # 위의 코드에서 입력받을 값만 추가해준다. C보다는 파이썬이 간편한 느낌이든다
# for i in change:
#     print(ord(i), end=',')
#
# # 숫자를 받으면 문자로 출력되기
# change = input("숫자를 입력하세요")
# change = int(change) #문자열로 변환을 해주기 위해
# print(chr(change)) # 숫자를 한가지밖에 못받는다 for문을 돌리면 계속쑬수있을것같은데 방법을 생각해보자
#
# # 영어를 입력받으면 아스키코드 값에서 +3이 나오는 암호함수
# change = input("영어를 입력하세요")
# for i in change:
#     print(ord(i)+3, end=',') # 파이썬에는 아스키코드함수가 따로 있어서 편한것같다
#     # ord = 영어를 아스키코드로 , chr = 아스키코드를 영어로
#
# #나만의 암호만들기
# word = "the quick brown fox jumps over the lazy dog"
# #복습을 위하여 암호를 소문자에서 리스트화하여 대문자로 출력해보았다.
# word = word.upper() # 대문자로 대입하기
# print(word)
# word = list(word) # 대문자리스트 대입하기
# print(word)
# for i in word:
#     print(ord(i),end=',')

# 소수구하기
# comfirm = 0
# num = int(input("숫자를 입력하세요 : ")) #처음 받을값을 처음부터 변환해주어야 한다.
#
# for i in range (2,num): # 입력받은 숫자만큼 반복으로 돌려준다.
#     if num%i == 0:      # 입력받은 숫자보다 -1작은수까지 모두 나눴을때 나머지 0
#         comfirm = 1 #나머지가 0이 되었을때 comfirm에 저장
# if comfirm == 0:
#     print("소수입니다.")
# else:
#     print("소수가 아닙니다.")

# 청소당번뽑기
# people = ['강민영','고연재','김기태','김명은','김성일','김연수','김재일','노도현','류가미','박규환','박성빈','박시형','박의용','오송화','이범규','이보라','이소윤','이여름','이지혜','이현도','임성경','임영효','임홍선','장은희','정연우','정철우','주민석','최지혁']
# # print(people[0]) # 리스트 출력 확인
# random.shuffle(people) #리스트를 랜덤으로 섞어주기
# print("분리수거",people[:2])
# print("쓸기",people[3:4]) # 중복된 값을 따로 빼주는 방법을 찾아봐야겠다.
# print("닦기",people[4:5]) # 일단 이렇게 중복제거하는걸로

# 청소당번뽑기 (중복제거)
people = ['강민영','고연재','김기태','김명은','김성일','김연수','김재일','노도현','류가미','박규환','박성빈','박시형','박의용','오송화','이범규','이보라','이소윤','이여름','이지혜','이현도','임성경','임영효','임홍선','장은희','정연우','정철우','주민석','최지혁']
for i in range(4):
    print(i,"째주",random.sample(set(people),4)) #파이썬 진짜 짱이다