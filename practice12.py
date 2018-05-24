# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요

for i in range(1,100) :
    s = str(i)
    length = len(s)
    count = 0
    for j in range(0, length) :
        if int(s[j]) != 0 and int(s[j]) % 3 == 0 :
            count += 1
    if count != 0 :
        print(s, '짝'*count)


