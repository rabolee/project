# name = [] # 이름 입력받기
# Attendance = [] # 받은이름 저장
#
# new = int(input("총 학생수를 입력:")) # 숫자로 받기
#
# for i in range(new): # 입력받은 수만큼 값 받기
#     name = str(input("이름을 입력하세요")) # 문자로 받기
#     Attendance.append(name) # 새 출석부에 이름 추가저장하기
#     Attendance.sort() # 이름 오름차순으로 정렬
# print("   출  석  부  ")
# print("===============")
#
# for i in range(len(Attendance)): # 저장된 요소만큼 출력
#     print("",[i+1],"",Attendance[i]) # 번호와 이름 출력

num_dict = dict()
num_list = []
login_list = []

idx = 0

idx += 1
num_dict[idx] ='고연재'

idx += 1
num_dict[idx] ='김기태'

idx += 1
num_dict[idx] ='강민영'

print(num_dict)
print(num_dict.keys())
print(num_dict.values())
num_dict = num_list
num_list.sort()
print(type(num_list))


