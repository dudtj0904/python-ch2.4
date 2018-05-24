# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.

num = input('수를 입력하세요: ')
if num.isalpha() :
    print('문자 입력 X')
elif num.isdigit() :
    if int(num) % 2 == 0 :
        print('짝수')
    else :
        print('홀수')