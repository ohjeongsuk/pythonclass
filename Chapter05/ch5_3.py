# 튜플

# menu = ("돈까스","생선까스","우동")
# print(menu, type(menu))   # ('돈까스', '생선까스', '우동') <class 'tuple'>
# print(menu[0])            # '돈까스'  
# print(menu[1])            # '생선까스'
# print(menu[2])            # '우동'
# # menu[3] = '피자'      # 추가불가
# # menu[2] = '짜장면'    # 수정불가  

# # 추가하는 방법 튜플 + ()
# menu = menu + ("김치나베",)
# print(menu)


# 튜플을 변수에 저장하는 방법
(name, age, hobby) = ["홍길동", 10, "코딩"]
(name1, age1, hobby1) = ("홍길동", 11, "코딩")
print(name, age, hobby)
print(name1, age1, hobby1)