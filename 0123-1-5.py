import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로

dummy_data = []
for i in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()

    
    # data= parsed_data[]
    dummy_data.append(parsed_data['name'])

print(dummy_data)


    

# API 요청

# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
# print(response)

# # # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])
