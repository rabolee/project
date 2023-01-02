import random
import time
import keyboard
import copy


monster = ['🤢','🤖','💀','🐻','🧐','😎','😈']

def map(): # 보여주기용 맵

       a = [['⬛'] * 15 for i in range(15)]
       return a

def realMap(): # 그림자처리 실제 맵

       rmap = [['🟨'] * 17 for i in range(17)]
       for i in range(0, 17): # 맵을 넘어가면 벽으로 둘러주기
              rmap[0][i-1] = '❌'
              rmap[i-1][0] = '❌'
              rmap[-1][i] ='❌'
              rmap[i][-1] ='❌'

       for i in range (0,50):
              x = random.randrange(1, 15)
              y = random.randrange(1, 15)
              rmap[x][y] = '⚔' # 몬스터 랜덤
       while True:
              x = random.randrange(1, 15)
              y = random.randrange(1, 15)
              if rmap[x][y] == '⚔':
                     continue
              rmap[x][y] = '🌀' # 포탈 랜덤
              break

       for i in range(0, 30):
              x = random.randrange(1, 15)
              y = random.randrange(1, 15)
              if rmap[x][y] == '⚔' or rmap[x][y] =='🌀':
                     continue
              rmap[x][y] = '❤' # 포션 랜덤

       return rmap

def move(): # 맵 호출, 캐릭터이동

       count = 0
       x=1
       y=1
       a = map()
       c = copy.deepcopy(a)
       b= realMap()
       a[x][y] = '🐯' # 캐릭터 위치
       for i in b:  # 콘솔에 출력
              for j in i:
                     print(j, end=" ")
              print()

       for i in a:  # 콘솔에 출력
              for j in i:
                     print(j, end=" ")
              print()

       print(" [↑ 상, ↓ 하, ← 좌, → 우] 방향을 눌러 이동하세요")

       while True:
              if keyboard.is_pressed('right'):
                     time.sleep(0.1) # 오른쪽 이동
                     if y == '❌':
                            print('❌오른쪽으로 이동불가❌')
                            continue

                     a = copy.deepcopy(c)
                     a[x][y + 1] = '🐯'
                     y += 1  # 내 위치 저장
                     a[x-1][y-1] = b[x-1][y-1] # 좌상
                     a[x-1][y] = b[x-1][y] # 상
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # 우상
                     a[x][y - 1] = b[x][y - 1]  # 좌
                     a[x][y +1] = b[x][y + 1] #우
                     a[x+1][y-1] = b[x+1][y - 1] # 좌하
                     a[x + 1][y] = b[x+1][y]  # 하
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # 우하
                     count += 1
                     for i in a:
                            for j in i:
                                   print(j, end=" ")
                            print()
                     print(' ')

              if keyboard.is_pressed('left'):
                     time.sleep(0.1) # 왼쪽 이동
                     if y == '❌':
                            print('❌왼쪽으로 이동불가❌')
                            continue
                     a = copy.deepcopy(c)
                     a[x][y - 1] = '🐯'
                     y -= 1  # 내 위치 저장
                     a[x - 1][y - 1] = b[x - 1][y - 1]  # 좌상
                     a[x - 1][y] = b[x - 1][y]  # 상
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # 우상
                     a[x][y - 1] = b[x][y - 1]  # 좌
                     a[x][y + 1] = b[x][y + 1]  # 우
                     a[x + 1][y - 1] = b[x + 1][y - 1]  # 좌하
                     a[x + 1][y] = b[x + 1][y]  # 하
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # 우하
                     count += 1
                     for i in a:
                            for j in i:
                                   print(j, end=" ")
                            print()
                     print(' ')

              if keyboard.is_pressed('up'):
                     time.sleep(0.1) # 위쪽 이동
                     if x == '❌':
                            print('❌위쪽으로 이동불가❌')
                            continue
                     a = copy.deepcopy(c)
                     a[x - 1][y] = '🐯'
                     x -= 1  # 내 위치 저장
                     a[x - 1][y - 1] = b[x - 1][y - 1]  # 좌상
                     a[x - 1][y] = b[x - 1][y]  # 상
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # 우상
                     a[x][y - 1] = b[x][y - 1]  # 좌
                     a[x][y + 1] = b[x][y + 1]  # 우
                     a[x + 1][y - 1] = b[x + 1][y - 1]  # 좌하
                     a[x + 1][y] = b[x + 1][y]  # 하
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # 우하
                     count += 1
                     for i in a:
                            for j in i:
                                   print(j, end=" ")
                            print()
                     print(' ')

              if keyboard.is_pressed('down'):
                     time.sleep(0.1) # 아래쪽 이동
                     if x == '❌':
                            print('❌아래쪽으로 이동불가❌')
                            continue
                     a = copy.deepcopy(c)
                     a[x + 1][y] = '🐯'
                     x += 1  # 내 위치 저장
                     a[x - 1][y - 1] = b[x - 1][y - 1]  # 좌상
                     a[x - 1][y] = b[x - 1][y]  # 상
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # 우상
                     a[x][y - 1] = b[x][y - 1]  # 좌
                     a[x][y + 1] = b[x][y + 1]  # 우
                     a[x + 1][y - 1] = b[x + 1][y - 1]  # 좌하
                     a[x + 1][y] = b[x + 1][y]  # 하
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # 우하
                     count += 1
                     for i in a:
                            for j in i:
                                   print(j, end=" ")
                            print()
                     print(' ')


