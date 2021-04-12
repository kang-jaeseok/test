# 사용자에게 입력받기
# a = input('이름은?')
# print('입력한 값은', a)

# 실습) 나이를 입력받아 화면에 출력

# age = input('나이는?')
# print('당신의 나이는 ' + age + '입니다')
# print('당신의 나이는 ',  age, '입니다', sep='', end='')
# print('당신의 나이는 ',  age, '입니다')
# end : print 함수에 끝 처리
# sep : 변수의 띄워쓰기 (, 이용시)
# input 함수 사용시 모두 문자 취급

# 실습) 날씨를 입력받아 오늘의 날씨 출력
# 예) 오늘의 날씨는 맑음

# help(input)
# txt = '오늘의 날씨는'
# txt = txt + ' ' + input('날씨는?')
# print(txt)

# 사용자가 입력한 값에 100을 더해서 출력

# a = input('숫자는?')
# # a = int(a) # 정수로 변환해서 반환해주는 함수
# a = float(a)  # 실수로 변환해서 반환해주는 함수
# print(a + 100)

# # 실습) 두수를 입력받아 사칙연산 프로그램
# print('두수를 입력해주세요')
# a = input('a = ')
# b = input('b = ')
# a = float(a)
# b = float(b)
#
# print('%.2f + %.2f = %.2f' % (a, b, a + b))
# print('%.2f - %.2f = %.2f' % (a, b, a - b))
# print('%.2f * %.2f = %.2f' % (a, b, a * b))
# print('%.2f / %.2f = %.2f' % (a, b, a / b))
# print('%.2f %% %.2f = %.2f' % (a, b, a % b))
#
# print(a, '+', b, '=', a + b)
# print(a, '-', b, '=', a - b)
# print(a, '*', b, '=', a * b)
# print(a, '/', b, '=', a / b)
# print(a, '%%', b, '=', a % b)

# a = int(input('첫번째수?'))
# b = int(input('두번째수?'))
#
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %.2f' % (a, b, a / b))
# print('%d %% %d = %d' % (a, b, a % b))


# 2)
# # splite() 사용
# data = input('두수는?')
# a = int(data.split()[0])
# b = int(data.split()[1])

# # map() 사용
# data = input('두수는?').split() #두수를 분리
# a,b = map(int, data) #data의 각값을 int 함수를 적용한후 a,b에 대입
# print(a, b)

# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %.2f' % (a, b, a / b))
# print('%d %% %d = %d' % (a, b, a % b))



# 실습) 반지름을 사용자로 부터 입력 받아 원의 넓이를 구해 봅시다.(원주율 : 3.14)
# r**2 == r*r 제곱
# r=float(input('반지름의 길이는?'))
# print('원의 넓이는 ', r**2*3.14, '입니다', sep='')


