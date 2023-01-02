def arbeitnum(money):           #인자는 호출때 사용한 인자랑 이름달라도 자리만 맞으면 작동합니다            # 도현
    if(money>=1500000):
        arbeit1=money/1500000   #고용가능한 알바수 구하기,메인의 진짜 arbeit과 혼동 피하기 위해 1 붙임
        while(1):
            print("%d명 고용가능"%arbeit1)
            select=(int(input("고용할 알바수 : ")))
            if(select<=arbeit1):
                return select       #고용가능수와 선택수가 같을경우 그만큼 리턴
            else:
                print("그만큼 고용하기엔 돈이 부족합니다")
    else:
        print("돈부족, 고용불가")
n = arbeitnum(5000000)
print(n)
def customer(arbeit): # 알바몬 받아오기                                            # 보라

    customer_num= random.randint(1,100) # 첫주에는 1~100명의 랜덤손님방문
    if arbeit != 0: # 알바몬이 0이 아닐때
        print (f'오늘은 총 {customer_num+arbeit*100}명의 손님이 방문합니다.') # return으로쓰고 print로 찍어 확인했었는데 함수안에 바로 print하면된다.
        return customer_num+arbeit*100
    else:
        print (f'오늘은 총 {customer_num }명의 손님이 방문합니다.')
        return customer_num

def day(arbeit):
    day_menu = []  # 하루방문 손님 리스트
    day_money = []  # 손님 매출 총합
    day_total = [] # 하루 매출 총합
    day_sum = 0 # 하루 매출 총합
    menu_list= ['후라이드치킨','양념치킨','간장치킨','후라이드순살','양념치킨순살','간장치킨순살','마른오징어','과일안주','포테이토후라이','쥐포','모듬튀김','테라','카스','오비라거','클라우드','콜라','사이다','쿨피스','오뎅탕','떡볶이']
    menu_price =[18000,19000,19000,17000,18000,18000,8000,15000,5000,7000,12000,5000,4000,4500,4500,2500,2000,1000,7000,7000]

    for i in range(customer(arbeit)): # 1~5개 메뉴 선택
        for j in range(random.randrange(5)):
            menu_choice = random.randrange(20)
            day_money.append(menu_price[menu_choice])
            day_menu.append(menu_list[menu_choice]) # 손님이 선택한 메뉴 저장
        print(f'주문하신 음식은 {day_menu}입니다.')
        print(f'{sum(day_money)}원 입니다')
        day_total.append(sum(day_money))

        day_menu.clear()
        day_money.clear()  # 다음손님 합을 초기화
        day_sum = sum(day_total)
    print(f'총합:{day_sum},손님은:{day_total}')
    return day_sum , day_total

day(1)
def claim(menu_price_claim):                                            # 4 성경누나

    claim_price=[]
    claim_price_sum = 0
    for i in range(len(menu_price_claim)):

        rand = random.randrange(100)

        if rand < 15:
            claim_price.append(menu_price_claim[i]*2)
            claim_price_sum = sum(claim_price)
    print(f'환불 금액은 {claim_price_sum}원 입니다.')

    return claim_price_sum

menu_price_claim = [18000, 30000, 4000, 5000, 6000, 40000, 50000]

claim(menu_price_claim)
def finish(total_money):                                                 # 6 성경누나

    if total_money >= 500000000:
        print("프랜차이즈화~")

    else :
        print("GAME OVER")

finish(500000000)
arbeit = 0
total_money = 0

for i in range(4):                                      # 4주 반복문
    if i != 0:
        arbeit += arbeitnum(total_money)               # 아르바이트 고용 함수
        total_money -= arbeit*1500000

    for j in range(7):                                  # 7일 반복문
        print(f'{i+1}주차 {j+1}일/////')
        day_total_money, claim_list = day(arbeit)       # 1일 매출 함수

        total_money += day_total_money                  # 1일 총매출액을 total_money에 더함
        print(f'하루 매출액 : {day_total_money}')

        # print(claim_list)
        claim_money = claim(claim_list)                 # 1일 클레임 함수
        print(f'하루 클레임 비용 : {claim_money}')
        total_money -= claim_money                      # total_money에서 클레임 비용 빼기
        print(f'총 매출액 : {total_money}')

finish(total_money)                                      # 매출액 비교 함수

