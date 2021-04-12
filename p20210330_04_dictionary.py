# 딕셔너리
# 순서가 없다. [1:3] 이런거 안됨

# data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# print(data['b'])
# print(data['d'])

#
# data = {'홍길동': 20, '이순신': 45}
# print(data['홍길동'], '살', sep='')
#
# data = {'홍길동': [20, 165.5], '이순신': 45}
# print(data['홍길동'])
# print(data['홍길동'][1])

# data = {'홍길동': {'나이': 20, '키': 165.5}, '이순신': {'나이': 45, '키': 170}}
# print(data['홍길동']['키'])
# print(data['이순신']['키'])
#
# data = {1: ['홍길동', 20, 165.5], 2: ['이순신', 45, 170.5]}
#
# print(data[2][0]) # [2]는 키, [0]은 index

# 딕셔너리 데이터 추가 리스트와 달리 별도의 METHOD 사용안함
# data = {}
# data['홍길동'] = 20
# data['이순신'] = [45, 170.8]
# print(data['이순신'][1])

##실습) 컴퓨터 언어를 입력받아 딕셔너리에 저장
# {'backend': 'java', 'frontend': 'html5'}

# lang = {}
# lang['backend'] = input('backend 언어 입력:')
# print(lang['backend'])
# lang['frontend'] = input('frontend 언어 입력:')
# print(lang['frontend'])
# print(lang)


# data = {'홍길동': {'나이': 20, '키': 165.5}, '이순신': {'나이': 45, '키': 170}}


# data = input('입력 : ')
# lang = {}
# lang['backend'] = data.split()[0]
# lang['frontend'] = data.split()[1]
#
# print(lang['backend'] + ' ' + lang['frontend'])
#
# data = {1: '고질라', 2: '귀멸의칼날', 3: '더박스'}
# print(list(data.keys())[0])  # 키를 list형식으로 출력
# print(list(data.values())[0])  # list 사용하고 나선 index가능


#set : 중복 허용x, 순서x
asia = {'한국', '중국', '일본'}
asia.add('베트남')
asia.add('중국')
asia.remove('일본')
asia.update({'한국', '홍콩', '태국'})
print(asia)