def win (): # 승리시
    print("""
   _   _  _____  _____  _                       
 | | | ||_   _|/  __ \| |                      
 | | | |  | |  | /  \/| |_   ___   _ __  _   _ 
 | | | |  | |  | |    | __| / _ \ | '__|| | | |
 \ \_/ / _| |_ | \__/\| |_ | (_) || |   | |_| |
  \___/  \___/  \____/ \__| \___/ |_|    \__, |
                                          __/ |
                                         |___/ 
""")
def lose (): # 패배시
    print("""
  _____   ___  ___  ___ _____   _____  _   _  _____ ______ 
|  __ \ / _ \ |  \/  ||  ___| |  _  || | | ||  ___|| ___ |
| |  \// /_\ \| .  . || |__   | | | || | | || |__  | |_/ /
| | __ |  _  || |\/| ||  __|  | | | || | | ||  __| |    / 
| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ /| |___ | |\ \ 
 \____/\_| |_/\_|  |_/\____/   \___/  \___/ \____/ \_| \_|
 
""")

def battle_monster(): # 몬스터 출현
    rand=random.randrange(100)
    M_HP=0
    M_power=0
    M_name=0
    monster_list=['🤢 좀비','🤖 구울','💀 해골','🐻 버그베어','🧐 동혀니','😎 홍거리','😈 디아복로']

    if rand < 48:
        M_name = monster_list[0]
        M_HP = random.randrange(300,501)
        M_power = 100
    elif 48 <= rand < 78:
        M_name=monster_list[1]
        M_HP = random.randrange(450, 701)
        M_power = 180
    elif 78 <= rand < 90:
        M_name=monster_list[2]
        M_HP = random.randrange(480, 801)
        M_power = 220
    elif 90 <= rand < 95:
        M_name=monster_list[3]
        M_HP = random.randrange(550, 901)
        M_power = 350
    elif 95 <= rand < 97:
        M_name=monster_list[4]
        M_HP = random.randrange(3000, 8001)
        M_power = random.randrange(1000, 3001)
    elif 97 <= rand < 99:
        M_name=monster_list[5]
        M_HP = random.randrange(3000, 8001)
        M_power = random.randrange(1000, 3001)
    elif rand == 99:
        M_name=monster_list[6]
        M_HP = random.randrange(5000, 15001)
        M_power = random.randrange(2500, 8001)
    return M_name, M_HP, M_power



def user_attack (M_name, M_HP,user_power): # 초코의용 공격
    print()
    print(f'⚔ 초코의용 공격 ⚔')
    print(f' [공격력 : {user_power}]')
    M_HP -= user_power
    print(f'{M_name} 남은 체력 : {M_HP}')
    return M_name, M_HP

def monster_attack (M_name, M_power, user,count_Exturn): # 몬스터와 전투
    if count_Exturn >=0:
        print(f'⚔ {M_name} 공격⚔!')
        user[1] -= 0
        print(f'초코의용 남은 체력 : ({M_power}-{user[1]})')
        print(f'포션 수 {user[2]}\n')
        print(f"엘릭서 수 {user[3]}")
        return M_name, M_power, user
    else:
        print(f'{M_name} 공격 ⚔!')
        user[1] -= M_power
        print(f'초코의용 남은 체력 : {user[1]}')
        return M_name, M_power, user

