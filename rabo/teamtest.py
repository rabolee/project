
# 51
movie_rank = ["닥터스트레인지","스플릿", "럭키"]
print(movie_rank)

# 52
movie_rank.append("배트맨") # 요소 마지막추가 'append'
print(movie_rank)

# 53
movie_rank.insert (1,"슈퍼맨") # 요소 중간삽입 'insert'
print(movie_rank)

# 54
del movie_rank[3] # 삭제할때 '.' 안찍습니다
print(movie_rank)

# 55
del movie_rank [2:]
print(movie_rank)

# 56
lang1 = ["c","c++","java"]
lang2 = ["python","go","c#"]
print(lang2+lang2)

#57
nums = [1,2,3,4,5,6,7]
print("max:",max(nums))
print("min:",min(nums))

# 58
nums = [1,2,3,4,5]
print(sum(nums))

# 59
cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print(len(cook)) # 요소의 개수를 찾아주는 함수 너무 편한듯

# 60
nums = [1,2,3,4,5]
total = sum(nums) // len(nums)
print(total)
print(sum(nums)//len(nums)) #함수를 만들지 않고도 한줄도 가능

# 61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:]) # 1번자리부터 마지막까지 출력

# 62 # 63
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[0::2]) # 0번요소부터 10번요소까지의 값중 +2씩 된값들만 출력
print(nums[1::2]) # 1번요소부터 10번요소까지의 값중 +2씩 된값들만 출력

# 64
nums = [1,2,3,4,5]
nums.reverse()
print(nums)
# print(nums.reverse())  # 프린트로 바로 출력안되네


# 바인딩 : 함수를 호출할때 실제함수가 위치한 메모리를 연결 해주는 것
# 65
interest = ['삼성전자','lg전자','naver']
print(interest[0::2]) #리스트 안의 값이 출력되므로 ' '까지 출력
# print(interest[0],[2]) # 이렇게는 출력안된다
print(interest[0],interest[2]) # 각각의 값을 출력했으므로 문자열만 출력

# 66 67 68
interest = ['삼성전자','lg전자','naver','sk하이닉스','미래에셋대우']
print((" ".join(interest)))
print("/".join(interest)) # 내가 넣고 싶은 문자열을 " "안에 넣어주고.join 합쳐라
print("*".join(interest))
print("\n".join(interest)) # 줄바꿈 도 가능하다

# 69
string = "삼성전자/lg전자/naver"
interest = list(string.split('/')) # 나누는 기준을 찾아준다.
print(interest)
# print(list(string.split('/')) # 바로 출력은 안되나보네
print((string.split('/'))) # 리스트 변환하기 전은 구분가능

# 70
date = [2, 4, 3, 1, 5, 10, 9]
date.sort() # 오름차순 정렬함수
# date.reverse() # 거꾸로 나오게할수도있어
print(date)

# 71
my_variable = () # 파이썬은 () {} [] 쓰임새마다 이름이 있다.
print(type(my_variable)) # 타입확인하기

# 72
movie_rank = ('닥터스트레인지','스플릿','럭키')
print(type(movie_rank)) # 위에윗줄에서 )한개빠져서 계속 에러났다 튜플잘못쓴줄..

# 73
num = (1)
print(type(num)) # 튜플로 선언을 해줘도 타입은 int이다.
num = (1,)
print(type(num))  # 튜플에서 1개의 값을 입력할때는 , 를 넣어줘야한다.

# 74
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
# 튜플은 원소의 값을 수정,삭제.생성 할 수 없다.

# 75
t = 1,2,3,4  # 튜플은 괄호 없이 사용할수 있다.
print(type(t))

# 76
# t = ('a','b','c')
# t.upper()
# print(t.upper()) # 오류가난다. 튜플은 수정할 수 없기때문에

# 77
interest = ('삼성전자','lg전자','sk hynix')
data = list(interest) # 리스트로 변환하기위한 함수
print(type(data)) # 변환된 값 출력

# 78
interest = ['삼성전자','lg전자','sk hynix']
data= tuple(interest)
print(type(data))

# 79
temp = ('apple', 'banana', 'cake') # 묶여있는 값 = 패킹
a, b, c = temp # 저장된값을 하나씩 꺼내기 = 언패킹
print(a, b, c)

# 80
num = tuple(range(2,100,2)) # 2부터 100까지의 범위중 2씩커져있는 숫자
print(num)

# 81
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,a,b = scores # 내가 원하는 숫자 다음부터는 다른 변수로 10중 8이면 따로 2개 지정해주기
print(valid_score)

# 82
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,b,*valid_score = scores
print(valid_score)

# 83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,*valid_score,b = scores
print(valid_score)

# 84
temp = {} # 딕셔너리의 기본값

# 85
temp = {"메로나":1000, "폴라포":1200, "빵빠레":1800}
print(temp)

# 86
ice = {"메로나":1000, "폴라포":1200, "빵빠레":1800}
ice["죠스바"] = 1200   # key값은 [] 넣어주기 value = 넣어주기
ice["월드콘"] = 1500
print(ice)

# 87 88 89
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print("메로나 가격:",ice['메로나']) # key값으로 value 얻기
ice['메로나'] = 1300 # 수정이 없으므로 새로운 한쌍을 넣어준다
print(ice['메로나']) # 중복된값은 출력되지 않고 새로운값만 출력된다.
del ice['메로나'] # key값이 메로나인 요소한쌍 삭제
print(ice)

