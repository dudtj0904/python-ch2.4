# 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전,
# 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.

money = input('금액: ')
if money.isalpha() :
    print('숫자로 입력해주세요.')
elif money.isdigit() :
    result = int(money)
    i = 50000
    b = True
    while i >= 1 :
        count = int(result / i)
        print('{0}원 : {1}개'.format(i, count))
        result = result - (i*count)
        if b :
            i = int(i/5)
            b = False
        else :
            i = int(i/2)
            b = True

