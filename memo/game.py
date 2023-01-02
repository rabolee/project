import random
import keyboard
import time
import pygame

# 1. 게임초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [500, 500]
screen = pygame.display.set_mode(size)

title = "Tiger's Den Game"
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
color = (0,0,0) # RGB값 검정
ss = pygame.image.load("C:/temp/tiger.png").convert_alpha() #이미지 삽입
ss = pygame.transform.scale(ss,(100,100))  # 이미지 크기변경
ss_x = round(size[0]/2) # 가운데 설정 반올림함수
ss_y = round(size[1]-5) # 가운데 설정 반올림함수

# 4. 메인 이벤트
BR = 0
while BR==0:

    # 4-1. fps 설정
    clock.tick(60) # 1초에 화면 60번

    # 4-2. 각종 입력 감지
    for event in pygame.event.get(): # 여러입력을 할수있기때문에 for문
        if event.type == pygame.QUIT: # 게임창을 닫았을때 라면
            BR = 1 # while문 값 변경으로 게임 종료
    # 4-3. 입력. 시간에 따른 변화

    # 4-4.  그리기
    screen.fill(color) # 바탕화면
    screen.blit(ss,(0,0))

    # 4-5. 업데이트
    pygame.display.flip() # 화면 업데이트

# 5. 게임 종료
pygame.quit()

#화면 크기 설정
# screen_width = 500 # 가로 크기
# screen_height = 500 # 세로 크기
# screen = pygame.display.set_mode((screen_width, screen_height))
#
# # 화면 타이틀 설정
# pygame.display.set_caption("tiger's den Game")
# # 이벤트 루프
# running = True # 게임 진행 여부에 대한 변수 True : 게임 진행 중
# while running:
#     for event in pygame.event.get(): # 이벤트의 발생 여부에 따른 반복문
#         if event.type == pygame.QUIT: # 창을 닫는 이벤트 발생했는가?
#             running = False
#
# # 이벤트 루프
# running = True # 게임 진행 여부에 대한 변수 True : 게임 진행 중
# while running:
#     for event in pygame.event.get(): # 이벤트의 발생 여부에 따른 반복문
#         if event.type == pygame.QUIT: # 창을 닫는 이벤트 발생했는가
#             running = False
#
#     screen.blit(background,(0,0)) # 배경에 이미지 그려주고 위치 지정
#     pygame.display.update()
#
# # pygame 종료
# pygame.quit()