import random
import os
import threading
import time
import pygame
import sys

class monster:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.x = 900                    # x축 800 맵 크기에서 시작
        if name == '치코리' or name == '피카츄' or name == '꼬부기':
            self.y = 400 - height             # y축 400 맵 크기에서 이미지 높이 뺀 만큼
        else:
            self.y = 400 - height - 80
        self.address = 'images/{0}.png'.format(self.name)



class ITEMS :
    def __init__(self, name):
        self.name = name
        self.address = 'images/{0}.png'.format(self.name)


# #1214 11:00
class FAIRY :
    time = 120

class KING(FAIRY):
    def __init__(self, name):
        self.name = name

    def MUNE(self, frame):
        print("%s 의 스킬발동 무적!"%(self.name))
        return

class RANGER(FAIRY):
    def __init__(self, name):
        self.name = name
    def RANGEBUFF(self, act_time):

        if act_time>0:
            print("%s 의 스킬발동 공격거리 2배!" % (self.name))
            return 2
        else:
            return 1

class ARROW(FAIRY):
    def __init__(self, name):
        self.name = name
    def SUBATTACK(self, frame):
        print("%s 의 스킬발동 대신공격!"%(self.name))
        return 1

def main():
    pygame.init()

    pygame.display.set_caption('Jumping dino')
    MAX_WIDTH = 900  # 스크린 가로 크기
    MAX_HEIGHT = 400  # 스크린 세로 크기
    # set screen, fps
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    SCREEN = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()
    GET = -500
    # 프레임을 조정하기 위한 변수를 생성
    # 화면을 초당 몇 번을 출력하는지
    imgheart = pygame.image.load('images/heart.png')

    # dino
    IMG_Dino1 = pygame.image.load('images/dino1.png')
    IMG_Dino2 = pygame.image.load('images/dino2.png')
    IMG_Dinob1 = pygame.image.load('images/dinob1.png')
    IMG_Dinob2 = pygame.image.load('images/dinob2.png')
    IMG_attack = pygame.image.load('images/attack.png')
    IMG_attack2 = pygame.image.load('images/car.png')


    DINO1 = IMG_Dino1
    DINO2 = IMG_Dino2

    Dino_height = DINO1.get_size()[1]               #80x90
    Dino_bottom = MAX_HEIGHT - Dino_height
    dino_x = 50                 # 공룡의 X축 위치     #80x60
    dino_y = Dino_bottom        # 공룡의 Y축 위치
    jump_top1 = 170              # 점프시 최고점

    leg_swap = True             # 공룡 사진 변경을 위한 변수
    IS_bottom = True            # 달리고 있는지 알려주는 변수
    IS_jump1 = False            # 공룡 위로 올라가고 있는지 알려주는 변수
    IS_jump2 = False            # 공룡 위로 올라가고 있는지 알려주는 변수

#====================================================================================class
    a0 = monster("치코리", 60, 60)
    a1 = monster("피카츄", 60, 60)
    a2 = monster("꼬부기", 60, 60)
    a3 = monster("버터플", 60, 60)
    a4 = monster("독충이", 60, 60)

    monster_list1 = [a0, a1, a2, a3, a4]
    monster_list2 = [a0, a1, a2, a3, a4]

    b0 = ITEMS("item1")
    b1 = ITEMS("ghost1")
    b2 = ITEMS("ghost2")
    b3 = ITEMS("ghost3")

    item_list = [b0, b1, b2, b3]

    monster_list = [a0, a1, a2, a3, a4]

    Small_font = pygame.font.SysFont(None, 40)


    #========================================================================================================

    MONSTER1_x = GET  # 나무 X축 위치 설정
    fire_x = GET
    fire_y = GET
    # item
    imgitem = pygame.image.load('images/heart.png')
    item_x = GET
    item_y = MAX_HEIGHT - random.randint(50,200)

