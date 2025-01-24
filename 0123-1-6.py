import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로

dummy_data = []
for i in range(1,11):
    dummy_dict = {}

    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    if -80 < float(parsed_data['address']['geo']['lat']) <80 and  -80 < float(parsed_data['address']['geo']['lng']) <80: 
        dummy_dict['company'] = parsed_data['company']['name']
    
        dummy_dict['lat'] = parsed_data['address']['geo']['lat']
        dummy_dict['lng'] = parsed_data['address']['geo']['lng']
        dummy_dict['name'] = parsed_data['name']
    
    
        dummy_data.append(dummy_dict)
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
