data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'


arr=''
uppstr = arr.upper()
for i in data_1:
    if i.isupper() or i==' ':
        arr= arr + i

    
        

print(arr,end='')
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.




print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr2 = []

# 아래에 코드를 작성하시오.
if data_2.find('내'):
    a = data_2.find('내')
    arr2.append(a)
if data_2.find('힘'):
    b = data_2.find('힘')
    arr2.append(b)
if data_2.find('들'):
    c= data_2.find('들')
    arr2.append(c)
if data_2.find('다'):
    d = data_2.find('다')
    arr2.append(d)
    

print(arr2)

arr2.sort()
print(arr2)

for idx in arr2:
    print(data_2[idx],end='')