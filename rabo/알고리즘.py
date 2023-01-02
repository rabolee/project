import random

# 버블,선택,삽입 정렬 구현하기

numlist = []
for i in range(10):

    num = random.randint(1,10)
    while num in numlist: # 중복방지
        num = random.randint(1,10)
    numlist.append(num)

# print(numlist)

# 버블정렬, 선택정렬
# for i in range(9):
#     i += 1
#     for j in range(9):
#         if numlist[i] < numlist[j]:
#             numlist[i],numlist[j] = numlist[j],numlist[i]
#     print(numlist)
#
# 삽입정렬
# for i in range(9):
#     i += 1
#     while True:
#         for i in range(9):
#             for j in range(9):
#                 numlist[i], numlist[j] = numlist[j], numlist[i]
#                 if numlist[i] < numlist[j]:
#                     print(numlist)
#
#                 if numlist[0] > numlist[1]:
#                     break
#
num1 = [1,2,5,7]
num2 = [3,4,6,7,8]
num3 =[]

for i in range(len(num1)):
    if num1[i] < num2[0]:
        num3.append(num1[i])
    if num1[0] < num2[i]:
        num3.append(num2[i])
        # for j in range(len(num2)):
        #     if num1[i] < num2[j]:
        #         num3.append(num2[j])
# print(num3)

# 삽입정렬
numlist = []
for i in range(10):
    num = random.randint(1,10)
    while num in numlist: # 중복방지
        num = random.randint(1,10)
    numlist.append(num)
print(numlist)


# 퀵 정렬
# def quick(numlist,start,end):
#     if start>=end:
#         return
#     pivot = start
#     left = start +1
#     right = end
#
#     while left <= right: # 피벗보다 큰 데이터를 찾을때까지 반복
#         while left <= end and numlist[left] <= numlist[pivot]:
#             left += 1 # 왼쪽 파티션에서 피벗보다 큰 데이터 찾기전까지 +1
#
#         while right > start and numlist[right] >= numlist[pivot]:
#             right -= 1  # 오른쪽 파티션에서 피벗보다 큰 데이터 찾기전까지 -1
#
#         if left>right: # 데이터와 피벗을 교체
#             numlist[right],numlist[pivot] = numlist[pivot],numlist[right]
#
#         else: # 엇갈리지 않는경우 작은데이터와 큰 데이터 교체
#             numlist[left],numlist[right] = numlist[right],numlist[left]
#
#     quick(numlist, start, right-1)
#     quick(numlist, right+1, end)
#
# quick(numlist,0,len(numlist)-1)
# print(numlist)


# 병렬정렬
def merge_sort(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하
    if n <= 1:
        return
    # 그룹을 나누어 각각 병합 정렬 호출
    mid = n//2          # 중간을 기준으로 두 그룹으로 나눔
    left = a[:mid]
    right = a[mid:]
    merge_sort(left)
    merge_sort(right)
    # 두 그룹을 하나로 병합
    l = 0
    r = 0
    ia = 0
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            a[ia] = left[l]
            l += 1
            ia += 1
        else:
            a[ia] = right[r]
            r += 1
            ia += 1
    # 아직 남아 있는 자료들을 결과에 추가
    while l < len(left):
        a[ia] = left[l]
        l += 1
        ia += 1
    # 아직 남아 있는 자료들을 결과에 추가
    while r < len(right):
        a[ia] = right[r]
        r += 1
        ia += 1

merge_sort(numlist)
print(numlist)




