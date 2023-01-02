import random

# A,B,C,D,E,F,G,H 총 8개의 팀이 경기를 한다.
# 한 팀에는 4개의 국가가 있다.
# 4개의 팀이 모두 한번씩 경기를 진행하며 총 6번의 경기를 한다.
# 승리 +3점, 무승부 +1점, 패배 +0점
# 승점이 가장 높은 2팀은 32강으로 진출한다.

Team = {"A":["네덜란드","세네갈","에콰도르","카타르"],
        "B":["잉글랜드","웨일즈","미국","이란"],
        "C":["아르헨티나","멕시코","폴란드","사우디아라비아"],
        "D":["프랑스","튀니지","덴마크","호주"],
        "E":["스페인","독일","일본","코스타리카"],
        "F":["벨기에","크로아티아","모로코","캐나다"],
        "G":["브라질","세르비아","카메론","스위스"],
        "H":["포르투갈","우루과이","가나","대한민국"]
        }
round16 = [] # 16강 점수별로 뽑아내기위해
victory = [] # 16강 진출국가 저장
round8 = [] # 8강 진출국가
round4 = [] # 4강 진출국가
round2 = [] # 결승전 진출국가
champion = []
world = ["A","B","C","D","E","F","G","H"] # 문자열포매팅으로반복문을 돌려보자

# 리스트와 딕셔너리 진짜 몇번을 고쳤는지 모르겠다.
# 몇번을 엎었던 이유가 한팀의 경기가 6번씩 확실하게 돌아가는걸 확인하지 않고
# 무작정 함수부터 만들고 승률부터 집어 넣었다 그 결과 어디서부터 어떤것이 잘못되었는지 찾을 수 없게 되었다.

# print(Team["A"]) # 각 팀이 호출되는지 확인
# print(Team["A"][0],Team["A"][3]) # 원하는 팀만 호출되는지 확인

# print(Team.keys()) # Team속의 키값만 출력
list_keys = list(Team.keys()) # 키값을 리스트로 변환
list_values = list(Team.values()) # values값을 리스트로 변환
# print(list_keys) # 리스트 출력 확인
# print(list_keys.index("A")) # A팀 위치 찾기
# data = enumerate(list_keys) # 순서가 있는 자료형을 인덱스값과 함께 출력해주는 함수
# change = list(zip(Team.keys(),Team.values())) # 딕셔너리를 리스트로 변환 이럴꺼면 리스트쓰지 왜?

