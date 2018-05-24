# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

li = []
sum, avg = 0, 1
for i in range(5) :
    num = input('> ')
    li.append(num)
    sum += int(num)

print('평균: ', sum/len(li))
