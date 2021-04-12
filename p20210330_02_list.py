# # 리스트 : 여러개의 데이터를 하나의 변수에 저장, 연속적인 메모리의 할당
# data = [10, 20, 30, 40, 50]
# print(data[2])
# print(data[1:3])  # print(data[1:-2])
# print(data[2:])
# print(data[:-1])
# data[1] = 200
# print(data)
#
# # data[5] = 200 # index 초과
# data.append(200) # 마지막 추가
# data.insert(3, 300) # index 지정
#
# del data[1]
# print(data)
#
# data.remove(50)
# print(data)
#
# del data[data.index(40)]
# print(data)

data = ['홍길동', 20, 165.8]
print(data[0], data[1], data[2])
data = [['홍길동', 20, 165.8], ['이순신', 40, 170.5]]
print(data[1][0])


