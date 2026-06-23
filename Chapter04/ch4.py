# 문자열에서 자주사용하는방법: slicing [], find(), count(), replace()

# 문자열 """ ~~~ """, ''' ~~~ ''': 여백,또는 공백 기능까지 모두포함해서 문자열취급한다.
 
# msg = "파이썬을 공부하고 있습니다."
# print(msg, type(msg))

# msg2 = '''
# 파이썬을
# 공부
# 하고 있습니다.
# '''

# print(msg2, type(msg2))

# 슬라이싱 []

jumin = "990829-1550823"

# print("사용자 성별번호 :", jumin[7])
# print("사용자 연도 :", jumin[:2])
# print("사용자 월 :", jumin[2:4])
# print("사용자 일 :", jumin[4:6])
# print("사용자 생년월일 :", jumin[:6])
# print("주민번호뒷자리 :", jumin[7:])
# print("주민번호뒷자리 :", jumin[-7:])
# print("주민번호뒷자리 검증번호이전 :", jumin[7:-1])
# print("주민번호 문자열 길이 :", len(jumin))

# 반복문을 이용해서 주민번호 한자리씩을 출력하시오. '-' 생략하시오
# for i in range(0,len(jumin)):
#   if jumin[i] == "-":
#     continue
#   print(jumin[i], end=" ")  

# 문자열 처리함수

# msg = "Python is Amazing"

# print(msg.lower())  # python is amazing
# print(msg.upper())  # PYTHON IS AMAZING
# print(msg.isupper())  # false
# print(msg[0].isupper())  # true
# print(msg[1:3].islower())  # true
# # replace  *** 문자열에서 필요한 영역을 다른문자로 교체가 가능(자바에서 이런기능을 사용하려면 많은 메모리가 사용됨)
# print(msg.replace("Python","java")) 


# find, index 차이점을 체크
# find 진행에서 찾는것이 없으면 -1, 다음문장으로 실행한다.
# index 진행에서 찾는것이 없으면 ValueError 발생시키고, 다음문장으로 실행하지 않는다.
# index 개념보다는 find를 사용하는것이 좋다. 

msg = "Python is Amazing"
# findIndex = msg.find("n")
# print(findIndex)    # 5

# findIndex2 = msg.find("n",findIndex+1)
# print(findIndex2)   # 15

# findIndex3 = msg.find("is")
# print(findIndex3)   # 7

# findIndex4 = msg.find("kim") 
# print(findIndex4)     # -1
# print("hi")

# findIndex6 = msg.find("n", 6, -1)
# print(findIndex6)   

# msg = "Python is Amazing"
# findIndex = msg.index("n")
# print(findIndex)    # 5

# findIndex2 = msg.index("n",findIndex+1)
# print(findIndex2)   # 15

# findIndex3 = msg.index("is")
# print(findIndex3)   # 7

# findIndex5 = msg.index("n", 6, -1)
# print(findIndex5)   

# findIndex4 = msg.index("kim") # 찾기 못하면 ValueError 발생이되서 다음문장을 실행안함
# print(findIndex4)   # ValueError
# print("hi")


msg = "Python is Amazing"
# print(msg.count("n"))  #2
# print(msg.count("k"))  #0
# print(len(msg))  #17


# 문자열 포맷

# print("java"+"python")  #javapython
# print("java","python")  #java python

# age = 20
# print("나는 %d살입니다."%age)
# like = "파이썬"
# print("나는 %s을 좋아합니다."%like)
# grade = "A"
# print("java언어의 점수는 %c 등급입니다."%grade)
# score = 96.50
# print("java언어의 점수는 %.2f 등급입니다."%score)
# flag = True
# print("나는 java언어를 좋아하는것은 %s 입니다."%flag)
# fruit1 = "수박"
# fruit2 = "참외"
# print("나는 좋아하는 과일은 %s과 %s 입니다."%(fruit1,fruit2))


# age = 20
# print("나는 {}살입니다.".format(age))
# like = "파이썬"
# print("나는 {}을 좋아합니다.".format(like))
# grade = "A"
# print("java언어의 점수는 {} 등급입니다.".format(grade))
# score = 96.50
# print("java언어의 점수는 {} 등급입니다.".format(score))
# flag = True
# print("나는 java언어를 좋아하는것은 {} 입니다.".format(flag))
# fruit1 = "수박"
# fruit2 = "참외"
# print("나는 좋아하는 과일은 {}과 {} 입니다.".format(fruit1,fruit2))
# print("나는 좋아하는 과일은 {1}과 {0} 입니다.".format(fruit1,fruit2))


# age = 20
# print(f"나는 {age}살입니다.")
# like = "파이썬"
# print(f"나는 {like}을 좋아합니다.")
# grade = "A"
# print(f"java언어의 점수는 {grade} 등급입니다.")
# score = 96.50
# print(f"java언어의 점수는 {score} 등급입니다.")
# flag = True
# print(f"나는 java언어를 좋아하는것은 {flag} 입니다.")
# fruit1 = "수박"
# fruit2 = "참외"
# print(f"나는 좋아하는 과일은 {fruit1}과 {fruit2} 입니다.")
# print(f"나는 좋아하는 과일은 {fruit2}과 {fruit1} 입니다.")

# 탈출문자  \n  \t  \b  \r  \'  \"
print("파이썬\n자바")
print("파이썬\t자바")
print("파이썬\b자바")
print("파이썬\r자바")
print("파이썬보다 \"자바\"ㅇ")
print('파이썬보다 \'자바\'ㅇ')
print("D:\\javaTest\\nmetadata\\")


