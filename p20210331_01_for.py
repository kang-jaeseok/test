# 반복문: for
# for x in [1, 20, 30, 7, 9]:
#     print('python', x)

# data = ['이선희', '최불암', 'BTS']
# print(data[0])
# print(data[1])
# print(data[2])
#
# for x in data:
#     print(x)

# for x in [0, 1, 2]:
#     print(data[x])

# 실습) 0~9 출력
# for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     print(x)

# 정수를 생성
# range(start, stop, step)

# print(list(range(10, 50, 2)))

# for x in range(0, 10, 2):
#     print(x)

# 합계를 구하기

# s = 0  # 합계를 저장할 변수
#
# for x in range(1, 11, 1):
#     s += x  # s = s + x
#
# print(s)

# 실습) 사용자에게 마지막 숫자를 입력 받아 1부터 그 숫자까지 덧셈, 합계 출력

# data = int(input('입력 : '))
# s = 0
# for x in range(1, data+1, 1):
#     s += x
#
# print(s)

# 실습) 1부터 100까지 합이 2000이 넘을때의 수를 출력

# s = 0
# for x in range(1, 101, 1):
#     s += x
#     if s > 2000:
#         break # 반복문을 종료할때
# print('x =', x, 's =',s)

# 실습) 바보라는 글자가 발견되면 강퇴
# for ~ else
# data = ['안녕', '반가워', '방가', '바보', '오늘만나']
# bad = ['바보', '멍청이']
# for x in data:
#     if x in bad:
#         print('강퇴')
#         break
# else: # for문이 정상수행했다면(break를 실행하지 않았다면) 수행.
#     print("바른말사용")

# continue

# data = [3, 4, 6, 8, 7, 10, ]
# for x in data:
#     if x % 2 == 1:
#         continue
#     print(x)

# data = input('점수는? :').split(',')
# data = map(int, data)
#
#
# #data = [65, 45, 95, 55, 70]
# #data = [68, 78, 96, 86, 72]
#
# for x in data:
#     if x <= 60:
#         print("불합격")
#         break
# else:
#     print("합격")
#
#
# data = input('점수는? :').split()
# data = map(int, data)
#
# s = 0
#
# for x in data:
#     s += x
#     if s >= 300:
#         print('합격')
#         break
# else:
#     print('불합격')

