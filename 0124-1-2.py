# 주어진 리스트의 최댓값 최솟값 구하기기
def find_min_max(list):
    cur_max = 0  # 입력되는 값 중 제일 작은 값값
    cur_min = 100
    for i in list:
        # print(i)
        if cur_max < i :
            cur_max = i
            # print(i, cur_max,)
    for j in list:
        if cur_min > j:
            cur_min = j
            # print(j, cur_min)
            
        
    
    return (cur_min, cur_max)



result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
print(type(result))