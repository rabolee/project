import random
import time
import keyboard
import copy

def hi(xy,user): # 포털이동 층 변경

    if xy == '🌀':
       print("- - - - - - - - - - - - - - - - - - - - - -[{}층으로 이동]".format(user[7]+1))
       po()
       if user[7]==2:
           print("                                        [마지막 던전입니다]")

       user[7]+=1
       return user

    elif xy == '❤': # 포션
        user[2] += 1  # 포션 개수 더하기
        print(f"❤포션 획득 ({user[2]})개❤")

        return user
    elif xy == '⚔': # 몬스터
        fight(user)

        return user
    else:
        return user

    # return 0

def map(): # 보여주기맵

       a = [["⬛"] * 17 for i in range(17)]
       return a

def realMap(user): # 찐 맵

       rmap = [['🟨'] * 17 for i in range(17)]
       for i in range(0, 17):
              rmap[0][i] = "❌"
              rmap[i][0] = "❌"
              rmap[-1][i] = "❌"
              rmap[i][-1] = "❌"

       for i in range (0,40):
              x = random.randrange(1,16)
              y = random.randrange(1,16)
              rmap[x][y]= '❤'
       while True:
        if user[7]==3: # 3층이상 포탈생성금지
            break
        else:
              x = random.randrange(1, 16)
              y = random.randrange(1, 16)
              if rmap[x][y]=='❤':
                     continue
              rmap[x][y]='🌀'
              break

       for i in range(0, 50):
              x = random.randrange(1, 16)
              y = random.randrange(1, 16)
              if rmap[x][y] == '❤' or rmap[x][y] =='🌀':
                     continue
              rmap[x][y] = '⚔'

       return rmap


def monster_Relocation(b):
    for i in range(1, 16):
        for j in range(1,15):
            if b[i][j] == '⚔':
                b[i][j] = '🟨'
    for i in range(0, 20):
        x = random.randrange(1, 16)
        y = random.randrange(1, 16)
        if b[x][y] == '❤' or b[x][y] == '🌀':
            continue
        b[x][y] = '⚔' # 몬스터
    return b

def po(): # 포탈이동시
    print("""
               .......                        
               ......:*===~.,....                 
             ... ..  =@@@@!   ......              
            ...      =@@@@!     .....             
            ...      =@;;@!      .....            
             ...,.   =@~-@!      ....             
              . .....=@~-@!   ...,..              
                   ..=@::@!....                   
                     ;*,,*~                       
                                                  
                                                  
                          .                       
                     ..   .                       
                     ,   ,                        
                     -   ,.                       
                  .  :.  -,                       
                  ,  ;.  -,  .                    
                  -  !.  :,  ,                    
                  ~  *.  :, .-                    
                  ;  !.  ~-  ~                    
                  *          :                    
                  *   ;##~  .;                    
                  *   @@@@. .;                    
                  ~   @@@@.  -                    
                 .!,..*@@;..:$..                  
             ....!@@@:!@@;*@@@- ...               
            . .. .:$@@@@@@@@!,   . .              
            .       -#@@@@=.       ..             
              .      =@@@@!   ... ..              
              .. ... =@@@@!    . .                
                .......,,.....      
                              
    """)
    time.sleep(0.1)

def win(): # 전투승리시

    print("""
    __      __ _  _ __   _ __    ___  _ __ 
    \ \ /\ / /| || '_ \ | '_ \  / _ \| '__|
     \ V  V / | || | | || | | ||  __/| |   
      \_/\_/  |_||_| |_||_| |_| \___||_|   
      
""")

def com(): # 디아복로 승리
    print("""
                                _        _         
                               | |      | |        
  ___   ___   _ __ ___   _ __  | |  ___ | |_   ___ 
 / __| / _ \ | '_ ` _ \ | '_ \ | | / _ \| __| / _ |
| (__ | (_) || | | | | || |_) || ||  __/| |_ |  __/
 \___| \___/ |_| |_| |_|| .__/ |_| \___| \__| \___|
                        | |                        
                        |_|                  
    """)

def lose():  # 패배시

    print("""
  _____   ___  ___  ___ _____   _____  _   _  _____ ______
|  __ \ / _ \ |  \/  ||  ___| |  _  || | | ||  ___|| ___ |
| |  \// /_\ \| .  . || |__   | | | || | | || |__  | |_/ /
| | __ |  _  || |\/| ||  __|  | | | || | | ||  __| |    /
| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ /| |___ | |\ |
 \____/\_| |_/\_|  |_/\____/   \___/  \___/ \____/ \_| \_|

""")

