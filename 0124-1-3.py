N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
for i in range(9):
    arr_1.append(data_1[i])
print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'

arr_2 = data_2.split(' ')
# print(arr_2) 타입 확인용용
for i in arr_2:
    i = int(i)
    if i % 2 != 0:

        print(i)