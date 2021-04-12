# print('hello python')
# 변수 : 데이터를 저장하기 위한 공간
# 변수명 : 저장괸 데이터를 접근하기 위한 이름
# = : 대입연산자
# a = 10
# print(a)


# 사칙연사 : +,-,*,/,%,//
# a = 50
# b = 3
#
# print('a+b=', a+b)
# print('a-b=', a-b)
# print('a*b=', a*b)
# print('a/b=', round(a/b))
# print('a/b=%.2f' %(a/b))
# print('a//b=', a//b)
# print('a%b=', a%b)

# a = 10000
# print('시:', a // 3600)
# print('분:', (a % 3600) // 60)
# print('초:', (a % 3600) % 60)

# 포맷 문자열
# 30 + 2-0 = 50
a = 30
b = 20

print(a, '+', b, '=', a + b)
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %.2f' % (a, b, a / b))
print('%d %% %d = %d' % (a, b, a % b))