# 90
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
# 딕셔너리에 없는 키을 인덱싱하면 에러가 발생한다.

# 91 92 93 94
inventory = {"메로나":[300,20],"비비빅":[400,3],"죠스바":[250,100]}
print(inventory)
print(inventory["메로나"][0],"원") # value의 값은 0부터 시작한다.
print(inventory["메로나"][1],"개")
inventory["월드콘"] = [500,7]
print(inventory)

# 95 96 97 98
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys()) # key값을 list로 저장해서 출력하는방법
print(ice)
# for key in icecream.keys():  # for문을 이용해서도 키값만 출력가능
#        print(key,",", end="")
cream = list(icecream.values())
print(cream)
# for value in icecream.values(): # for문을 이용해서도 value 출력가능
#        print(value,",", end="")
print(sum(cream))
new_product = {'팥빙수':2700,'아맛나':1000}
icecream.update(new_product) # 직관적인 파이썬언어ㅎㅎ찐업데이트
print(icecream)

# 99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = {keys[0]:vals[0],keys[1]:vals[1],keys[2]:vals[2]} # 일단 이렇게 짜봤다.
result1 = dict(zip(keys,vals)) # zip 함수를 이용하여 출력
print(result)
print(result1)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price)) # 파이썬 진짜 짱이다
print(close_table)

# 101 102 103
# True 와 False 를 갖는 데이터 타입은 불자료형입니다.
print(3==5) # 거짓
print(3<5) # 진실

# 104 105
x = 4
print(1<x<5) # 진실
print((3 == 3) and (4!=3)) # 진실 3과3은 같다 4는3과다르다는 값이 모두 참이기때문에

# 106
# print(3=>4) # 부등호 틀렸습니다 =은 항상뒤에

# 107
# if 4 < 3:  # 조건이 틀렸기 때문에 아무것도 출력되지 않는다.
#     print("hello world")

# 108
if 4 < 3:
       print("hello world")
else: # 조건이 진실일때 출력
       print("hi,there")

# 109
if True:
       print("1")
       print("2")
else:
       print("3")  # 조건이 맞지 않기 때문에 출력되지않는다.
print("4")

# 110
if True:
       if False :
              print("1")
              print("2")
       else:
              print("3")
else:
       print("4")
print("5")
# 값이 진실인 3과 5가 출력된다.

# 111
print(input()*2) # 한줄로 쓰는방법
hi = input()
print(hi*2)

# 112
a = int(input("숫자를 입력하세요:")) #자꾸 한줄로줄이려는 욕심에 프린트 넣었다가 계산출력이 안되는오류발생ㅋㅋ
print(a+10)

# 113
num = int(input("숫자를 입력하세요"))
jjak = num%2==0
hol = num%2==1
print("홀수",hol) # if문 안써야 되는줄알고 이렇게 만들었지
print("짝수",jjak)
if num %2==0:
       print("짝수입니다.")
else:
       print("홀수입니다.")

# 114
num = int(input("숫자를 입력하세요"))
num += 20
if num < 255:
       print(num)
else:
       print("255")

# 115
num = int(input("숫자를 입력하세요"))
num -= 20
if 0 < num < 255:
       print(num)
if num < 0:
       print("0")

# 116
time = (input("현재시간 :"))  #이야 이거 생각보다 오래걸렸다.
if time[-2:]=="00": # 여기 확인하자 문자열로 입력받았으니 "" 넣어주기
       print("정각입니다.")
else:
       print("정각이아닙니다.")

# 117
fruit = ["사과","포도","홍시"]
eat = input("좋아하는과일은?:") # 프린트를 여기다가 넣어서 자꾸 오답이 나왔다
if eat in fruit:
       print("정답입니다.")
else:
       print("오답입니다.")

# 118
warn_investment_list = ["microsft","google","naver","kakao","samsung","lg"]
investment = input ("종목을 입력하세요 : ")
if investment in warn_investment_list:
       print("투자 경고 종목입니다.")
else:
       print("투자 경고 종목이 아닙니다.")

# 119 120
fruit = {"봄":"딸기","여름":"토마토","가을":"사과"}
a = input("제가 좋아하는 계절은?:")
if a in fruit:
       print("정답입니다.")
else:
       print("오답입니다.")

b = input("제가 좋아하는 과일은?:")
if a in fruit.values(): # 키값과 다르게 values는 지정해주어야한다.
       print("정답입니다.")
else:
       print("오답입니다.")

# 121
abc = input("영어를 입력하세요:")
comfirm = abc.islower()
if comfirm == True:
       print(abc.upper())
else:
       print(abc.lower())

# 122
total = int(input("score :"))
if 0 < total < 20:
       print("E")
if 21 < total < 40:
       print("D")
if 41 < total < 60:
       print("C")
if 61 < total < 80:
       print("B")
if 81 < total < 100:
       print("A")

# 123
money = {"달러":1167,"엔":1.096,"유로":1268,"위안":171}
comfirm = str(input("화폐입력:"))
change = int(input("금액입력:"))
if comfirm in money:
       print(change*1167)

