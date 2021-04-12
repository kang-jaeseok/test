# 연습문제
# 별찍기

# for x in range(1, 7):
#     print('*' * x)

# for x in range(7, 1, -1):
#     print('*' * x)

for x in range(1, 7):
    print(' ' * (6 - x), end = '')
    print('*' * x)

for x in range(1, 7):
    print(' ' * (6 - x), end = '')
    print('*' * (2 * x - 1))