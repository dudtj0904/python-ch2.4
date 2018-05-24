# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요
# a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
# - 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )
# b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
# - 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )

input_num = input('숫자를 입력하세요: ')
if input_num.isalpha() :
    print('문자 XX')
elif input_num.isdigit() :
    num = int(input_num)
    sum = 0
    if num % 2 == 0 :
        for i in range(0, num+1, 2) :
           sum += i
    else :
        for i in range(1, num+1, 2) :
            sum += i

print('결과 값: ', sum)