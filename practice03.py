# 문제3. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
# 또, 디렉토리 경로명과 파일명을 분리하여 출력하세요.

s = '/usr/local/bin/python'

split_str = s.split('/')
path1 = ', '.join(split_str)
print(path1[2:])

split_str = s.rsplit('/', 1)
path2 = ', '.join(split_str)
print(path2)