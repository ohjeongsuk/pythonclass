# 내장함수 https://docs.python.org/ko/3.14/library/functions.html

# dir: 어떤 객체를 넘겼을때 해당된 객체의 멤버변수, 멤버함수를 볼 수 있다.
print(dir())
print("-"*100)
import random
print(dir())
print("-"*100)

list = [1,2,3,4]
print(dir(list))
print("-"*100)

name = "홍길동"
print(dir(name))