def run(): # 도망가기
    rand = random.randrange(2)
    if rand == 0:
        print()
        print(f'도망성공 🏳')
        print(f'맵으로 돌아갑니다!!!\n')
    else:
        print()
        print(f'도망실패 🏴')
        print(f'전투복귀 ⚔!\n')
    return rand

def potion(user): # 포션 사용
    user[1] = user[0] #변화된 hp에 기본hp 대입, 초기화
    if user[2] >= 1: #포션개수가 1개이상이면
        print()
        print(f'❤ 포션사용 ❤!')
        print(f'초코의용HP {user[1]}만큼 회복')
        user[2] -= 1     # 포션개수차감
        # print(f'❤ 포션남은개수: {user[2]}\n')
        return user, 1
    else :     # 포션없으면
        print()
        print(f'❤포션남은개수: 0')
        print(f'전투복귀!!!\n')
        return user, 0


def elixir(user): # 엘릭서 사용
    if user[3] > 0:  # 엘릭서 개수
        print("✨엘릭서를 사용합니다")
        print("✨앞으로 10턴 동안 무적상태가 됩니다✨")
        user[3] -= 1    # 엘릭서 개수 차감
        return user, 10    # 10턴 동안 돌리기 위함
    else:
        print("엘릭서가 없습니다")
        return user, 0

def potion_drop(user): # 포션 얻기
    rand = random.randrange(2) # 50%확률로 포션 받음.
    if rand == 0: # 포션받음
        rand = random.uniform(0,100) #uniform 0부터 100까지 실수 출력
        # print(rand)
        if rand <= 1:
            print("✨ 엘릭서 획득 ✨")
            user[3] += 1 # 엘릭서 개수 더하기
        else :
            print("❤ 포션 획득 ❤")
            user[2] += 1 # 포션 개수 더하기
            print(f"포션 수: {user[2]}")
    else : #포션 못받음
        print("❌포션 획득 실패❌")

    return user

def test (): # 초코의용 현재상태
    user = [500, 500, 5, 5,0] # 기본hp, hp변화, 포션수, 엘릭서수
    print('----' * 15)
    print("              🐯 초코의용군 현재 상태 🐯")
    print(f"     [기본HP:{user[0]}]  [HP변화:{user[1]}]  [포션수:{user[2]}]  [엘릭서수:{user[3]}]")
    print('----' * 15)
    count_Exturn = 0
    M_name, M_HP, M_power = battle_monster()
    print(f"                   {M_name} 등장")
    print(f'           {M_name} [HP {M_HP}] [공격력 {M_power}]')
    print('----' * 15)

    while True:
        user_power = random.randrange(100,151)  # 공격력, 리스트 마지막에 추가됨
        user[4] = user_power
        if count_Exturn >=0:
            count_Exturn-=1
        choice = int(input(f"[1.⚔ 공격하기]  [2.🚴‍ 도망가기]  [3.❤포션({user[2]}개)]  [4.✨엘릭서({user[3]}개)]"))
        if choice == 1:
            M_name, M_HP = user_attack (M_name, M_HP,user_power)
            if M_HP > 0:   # HP -되면 공격 못함
                M_name,M_power, user = monster_attack(M_name, M_power, user, count_Exturn)
        elif choice == 2:
            rand = run()
            if rand == 0:    # 도망 성공
                break
            else:    # 도망 실패
                M_name, M_power, user = monster_attack(M_name, M_power, user,count_Exturn)
        elif choice == 3:
            succes = potion(user)    # 포션 성공
            M_name, M_power, user = monster_attack(M_name, M_power, user, count_Exturn)
        elif choice == 4:
            count_Exturn = elixir(user)[1]
            M_name, M_power, user = monster_attack(M_name, M_power, user, count_Exturn)
        else:
            print("잘못눌렀습니다. 다시 선택해주세요")
            continue
        if M_HP <= 0:
            print("                                 [초코의용 승🏆]")
            print(win())
            print("🥇 초코의용 레벨업 🥇")
            user_copy = user[:]    # HP변화 유지하려고 복사
            user_copy[4] = user_copy[4] + (user_copy[4]*0.05)    # 공격력 증가
            user_copy[0] = user_copy[0] + (user_copy[0]*0.05)    # HP 증가
            user[1] = user[0]     # HP 변화 초기화
            user = potion_drop(user)
            break
        elif user[1] <= 0:
            print("                                 [초코의용 패🏳]")
            print(lose())

            break
    return user_copy



# ----------------------------main함수 시작 --------------------------------------
print(f'{monster}가 나타납니다')
print(' ')
user = test()
print(user)