for value in 'A':
    print(f"{[value]}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def seed1():
    game = random.randrange(0,11)
    if 0 < game <= 7: # 랜덤으로 0~7까지 나온다면 그게 승률 70%
        return "승"
    else:
        return "패"

def seed2():
    game = random.randrange(0,11)
    if 0 < game <= 6: # 랜덤으로 0~6까지 나온다면 그게 승률 60%
        return "승"
    else:
        return "패"

def seed3():
    game = random.randrange(0,11)
    if 0 < game <= 4: # 랜덤으로 0~4까지 나온다면 그게 승률 40%
        return "승"
    else:
        return "패"

def seed4():
    game = random.randrange(0,11)
    if 0 < game <= 2: # 랜덤으로 0~2까지 나온다면 그게 승률 20%
        return "승"
    else:
        return "패"
# 이렇게 함수를 만드니깐 seed1과 seed2의 무승부가 너무 많이 나온다.

def tryoutA(): # 예선전을 위한 함수 만들기 이걸  8개를 안만들고 싶단 말이지..어떻게 줄일수있을까
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    j = 0
    i = 0
    for i in range(3): # 첫번째팀과 나머지 세팀의 경기
        print(Team["A"][j],"VS",Team["A"][i+1])
        if seed1() == seed2():
            print("'무승부'")
            total1 += 1
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1()=="승" or seed2()=="패":
            print("'승'")
            total1 += 3
        else:
            print("'패'")
            total2 += 3
            total3 += 3
            total4 += 3

    print(Team["A"][j],":",total1)
    round16.append([total1,Team["A"][j]])
    i = 0
    j += 1
    for i in range(2): # 두번째 팀과 나머지 두팀의 경기
        print(Team["A"][j],"VS",Team["A"][i+2])
        if seed2() == seed3():
            print("'무승부'")
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total2 += 3
        else:
            print("'패'")
            total3 += 3
            total4 += 3
    print(Team["A"][j],":",total2)
    round16.append([total2,Team["A"][j]])

    j = 2
    i = 0
    print(Team["A"][j], "VS",Team["A"][i+3]) #나머지 둘이 싸워라
    if seed3() == seed4():
        print("무승부")
        total3 += 1
        total4 += 1
    elif seed1() == "승" or seed2() == "패":
        print("승")
        total3 += 3
    else:
        print("패")
        total4 += 3
    print(Team["A"][j], ":", total3)
    round16.append([total3,Team["A"][j]])
    round16.append([total4,Team["A"][i+3]])
    print(*round16)
    print("=="*30)

    round16.sort()
    round16.reverse()
    victory.append(round16[0])
    victory.append(round16[1])
    print(*round16[0:2],"16강 진출합니다")
    del round16[:] # 다음나라를 위해 초기해해준다
# print(tryoutA())


def tryoutB(): # 예선전을 위한 함수 만들기 이걸  8개를 안만들고 싶단 말이지..어떻게 줄일수있을까
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    j = 0
    i = 0
    for i in range(3): # 첫번째팀과 나머지 세팀의 경기
        print(Team["B"][j],"VS",Team["B"][i+1])
        if seed1() == seed2():
            print("'무승부'")
            total1 += 1
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1()=="승" or seed2()=="패":
            print("'승'")
            total1 += 3
        else:
            print("'패'")
            total2 += 3
            total3 += 3
            total4 += 3

    print(Team["B"][j],":",total1)
    round16.append([total1,Team["B"][j]])
    i = 0
    j += 1
    for i in range(2): # 두번째 팀과 나머지 두팀의 경기
        print(Team["B"][j],"VS",Team["B"][i+2])
        if seed2() == seed3():
            print("'무승부'")
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total2 += 3
        else:
            print("'패'")
            total3 += 3
            total4 += 3
    print(Team["A"][j],":",total2)
    round16.append([total2,Team["B"][j]])

    j = 2
    i = 0
    print(Team["B"][j], "VS",Team["B"][i+3]) #나머지 둘이 싸워라
    if seed3() == seed4():
        print("무승부")
        total3 += 1
        total4 += 1
    elif seed1() == "승" or seed2() == "패":
        print("승")
        total3 += 3
    else:
        print("패")
        total4 += 3
    print(Team["B"][j], ":", total3)
    round16.append([total3,Team["B"][j]])
    round16.append([total4,Team["B"][i+3]])
    print(*round16)
    print("=="*30)

    round16.sort()
    round16.reverse()
    victory.append(round16[0])
    victory.append(round16[1])
    print(*round16[0:2],"16강 진출합니다")
    del round16[:]  # 다음나라를 위해 초기해해준다

# print(tryoutB())

def tryoutC(): # 예선전을 위한 함수 만들기 이걸  8개를 안만들고 싶단 말이지..어떻게 줄일수있을까
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    j = 0
    i = 0
    for i in range(3): # 첫번째팀과 나머지 세팀의 경기
        print(Team["C"][j],"VS",Team["C"][i+1])
        if seed1() == seed2():
            print("'무승부'")
            total1 += 1
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1()=="승" or seed2()=="패":
            print("'승'")
            total1 += 3
        else:
            print("'패'")
            total2 += 3
            total3 += 3
            total4 += 3

    print(Team["C"][j],":",total1)
    round16.append([total1,Team["C"][j]])
    i = 0
    j += 1
    for i in range(2): # 두번째 팀과 나머지 두팀의 경기
        print(Team["C"][j],"VS",Team["C"][i+2])
        if seed2() == seed3():
            print("'무승부'")
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total2 += 3
        else:
            print("'패'")
            total3 += 3
            total4 += 3
    print(Team["C"][j],":",total2)
    round16.append([total2,Team["C"][j]])

    j = 2
    i = 0
    print(Team["C"][j], "VS",Team["C"][i+3]) #나머지 둘이 싸워라
    if seed3() == seed4():
        print("무승부")
        total3 += 1
        total4 += 1
    elif seed1() == "승" or seed2() == "패":
        print("승")
        total3 += 3
    else:
        print("패")
        total4 += 3
    print(Team["C"][j], ":", total3)
    round16.append([total3,Team["C"][j]])
    round16.append([total4,Team["C"][i+3]])
    print(*round16)
    print("=="*30)

    round16.sort()
    round16.reverse()
    victory.append(round16[0])
    victory.append(round16[1])
    print(*round16[0:2],"16강 진출합니다")
    del round16[:]  # 다음나라를 위해 초기해해준다

# print(tryoutC())

def tryoutD(): # 예선전을 위한 함수 만들기 이걸  8개를 안만들고 싶단 말이지..어떻게 줄일수있을까
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    j = 0
    i = 0
    for i in range(3): # 첫번째팀과 나머지 세팀의 경기
        print(Team["D"][j],"VS",Team["D"][i+1])
        if seed1() == seed2():
            print("'무승부'")
            total1 += 1
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1()=="승" or seed2()=="패":
            print("'승'")
            total1 += 3
        else:
            print("'패'")
            total2 += 3
            total3 += 3
            total4 += 3

    print(Team["D"][j],":",total1)
    round16.append([total1,Team["D"][j]])
    i = 0
    j += 1
    for i in range(2): # 두번째 팀과 나머지 두팀의 경기
        print(Team["D"][j],"VS",Team["D"][i+2])
        if seed2() == seed3():
            print("'무승부'")
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total2 += 3
        else:
            print("'패'")
            total3 += 3
            total4 += 3
    print(Team["D"][j],":",total2)
    round16.append([total2,Team["D"][j]])

    j = 2
    i = 0
    print(Team["D"][j], "VS",Team["D"][i+3]) #나머지 둘이 싸워라
    if seed3() == seed4():
        print("무승부")
        total3 += 1
        total4 += 1
    elif seed1() == "승" or seed2() == "패":
        print("승")
        total3 += 3
    else:
        print("패")
        total4 += 3
    print(Team["D"][j], ":", total3)
    round16.append([total3,Team["D"][j]])
    round16.append([total4,Team["D"][i+3]])
    print(*round16)
    print("=="*30)

    round16.sort()
    round16.reverse()
    victory.append(round16[0])
    victory.append(round16[1])
    print(*round16[0:2],"16강 진출합니다")
    del round16[:]  # 다음나라를 위해 초기해해준다

# print(tryoutD())

def tryoutE():  # 예선전을 위한 함수 만들기 이걸  8개를 안만들고 싶단 말이지..어떻게 줄일수있을까
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    j = 0
    i = 0
    for i in range(3):  # 첫번째팀과 나머지 세팀의 경기
        print(Team["E"][j], "VS", Team["E"][i + 1])
        if seed1() == seed2():
            print("'무승부'")
            total1 += 1
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total1 += 3
        else:
            print("'패'")
            total2 += 3
            total3 += 3
            total4 += 3

    print(Team["E"][j], ":", total1)
    round16.append([total1, Team["E"][j]])
    i = 0
    j += 1
    for i in range(2):  # 두번째 팀과 나머지 두팀의 경기
        print(Team["E"][j], "VS", Team["E"][i + 2])
        if seed2() == seed3():
            print("'무승부'")
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total2 += 3
        else:
            print("'패'")
            total3 += 3
            total4 += 3
    print(Team["E"][j], ":", total2)
    round16.append([total2, Team["E"][j]])

    j = 2
    i = 0
    print(Team["E"][j], "VS", Team["E"][i + 3])  # 나머지 둘이 싸워라
    if seed3() == seed4():
        print("무승부")
        total3 += 1
        total4 += 1
    elif seed1() == "승" or seed2() == "패":
        print("승")
        total3 += 3
    else:
        print("패")
        total4 += 3
    print(Team["E"][j], ":", total3)
    round16.append([total3, Team["E"][j]])
    round16.append([total4, Team["E"][i + 3]])
    print(*round16)
    print("==" * 30)

    round16.sort()
    round16.reverse()
    victory.append(round16[0])
    victory.append(round16[1])
    print(*round16[0:2], "16강 진출합니다")
    del round16[:]  # 다음나라를 위해 초기해해준다

# print(tryoutE())

def tryoutF():  # 예선전을 위한 함수 만들기 이걸  8개를 안만들고 싶단 말이지..어떻게 줄일수있을까
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    j = 0
    i = 0
    for i in range(3):  # 첫번째팀과 나머지 세팀의 경기
        print(Team["F"][j], "VS", Team["F"][i + 1])
        if seed1() == seed2():
            print("'무승부'")
            total1 += 1
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total1 += 3
        else:
            print("'패'")
            total2 += 3
            total3 += 3
            total4 += 3

    print(Team["F"][j], ":", total1)
    round16.append([total1, Team["F"][j]])
    i = 0
    j += 1
    for i in range(2):  # 두번째 팀과 나머지 두팀의 경기
        print(Team["F"][j], "VS", Team["F"][i + 2])
        if seed2() == seed3():
            print("'무승부'")
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total2 += 3
        else:
            print("'패'")
            total3 += 3
            total4 += 3
    print(Team["F"][j], ":", total2)
    round16.append([total2, Team["F"][j]])

    j = 2
    i = 0
    print(Team["F"][j], "VS", Team["F"][i + 3])  # 나머지 둘이 싸워라
    if seed3() == seed4():
        print("무승부")
        total3 += 1
        total4 += 1
    elif seed1() == "승" or seed2() == "패":
        print("승")
        total3 += 3
    else:
        print("패")
        total4 += 3
    print(Team["F"][j], ":", total3)
    round16.append([total3, Team["F"][j]])
    round16.append([total4, Team["F"][i + 3]])
    print(*round16)
    print("==" * 30)

    round16.sort()
    round16.reverse()
    victory.append(round16[0])
    victory.append(round16[1])
    print(*round16[0:2], "16강 진출합니다")
    del round16[:]  # 다음나라를 위해 초기해해준다

# print(tryoutF())

def tryoutG():  # 예선전을 위한 함수 만들기 이걸  8개를 안만들고 싶단 말이지..어떻게 줄일수있을까
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    j = 0
    i = 0
    for i in range(3):  # 첫번째팀과 나머지 세팀의 경기
        print(Team["G"][j], "VS", Team["G"][i + 1])
        if seed1() == seed2():
            print("'무승부'")
            total1 += 1
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total1 += 3
        else:
            print("'패'")
            total2 += 3
            total3 += 3
            total4 += 3

    print(Team["G"][j], ":", total1)
    round16.append([total1, Team["G"][j]])
    i = 0
    j += 1
    for i in range(2):  # 두번째 팀과 나머지 두팀의 경기
        print(Team["G"][j], "VS", Team["G"][i + 2])
        if seed2() == seed3():
            print("'무승부'")
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total2 += 3
        else:
            print("'패'")
            total3 += 3
            total4 += 3
    print(Team["G"][j], ":", total2)
    round16.append([total2, Team["G"][j]])

    j = 2
    i = 0
    print(Team["G"][j], "VS", Team["G"][i + 3])  # 나머지 둘이 싸워라
    if seed3() == seed4():
        print("무승부")
        total3 += 1
        total4 += 1
    elif seed1() == "승" or seed2() == "패":
        print("승")
        total3 += 3
    else:
        print("패")
        total4 += 3
    print(Team["G"][j], ":", total3)
    round16.append([total3, Team["G"][j]])
    round16.append([total4, Team["G"][i + 3]])
    print(*round16)
    print("==" * 30)

    round16.sort()
    round16.reverse()
    victory.append(round16[0])
    victory.append(round16[1])
    print(*round16[0:2], "16강 진출합니다")
    del round16[:]  # 다음나라를 위해 초기해해준다

# print(tryoutG())

def tryoutH():  # 예선전을 위한 함수 만들기 이걸  8개를 안만들고 싶단 말이지..어떻게 줄일수있을까
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    j = 0
    i = 0
    for i in range(3):  # 첫번째팀과 나머지 세팀의 경기
        print(Team["H"][j], "VS", Team["H"][i + 1])
        if seed1() == seed2():
            print("'무승부'")
            total1 += 1
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total1 += 3
        else:
            print("'패'")
            total2 += 3
            total3 += 3
            total4 += 3

    print(Team["H"][j], ":", total1)
    round16.append([total1, Team["H"][j]])
    i = 0
    j += 1
    for i in range(2):  # 두번째 팀과 나머지 두팀의 경기
        print(Team["H"][j], "VS", Team["H"][i + 2])
        if seed2() == seed3():
            print("'무승부'")
            total2 += 1
            total3 += 1
            total4 += 1
        elif seed1() == "승" or seed2() == "패":
            print("'승'")
            total2 += 3
        else:
            print("'패'")
            total3 += 3
            total4 += 3
    print(Team["H"][j], ":", total2)
    round16.append([total2, Team["H"][j]])

    j = 2
    i = 0
    print(Team["H"][j], "VS", Team["H"][i + 3])  # 나머지 둘이 싸워라
    if seed3() == seed4():
        print("무승부")
        total3 += 1
        total4 += 1
    elif seed1() == "승" or seed2() == "패":
        print("승")
        total3 += 3
    else:
        print("패")
        total4 += 3
    print(Team["H"][j], ":", total3)
    round16.append([total3, Team["H"][j]])
    round16.append([total4, Team["H"][i + 3]])
    print(*round16)
    print("==" * 30)

    round16.sort()
    round16.reverse()
    victory.append(round16[0])
    victory.append(round16[1])
    print(*round16[0:2], "16강 진출합니다")
    del round16[:]  # 다음나라를 위해 초기해해준다

# print(tryoutH())
# print(*victory)

print("      >>>""  조 예선전 시작합니다 <<<")
print("=========================================")
print("            경 기 s t a r t!")
print("=========================================")

print(tryoutA())
print(tryoutB())
print(tryoutC())
print(tryoutD())
print(tryoutE())
print(tryoutF())
print(tryoutG())
print(tryoutH())
print("예선전 종료!")
for i in range(0,16):
    print(i+1,"위",victory[i][1]) # 프린트안에서 값을 더해줘서 1위부터 출력
    round8.append(victory[i][1]) # 16개국 리스트 저장을 위해여

print("      >>>""  16강전  시작합니다 <<<")
print("=========================================")
print("            경 기 s t a r t!")
print("=========================================")

for i in range(0,len(round8),2): # 16강전
    print((round8[i]),"VS", (round8[i+1]),"경기 시작합니다.")
    if seed1() == "승" or seed2() == "패":
        print(round8[i],"승")
        round4.append([round8[i]])
        i += 1
    else:
        print(round8[i+1],"승")
        round4.append([round8[i]])

print("8강전 진출국가 :",*round4)

print("      >>>""  8 강전  시작합니다 <<<")
print("=========================================")
print("            경 기 s t a r t!")
print("=========================================")

for i in range(0,len(round4),2): # 8강전
    print((round4[i]),"VS", (round4[i+1]),"경기 시작합니다.")
    if seed1() == "승" or seed2() == "패":
        print(round4[i],"승")
        round2.append([round4[i]])
        i += 1
    else:
        print(round4[i],"승")
        round2.append([round4[i]])

print("4강전 진출국가 :", *round2)

print("      >>>""  4 강전  시작합니다 <<<")
print("=========================================")
print("            경 기 s t a r t!")
print("=========================================")

for i in range(0,len(round2),2): # 4강전
    print((round2[i]),"VS", (round2[i+1]),"경기 시작합니다.")
    if seed1() == "승" or seed2() == "패":
        print(round2[i],"승")
        champion.append([round2[i]])
        i += 1
    else:
        print(round2[i],"승")
        champion.append([round2[i]])

print("결승전 진출국가 :", *champion)

print("      >>>""결 승 전  시작합니다 <<<")
print("=========================================")
print("            경 기 s t a r t!")
print("=========================================")

for i in range(1):  # 결승
    print((round2[i]), "VS", (round2[i + 1]), "경기 시작합니다.")
    if seed1() == "승" or seed2() == "패":
        print("우승국가는:",round2[i], "승")
        round2.append([champion[i]])
        i += 1
    else:
        print(round2[i], "승")

