

f = open("c:/doit/새파일.txt",'w')  # 여기서 썼는데 메모장에 자동 저장이 된다 신기방기
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()


f = open("C:/doit/새파일.txt",'r') # 메모장에 있는 한줄을 불러온다.
line = f.readline()
print(line)
f.close()

f = open("C:/doit/새파일.txt",'r') # 메모장에 있는 여러줄을 불러온다.
line = f.readlines()
print(line)
f.close()

f = open("C:/doit/새파일.txt",'r') # 메모장에 저장된 파일 그대로 불러온다
#한줄씩 쓰고 싶으면 split으로 찾아서 사용
data = f.read()
print(data)
f.close()