#=====================================================
    attack_time = 0
    ACTIVE_ATTACK = 0
    ACTIVE_ATTACK1 = 0
    #======================================페어리 관련 변수들
    TIME_ACTIVE = 0
    GAME_frame = 0
    FRAME_count = 0
    DEOBLEJUMP = 0
    GROUNDZERO = 0
    RANGE = 200
    FAIRY_RANGERTIME = 0
    FAIRY_KINGTIME = 0
    FAIRY_ATTACK = 0
    attack_crash = 0
    GET_ITEM = 0
    ghost1_count = 0
    ghost2_count = 0
    ghost3_count = 5
    # 화면 표시
    SCORE_FRAME = 0
    SCORE_TOTAL = 0
    life = 5
    message_score = Small_font.render("Score : {0}".format(SCORE_TOTAL), True, (0, 0, 0))  # 스코어
    message_dino_y = Small_font.render("dino_y : {0}".format(Dino_height), True, (0, 0, 0))  # dino_y


    fa1 = RANGER("약범")

    while True:
        screen.fill((255, 255, 255))  # 스크린 채울 색깔 설정 RGB # 흰색 화면 출력
        SCORE_FRAME += 1
        SCORE_TOTAL = SCORE_FRAME // 10

        if life != 0:
            MOVE_SPEED_MONSTER = 4

            if MONSTER1_x < 0:
                MONSTER1_x = MAX_WIDTH
                num = random.choice(monster_list)
                IMG_MONSTER = pygame.image.load(num.address)
                MONSTER1_y = num.y

            if item_x < 0:  # 아이템 첫시작 x위치는 0
                item = random.randrange(1000)  # 아이템 랜덤
                if item < 10:  # 아이템이 10미만 일 경우
                    item_x = random.randint(1000,2000)  # 아이템 x좌표(800) 리셋
                    item_y = 400 - random.randint(50,200)
                    aitem = random.choice(item_list)
                    imgitem = pygame.image.load(aitem.address)  # 이미지아이템 로드
            item_x -= MOVE_SPEED_MONSTER
            # 라이프 표시
            tmp = 50
            for i in range(life):
                screen.blit(imgheart, (90 + tmp * i, 50))


            screen.blit(message_score, (630, 30))  # 화면상에 스코어 표시
            screen.blit(message_dino_y, (630, 120))  # 화면상에 dino_y 표시
            message_score = Small_font.render("Score: {}".format(SCORE_TOTAL), True, (0, 0, 0))  # 스코어
            message_dino_y = Small_font.render("dino_y : {}".format(dino_y), True, (0, 0, 0))  # dino_y
            screen.blit(message_dino_y, (630, 120))  # 화면상에 dino_y 표시
            message_dino_y = Small_font.render("dino_y : {}".format(dino_y), True, (0, 0, 0))  # dino_y

            for event in pygame.event.get():                    # 사용자가 무언가를 했다면(마우스, 키보드 클릭 등)
                if event.type == pygame.QUIT:  # X 버튼을 눌렀다면
                    pygame.quit()  # 게임 멈추기
                    sys.exit()
                elif event.type == pygame.KEYDOWN:  # 키보드를 클릭 했다면
                    if event.key == pygame.K_UP:                # 위 방향키
                        if IS_bottom :
                            IS_jump1 = True
                            IS_bottom = False
                            GROUNDZERO = 1
                        elif IS_bottom == False and DEOBLEJUMP==0 and event.key == pygame.K_UP:
                            IS_jump2 = True
                            jump2_y = dino_y
                            DEOBLEJUMP = 1

                    elif event.key == pygame.K_SPACE:           # 스페이스바
                        if FAIRY_ATTACK > 0:
                            ACTIVE_ATTACK1 = 1
                        else:
                            ACTIVE_ATTACK = 1

                    elif event.key == pygame.K_DOWN:            # 아래 방향키
                        if GROUNDZERO == 0:
                            DINO1 = IMG_Dinob1                         # 웅크리기 이미지
                            DINO2 = IMG_Dinob2
                            dino_bottom = MAX_HEIGHT - DINO1.get_size()[1]
                            dino_y = dino_bottom
                elif event.type == pygame.KEYUP:  # 키보드를 땔 때
                    if event.key == pygame.K_DOWN:  # 방향키 아래
                        DINO1 = IMG_Dino1  # 본래 이미로 복구
                        DINO2 = IMG_Dino2
                        dino_bottom = MAX_HEIGHT - DINO1.get_size()[1]
                        dino_y = dino_bottom

            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                if ghost1_count > 0:
                    FAIRY_RANGERTIME = 5 * GAME_frame
                FAIRY_RANGERTIME_A = FAIRY_RANGERTIME
                # ghost_adress = b1.address
                # ghost_name = b1.name
            elif keys[pygame.K_2]:
                if ghost2_count > 0:
                    FAIRY_KINGTIME += 5 * GAME_frame
                FAIRY_KINGTIME_A = FAIRY_KINGTIME
                # ghost_adress = b2.address
                # ghost_name = b2.name
            elif keys[pygame.K_3]:
                if ghost3_count > 0:
                    FAIRY_ATTACK += 5 * GAME_frame
                    FAIRY_ATTACK_A = FAIRY_ATTACK
                # ghost_adress = b3.address
                # ghost_name = b3.name
            # if keys[pygame.K_RIGHT]:
            #     player_x += 5
            # elif keys[pygame.K_LEFT]:
            #     player_x -= 5


            if FAIRY_RANGERTIME != 0:
                if FAIRY_RANGERTIME == FAIRY_RANGERTIME_A:
                    ghost1_count -= 1
                    print(ghost1_count)
                FAIRY_RANGERTIME -= 1

                myfont = pygame.font.SysFont(None, 20)
                screen.blit(myfont.render("거리2배 : %d" % (FAIRY_RANGERTIME//GAME_frame), True, (0, 0, 0)), (dino_x, dino_y-30))
                screen.blit(pygame.image.load('images/ghost1.png'), (dino_x - 20, dino_y - 50))

            RANGE = fa1.RANGEBUFF(FAIRY_RANGERTIME) * 200
            if FAIRY_KINGTIME != 0:
                if FAIRY_KINGTIME == FAIRY_KINGTIME_A:
                    ghost2_count -= 1
                    print(ghost2_count)
                FAIRY_KINGTIME -= 1
                myfont = pygame.font.SysFont(None, 20)
                screen.blit(myfont.render("무적 : %d" % (FAIRY_KINGTIME//GAME_frame), True, (0, 0, 0)), (dino_x, dino_y-60))
                screen.blit(imgitem, (item_x, item_y))
                screen.blit(pygame.image.load('images/ghost2.png'), (dino_x+10 , dino_y - 70))

            #################################################################################################
            if FAIRY_ATTACK != 0:
                if FAIRY_ATTACK == FAIRY_ATTACK_A:
                    ghost3_count -= 1
                    print(ghost3_count)
                FAIRY_ATTACK -= 1
                if ACTIVE_ATTACK1 == 1:
                    if attack_time == 0:
                        fire_x = dino_x
                        RANGE_ATTACK = dino_x + RANGE
                        fire_y = dino_y - 20
                        screen.blit(IMG_attack2, (fire_x, fire_y-150))
                        attack_time = 1
                        ACTIVE_ATTACK1 = 0
                if attack_time == 1:
                    if fire_x < RANGE_ATTACK:
                        fire_x += 15
                        screen.blit(IMG_attack2, (fire_x, fire_y-70))
                    else:
                        attack_time = 0
                        fire_x = GET

                if MONSTER1_x < fire_x + 400 :
                    # attack_crash = tree_x // MOVE_SPEED_MONSTER + 5
                    attack_time = 0
                    fire_x = GET
                    MONSTER1_x = GET
                elif (dino_x + 75 > MONSTER1_x and dino_y + 85 > MONSTER1_y) and (dino_x + 75 > MONSTER1_x and dino_y < MONSTER1_y + 55) and (dino_x < MONSTER1_x + 55 and dino_y + 85 > MONSTER1_y) and (dino_x < MONSTER1_x and dino_y < MONSTER1_y + 55):
                    if FAIRY_KINGTIME == 0:
                        life -= 1
                    MONSTER1_x = GET
                    # attack_crash = tree_x//MOVE_SPEED_MONSTER+5                      #해당 프레임 동안은 충돌한 녀석 안보이게
                else:
                    screen.blit(IMG_MONSTER, (MONSTER1_x, MONSTER1_y))

                if (dino_x + 600 > item_x) and (dino_x + 600 > item_x) and (dino_x < item_x + 600) and (dino_x < item_x):

                    item_x = -100  # 아이템 먹었을 경우 item_x를 좌측으로 없앰

                else:
                    screen.blit(imgitem, (item_x, item_y))

    ########################################################################################

                myfont = pygame.font.SysFont(None, 20)
                screen.blit(myfont.render("무적 : %d" % (FAIRY_ATTACK//GAME_frame), True, (0, 0, 0)), (dino_x, dino_y-60))
                screen.blit(imgitem, (item_x, item_y))
                screen.blit(pygame.image.load('images/ghost3.png'), (dino_x+40 , dino_y - 50))




            if ACTIVE_ATTACK == 1:
                if attack_time == 0 :
                    fire_x = dino_x
                    RANGE_ATTACK = dino_x + RANGE
                    fire_y = dino_y+20
                    screen.blit(IMG_attack, (fire_x, fire_y))
                    attack_time = 1
                    ACTIVE_ATTACK = 0
            if attack_time == 1:
                if fire_x < RANGE_ATTACK:
                    fire_x += 15
                    screen.blit(IMG_attack, (fire_x, fire_y))
                else:
                    attack_time = 0
                    fire_x = GET




            MONSTER1_x -= MOVE_SPEED_MONSTER  # 나무가 왼쪽으로 10만큼 이동한다.
            if MONSTER1_x <= 0:  # 나무가 창 왼쪽으로 나갔다면
                MONSTER1_x = MAX_WIDTH  # 창 오른쪽으로 보낸다.


            # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


            if MONSTER1_x < fire_x + 45 and MONSTER1_y < fire_y + 45 and MONSTER1_y + 55 > fire_y:
                # attack_crash = tree_x // MOVE_SPEED_MONSTER + 5
                attack_time = 0
                fire_x = GET
                MONSTER1_x = GET
            elif (dino_x+75 > MONSTER1_x and dino_y+85 > MONSTER1_y) and (dino_x+75 > MONSTER1_x and dino_y < MONSTER1_y+55) and (dino_x < MONSTER1_x+55 and dino_y+85 > MONSTER1_y) and (dino_x < MONSTER1_x and dino_y < MONSTER1_y+55):
                if FAIRY_KINGTIME == 0 :
                    life -= 1
                MONSTER1_x = GET
                # attack_crash = tree_x//MOVE_SPEED_MONSTER+5                      #해당 프레임 동안은 충돌한 녀석 안보이게
            else:
                screen.blit(IMG_MONSTER, (MONSTER1_x, MONSTER1_y))


            if (dino_x + 75 > item_x and dino_y + 85 > item_y) and (
                    dino_x + 75 > item_x and dino_y < item_y + 25) and \
                    (dino_x < item_x + 25 and dino_y + 85 > item_y) and (dino_x < item_x and dino_y < item_y + 25):

                item_x = -100  # 아이템 먹었을 경우 item_x를 좌측으로 없앰
                if aitem.name == "item1":  # 아이템 먹었을 때 카운트
                    life += 1
                    print(life)
                if aitem.name == "ghost1":
                    ghost1_count += 1
                    print(ghost1_count)
                if aitem.name == "ghost2":
                    ghost2_count += 1
                    print(ghost2_count)
                if aitem.name == "ghost3":
                    ghost3_count += 1
                    print(ghost3_count)
            else:
                screen.blit(imgitem, (item_x, item_y))







            if IS_jump1:                                    # 올라가고 있다면
                dino_y -= 5                                # 공룡이 위쪽으로 10만큼 올라간다
            elif IS_jump2:                                    # 올라가고 있다면
                dino_y -= 5                                # 공룡이 위쪽으로 10만큼 올라간다
            elif not IS_jump1 and not IS_bottom:            # 내려가고 있다면
                dino_y += 5                                # 공룡이 아래쪽으로 10만큼 내려간다

            # 공룡 점프 및 지상 인식
            if IS_jump1 and dino_y <= jump_top1:             # 공룡이 최대 높이 이하에 위치한다면
                IS_jump1 = False                            # 내려가는 상태 변수가 참이 된다

            elif IS_jump2 and dino_y <= jump2_y - 120 :             # 공룡이 최대 높이 이하에 위치한다면
                IS_jump2 = False         # 내려가는 상태 변수가 참이 된다
            elif not IS_bottom and dino_y >= Dino_bottom:     # 공룡이 최저 높이 이상에 위치한다면
                IS_bottom = True                            # 달리고 있는 상태 변수가 참이 된다.
                dino_y = Dino_bottom                        # 공룡의 y축 중심은 최저 높이로 변경 된다.
                DEOBLEJUMP = 0
                GROUNDZERO = 0

        ########################################################################
            # fairy
            # if TIME_ACTIVE > 0:  # 유지시간
            #     if FRAME_count == 0:  # 지금 현재 게임 프레임을 받아서 해당프레임이 진행되면 유지시간을 1씩 감소시키는 방식
            #         TIME_ACTIVE -= 1
            #         FRAME_count = GAME_frame
            #     else:
            #         FRAME_count -= 1
            #달리기 모션
            if leg_swap:  # 2번 사진이라면
                screen.blit(DINO1, (dino_x, dino_y))  # 1번 사진으로 바꾼다
                leg_swap = False  # 1번 사진이 나오고 있는 상태임을 표시한다
            else:
                screen.blit(DINO2, (dino_x, dino_y))  # 2번 사진으로 바꾼다
                leg_swap = True  # 1번 사진이 나오고 있는 상태임을 표시한다

        else :
            #gameover
            myfont = pygame.font.SysFont(None, 80)
            message1 = myfont.render("score : %d" % SCORE_TOTAL, True, (0, 0, 0))
            screen.blit(message1, (300, 200))
            time.sleep(1)

        SPEED = SCORE_TOTAL // 100
        GAME_frame = 50 + SPEED


        # update
        pygame.display.update()
        fps.tick(GAME_frame)                                   # 화면 업데이트가 초당 30번 실행


if __name__ == '__main__':
    main()