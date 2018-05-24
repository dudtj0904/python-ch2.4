# 문제1. 키보드로 정수 수치 입력 받아 3의 배수인지 판단


num = input('수를 입력하세요:')
if num.isalpha() :
    print('정수가 아닙니다.')
elif num.isdigit() :

    if int(num) % 3 == 0 :
        print('3의 배수 입니다.')
    else :
        print('3의 배수가 아닙니다.')
