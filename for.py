# for 반복문
a = ['cat', 'cow', 'tiger']

for animal in a :
    # print(animal)             # 개행 띄우기
    print(animal, end='  ')    # end 설정한 만큼 띄어쓰기
else :
    # pass
    print('')   # for문이 끝난 시점에 한번만 개행 띄우기

print('!!!!!!!!!!')

# 복합 자료형을 사용하는 for문
l = [('둘리', 10), ('마이콜', 20), ('도우넛', 30)]

for data in l :
    print('이름:%s, 나이:%d' % data)
else :
    print('')

for name, age in l :
    print('이름:{0}, 나이:{1}'.format(name, age))

l = [{'name': '둘리', 'age': 10},
     {'name': '또치', 'age': 20},
     {'name': '도우넛', 'age': 30}]

for data in l :
    print('이름:%(name)s, 나이:%(age)d' % data)

# 1~10 합 구하기
s = 0
for i in range(1, 11) :
    s += i

print(s)

# break
for i in range(10) :
    if i > 5 :
        break
    print(i, end=' ')
else :                  # for ~ else 에서 else는 for문 정상 종료시에만 실행
    print('')

print('!!!break!!!')

# continue
for i in range(10) :
    if i <= 5 :
        continue
    print(i, end=' ')
else :
    print('')

print('!!!continue!!!')

# 과제

print('1. 구구단')
# 구구단
for i in range(1, 10) :
    for j in range(1, 10) :
        print('{0} X {1} = {2}'.format(j, i, i*j), end='\t')
        # print(format(j, "d") + ' X ' + format(i, "d") + ' = ' + format((i*j), "d"), end='\t')
    else :
        print('')
else :
    pass

print('2. 삼각형')
# 삼각형
for i in range(0, 10) :
    for j in range(0, i+1) :
        print('*', end='')
    else :
        print('')

print('3. 역삼각형')
# 역삼각형
for i in range(10, 0, -1) :
    for j in range(0, i) :
        print('*', end='')
    else :
        print('')


print('4. 삼각형 별해')
# 삼각형 별해
# 중첩 for 문 사용하지 않고 작성
for i in range(0, 10) :
    print('*' * (i+1))

print('5. 역삼각형 별해')
# 역삼각형 별해
for i in range(10, 0, -1) :
    print('*' * i)