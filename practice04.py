# 문제4. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>
"""
temp = True
for str in s :
    if str == '<' :
        temp = False
    elif str == '>' :
        temp = True
        continue

    if temp :
        print(str, end='')
else :
    pass


