# 반복문 : while
# 조걸일 참일동안 실행
# while True:
#     print('python')

# 1부터 10까지 출력
# a = 0
# while a < 10:
#     a += 1
#     # if a > 9:   break
#     print(a)

# 실습) 1~10합을 출력

# s = 0  # 합계를 누적할 변수
# a = 0  # 증가하는 변수
#
# while True:
#     a += 1
#     s += a
#     if a > 9:
#         print(s)
#         break

#a가 증가하면서 합계를 구하고 그 합계가 2000이 넘으면 종료한다.

# s = 0
# a = 0
#
# while s < 2000:
#     a += 1
#     s += a
#
# print('a =', a, 's =', s)

# 사용자가 입력한 수를 누적 하다가 만약 0을 입력하면 반복문 종료 누적합계를 출력

# s = 0
# data = 1
#
# while data != 0:
#     data = int(input('더할값은?'))
#     s += data
#
# print(s)
#
# s = 0
#
# while True:
#     a = int(input('더할값은?'))
#     s += a
#     if a == 0:  break
#
# print(s)
