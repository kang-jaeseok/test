# #조건문
# a = -10
# if a > 0:
#     print('양수')
#     print(a)
# else:
#     print('음수')
#     print(a)
#
# print('프로그램 종료')

# 실습) 회원등급 출력
# a가 90보다 크면 good 아니면 try출력

# a = int(input('입력 :'))
# if a > 90:
#     print("good")
# else:
#     print("try")

# #  실습) 비밀번호 체크
# # 비밀번호가 일치하면 '문이 열립니다'
# # 일치하지 않으면 '다시 확인 하세요'
#
# pw = 1234 #기존 등록된 비밀번호
# a = int(input('입력 : '))
# if pw == a:
#     print('문이열립니다.')
# else:
#     print('다시확인하세요')

# 어떤수가 짝수이면 '짝수' 홀수이면 '홀수' 출력

# a = int(input())
# if a == 0:
#     print('짝수도 홀수도 아닙니다.')
# elif a % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# 실습) ~ 90점이상은 A 89~80 B, 79~70 C, 69~60 D, 59~ F

# a = int(input('입력 :'))
#
# if a >= 90:
#     print('A')
# elif a >= 80:  # if a <= 89 and a >= 80
#     print('B')
# elif a >= 70:
#     print('C')
# elif a >= 60:
#     print('D')
# elif a <= 59:
#     print('F')

# 실습) 몸무게와 키를 입력 받아서 비만 여부 출력

# data = input('이름 키 몸무게 : ')
#
# name = data.split()[0]
# height = float(data.split()[1])
# weight = float(data.split()[2])
#
# normal = (height-100) * 0.9

# print(normal, normal * 0.95, normal * 1.05)

# if normal * 0.95 <= weight and normal * 1.05 >= weight:
#     print('적정')
# elif normal * 0.95 > weight:
#     print('미만')
# elif normal * 1.05 < weight:
#     print('초과')

# if weight < normal * 0.95:
#     print('미만')
# elif weight <= normal * 1.05:
#     print('정상')
# else:
#     print('비만')


# 실습) 계산기
# 두수와 연산기호 입력

# data = input('두수와 연산기호 : ').split()
#
# a = int(data[0])
# b = int(data[2])
# c = data[1]
# # a = int(data.split()[0])
# # b = int(data.split()[2])
# # c = data.split()[1]
#
# if c == '+':
#     print('%d + %d = %d' % (a, b, a + b))
# elif c == '-':
#     print('%d - %d = %d' % (a, b, a - b))
# elif c == '*':
#     print('%d * %d = %d' % (a, b, a * b))
# else:
#     print('%d / %d = %.2f' % (a, b, a / b))

# data = input('계산식은?').split()
# print(data)
# a = int(data[0])
# b = int(data[2])
# sign = data[1]
# if sign == '+':
#     print('%d + %d = %d' % (a, b, a+b))
# elif sign == '-':
#     print('%d - %d = %d' % (a, b, a-b))
# elif sign == '*':
#     print('%d * %d = %d' % (a, b, a*b))
# elif sign == '/':
#     print('%d / %d = %.2f' % (a, b, a/b))
# else:
#     print('잘못된 기호')

#
import os

#
# data = input('계산식은?')
# cal = eval(data) # 문자를 식으로 해석 # 의도적인 공격에 노출되기 쉬움 쓰지 말것
# print(cal)

# 실습) 두 수를 입력을 받아 큰수를 화면에 출력

# data = input("두수 입력 : ").split()
# a = int(data[0])
# b = int(data[1])
#
# if a > b:
#     print(a)
# elif b > a:
#     print(b)
# else:
#     print("같음")


# amount= int(input('현재 금액:'))
# pay = int(input('구입 금액:'))
#
# if amount > pay:
#     print('거스름돈 ', amount - pay, '원', sep='')
# elif pay > amount:
#     print('돈이 ', pay - amount, '원 부족', sep='')
# else:
#     print('계산 완료')
#

# 논리연산자
# a = 10;b = 20
# print(a > 0 and b > 0)
# print(a > 0 and b < 0)
# print(a > 0 or b < 0)
# print(not (a > 0))

# a = -10; b = 20
# if a == 0 or b == 0:
#     print('0이 아닌수를 입력하세요')
# elif a > 0 and b > 0:
#     print('둘다 양수')
# elif a > 0 or b > 0:
#     print('둘중하나는음수입니다.')
# else:
#     print('둘다 음수')

menu = int(input('1.자장면, 2.짬뽕, 3.설렁탕, 4.비빔밥, 5.피자, 6.스파게티 메뉴를 선택하세요 : '))

# # if menu == 1 or menu == 2:
# if menu in [1, 2]:
#     print('중식')
# elif menu == 3 or menu == 4:
#     print('한식')
# elif menu == 5 or menu == 6:
#     print('양식')
# else:
#     print('잘못된 입력')
# if menu >= 1 and menu <= 2:
#     print('중식')
# elif menu >= 3 and menu <= 4:
#     print('한식')
# elif menu >= 5 and menu <= 6:
#     print('양식')
# else:
#     print('잘못된 입력')
# menudictionary = {1: ['자장면', 5000, '중식'], 2: ['짬뽕', 6000, '중식'], 3: ['설렁탕', 7000, '한식'],
#                   4: ['비빔밥', 8000, '한식'], 5: ['피자', 9000, '양식'], 6: ['스파게티', 10000, '양식']}
#
# menukey = menudictionary.keys()
#
# if menu not in menukey:
#     print('잘못된입력')
# else:
#     print(menudictionary[menu][0] + ' ', menudictionary[menu][1], '원 ', menudictionary[menu][2], sep='')
#

# if menu == list(menudictionary.keys())[0] or menu == list(menudictionary.keys())[1]:
#     print(menudictionary[menu][1])
# elif menu == list(menudictionary.keys())[2] or menu == list(menudictionary.keys())[3]:
#     print(menudictionary[menu][1])
# elif menu == list(menudictionary.keys())[4] or menu == list(menudictionary.keys())[5]:
#     print(menudictionary[menu][1])
# else:
#     print('잘못된 입력')