def fist():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⢿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⣿⡿⠏⠀⠀⠀⠀⠀⠀⠀⣈⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⣿⣿⣿⣿⣷⠀⠀⠀⢈⠑⢄⡀⢀⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡏⠙⠷⠖⠒⠉⠀⠈⠛⠟⠉⠀⣹⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣤⣄⣀⣀⣀⠀⣀⣀⣀⣿⠀⢀⣠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⠿⠿⠿⠿⠿⠿⠛⠛⢛⣥⣾⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠀⠀⠀⠀⠀⠀⣴⣿⠟⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠀⠀⠀⠀⠀⠀⣼⡿⠃⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣿⠋⠀⠀⠀⠀⠈⠛⠻⠏⠀⠀⣨⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          """)

def user_staus ():
    user = [500, 500, 0, 0, 0, 100, 150,1]    # 기본hp, hp변화, 포션수, 엘릭서수, 랜덤공격력, 최초공격력, 최대공격력, 층
    return user

def battle_monster():
    rand=random.randrange(100)
    M_HP=0
    M_power=0
    M_name=0
    monster_list = ['🤢 좀비', '🤖 구울', '💀 해골', '🐻 버그베어', '🧐 동혀니', '😎 홍거리', '😈 디아복로']

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
    return M_name, M_HP, M_power,monster_list    # 디아복로 잡았을 때 시스템 종료시키려고 monster_list추가



def user_attack (M_name, M_HP,user_power):
    print()
    print(f'⚔ 초코의용 공격 ⚔')
    print(f' [공격력 : {user_power}]')
    M_HP -= user_power
    print(f'{M_name} 남은 체력 : {M_HP}')
    return M_name, M_HP


def monster_attack (M_name, M_power, user,count_Exturn):
    if count_Exturn >0:
        print(f'⚔ {M_name} 공격⚔!')
        user[1] -= 0
        return M_name, M_power, user

    else:
        print(f'{M_name} 공격 ⚔!')
        user[1] -= M_power
        print(f'초코의용 남은 체력 : {user[1]}')
        return M_name, M_power, user

def run():
    rand = random.randrange(2)
    if rand == 0:
        print()
        print(f'도망성공 🏳')
        print(f'맵으로 돌아갑니다!\n')
    else:
        print()
        print(f'도망실패 🏴')
        print(f'전투복귀!!!\n')
    return rand

def potion(user):

    if user[2] >= 1: #포션개수가 1개이상이면
        print()
        print(f'❤ 포션사용 ❤!')
        print(f'초코의용HP {user[0]}만큼 회복')
        user[1] = user[0]  # 변화된 hp에 기본hp 대입, 초기화
        user[2] -= 1  # 포션차감
        return user
    else :     # 포션없으면
        print()
        print(f'❤ 포션남은개수: 0')
        print(f'⚔전투복귀⚔\n')
        return user


def elixir(user):
    if user[3] > 0:  # 엘릭서 개수
        print("✨엘릭서를 사용합니다")
        print("✨앞으로 10턴 동안 무적상태가 됩니다✨")
        user[3] -= 1       #엘릭서 차감
        return user, 10    #10턴 동안 돌리기 위함
    else:
        print("엘릭서가 없습니다")
        return user, 0

def potion_drop(user): #포션얻기
    rand = random.randrange(2) #50%확률로 포션 받음.
    if rand == 0: #포션받음
        rand = random.uniform(0,100) #uniform 0부터 100까지 실수 출력
        # print(rand)
        if rand <= 0.5:
            print("✨ 엘릭서 획득 ✨")
            user[3] += 1 # 엘릭서 개수 더하기
        else :
            user[2] += 1  # 포션 개수 더하기
            print(f"❤ 포션 획득 ❤ ({user[2]})개")
            print(" ")
            # print(f"포션 수: {user[2]}")
    else : #포션 못받음
        print("❌포션 획득 실패❌")
        print(" ")

    return user

def fight (user):

    print('----' * 15)
    print("                🐯 초코의용군 현재 상태 🐯")
    print(f"      [ ❤ : {user[0]}]  [ 🐯 : {user[1]}]  [ 🧴 : {user[2]}]  [ ✨ : {user[3]}]")
    print(f"              💪[최소공격력: {user[5]}] 💪💪[최대공격력: {user[6]}]")
    print('----' * 15)
    count_Exturn = 0

    # user = user_staus()
    M_name, M_HP, M_power,monster_list = battle_monster()
    print(" ")
    print(f"                     {M_name} 등장")
    print(f'             {M_name} [HP {M_HP}] [공격력 {M_power}]')
    print('----' * 15)
    fist()

    while True:
        user_power = random.randint(user[5],user[6])
        user[4] = user_power
        if count_Exturn >0:
            count_Exturn-=1
        print(' ')
        choice = int(input(f"[1.⚔ 공격하기] [2.🚴‍ 도망가기] [3.🧴 포션({user[2]}개)] [4.✨엘릭서({user[3]}개)]"))
        print('----' * 15)
        if choice == 1:
            M_name, M_HP = user_attack (M_name, M_HP,user_power)
            if M_HP > 0:
                M_name,M_power, user = monster_attack(M_name, M_power, user, count_Exturn)
        elif choice == 2:
            rand = run()
            if rand == 0:    #도망 성공
                break
            else:    # 도망 실패
                M_name, M_power, user = monster_attack(M_name, M_power, user,count_Exturn)
        elif choice == 3:
            user = potion(user)    #포션 성공
            M_name, M_power, user = monster_attack(M_name, M_power, user, count_Exturn)
        elif choice == 4:
            count_Exturn = elixir(user)[1]
            M_name, M_power, user = monster_attack(M_name, M_power, user, count_Exturn)
        else:
            print("잘못눌렀습니다. 다시 선택해주세요")
            continue
        if M_name == monster_list[6]:    #몬스터가 디아복로 일때
            if M_HP <= 0:
                print("⚔드디어 최종보스 디아복로를 물리쳤습니다⚔")
                print("초코의용군이 던전 마스터가 됐습니다~~~~~~👍")
                com() # 승리시 complete
                user[0]=1
                exit()
        elif M_HP <= 0:     #그 외 몬스터를 잡았을 때
            print("                                        [초코의용 승🏆]")
            win()
            print("🥇 초코의용 레벨업 🥇")
            user[5] =int(user[5] *1.05)
            user[6] =int(user[6] *1.05)
            user[0] =int(user[0] *1.05)
            user = potion_drop(user)
            break

        elif user[1] <= 0:
            print("                                             [초코의용 패🏳]")
            lose()
            exit()
    return user

def move(): # 맵 호출, 캐릭터값을 받아와서 움직임 함수
    user = user_staus()
    count = 0
    while True:
       floor = 0
       x=1
       y=1
       a = map()
       c = copy.deepcopy(a)
       b= realMap(user)
       a[x][y]='🐯'
       a[x - 1][y - 1] = b[x - 1][y - 1]  # 좌상
       a[x - 1][y] = b[x - 1][y]  # 상
       a[x - 1][y + 1] = b[x - 1][y + 1]  # 우상
       a[x][y - 1] = b[x][y - 1]  # 좌
       a[x][y + 1] = b[x][y + 1]  # 우
       a[x + 1][y - 1] = b[x + 1][y - 1]  # 좌하
       a[x + 1][y] = b[x + 1][y]  # 하
       a[x + 1][y + 1] = b[x + 1][y + 1]  # 우하
       for i in a:  # 콘솔에 출력기능
           for j in i:
               print(j, end=" ")
           print()
       print(" ")

       # for i in b:  # 콘솔에 출력기능
       #        for j in i:
       #               print(j, end=" ")
       #        print()

       # for i in a:  # 콘솔에 출력기능
       #        for j in i:
       #               print(j, end=" ")
       #        print()

       print("     [↑ 상, ↓ 하, ← 좌, → 우] 방향을 눌러 이동하세요")
       while True:
              if count >=3 and count%3==0:
                    b=monster_Relocation(b)

              if keyboard.is_pressed('right'):
                     time.sleep(0.1) # 오른으로 이동
                     if y == 15:
                            print('오른쪽으로 이동불가')
                            continue

                     a = copy.deepcopy(c)
                     floor = user[7]
                     user=hi(b[x][y+1],user)
                     if user[7]>floor:
                         break
                     a[x][y + 1] = '🐯'
                     b[x][y + 1] = '🟨'
                     y += 1  # 내위치 저장
                     a[x-1][y-1] = b[x-1][y-1] #좌상
                     a[x-1][y] = b[x-1][y] #상
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # 우상
                     a[x][y - 1] = b[x][y - 1]  # 좌
                     a[x][y +1] = b[x][y + 1] #우
                     a[x+1][y-1] = b[x+1][y - 1] #좌하
                     a[x + 1][y] = b[x+1][y]  # 하
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # 우하
                     count+=1
                     for i in a:  # 콘솔에 출력기능
                            for j in i:
                                   print(j, end=" ")
                            print()
                     print(" ")

              if keyboard.is_pressed('left'):
                     time.sleep(0.1) # 왼쪽으로 이동
                     if y ==  1:
                            print('왼쪽으로 이동불가')
                            continue
                     a = copy.deepcopy(c)
                     floor = user[7]
                     user = hi(b[x][y-1],user)
                     if user[7] > floor:
                         break
                     a[x][y - 1] = '🐯'
                     b[x][y - 1] = '🟨'
                     y -= 1  # 내위치 저장
                     a[x - 1][y - 1] = b[x - 1][y - 1]  # 좌상
                     a[x - 1][y] = b[x - 1][y]  # 상
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # 우상
                     a[x][y - 1] = b[x][y - 1]  # 좌
                     a[x][y + 1] = b[x][y + 1]  # 우
                     a[x + 1][y - 1] = b[x + 1][y - 1]  # 좌하
                     a[x + 1][y] = b[x + 1][y]  # 하
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # 우하
                     count += 1
                     for i in a:  # 콘솔에 출력기능
                            for j in i:
                                   print(j, end=" ")
                            print()
                     print(" ")

              if keyboard.is_pressed('up'):
                     time.sleep(0.1) # 위쪽으로 이동
                     if x == 1:
                            print('위쪽으로 이동불가')
                            continue
                     a = copy.deepcopy(c)
                     floor = user[7]
                     user = hi(b[x-1][y],user)
                     if user[7] > floor:
                         break
                     a[x - 1][y] = '🐯'
                     b[x - 1][y] = '🟨'
                     x -= 1  # 내위치 저장
                     a[x - 1][y - 1] = b[x - 1][y - 1]  # 좌상
                     a[x - 1][y] = b[x - 1][y]  # 상
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # 우상
                     a[x][y - 1] = b[x][y - 1]  # 좌
                     a[x][y + 1] = b[x][y + 1]  # 우
                     a[x + 1][y - 1] = b[x + 1][y - 1]  # 좌하
                     a[x + 1][y] = b[x + 1][y]  # 하
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # 우하
                     count += 1
                     for i in a:  # 콘솔에 출력기능
                            for j in i:
                                   print(j, end=" ")
                            print()
                     print(" ")

              if keyboard.is_pressed('down'):
                     time.sleep(0.1) # 아래쪽으로 이동
                     if x == 15:
                            print('아래쪽으로 이동불가')
                            continue
                     a = copy.deepcopy(c)
                     floor = user[7]
                     user=hi(b[x + 1][y],user)
                     if user[7] > floor:
                         break
                     a[x + 1][y] = '🐯'
                     b[x + 1][y] = '🟨'
                     x += 1  # 내위치 저장
                     a[x - 1][y - 1] = b[x - 1][y - 1]  # 좌상
                     a[x - 1][y] = b[x - 1][y]  # 상
                     a[x - 1][y + 1] = b[x - 1][y + 1]  # 우상
                     a[x][y - 1] = b[x][y - 1]  # 좌
                     a[x][y + 1] = b[x][y + 1]  # 우
                     a[x + 1][y - 1] = b[x + 1][y - 1]  # 좌하
                     a[x + 1][y] = b[x + 1][y]  # 하
                     a[x + 1][y + 1] = b[x + 1][y + 1]  # 우하
                     count += 1
                     for i in a:  # 콘솔에 출력기능
                            for j in i:
                                   print(j, end=" ")
                            print( )
                     print(" ")


              if user[0]==1 or user[1]<=0:
                  return

print(" ")
print("     초코의용은 디아복로를 물리치기위해 던전으로 향한다...!")
time.sleep(0.1)
print("     초코의용은 던젼마스터가 될수 있을까..?")
print(" ")
print(" - - - - - - 던 전 으 로 입 장 합 니 다 - - - - - - - - - ")
time.sleep(0.1)

move()