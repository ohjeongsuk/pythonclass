# 파이썬 리스트 == 자바 List<Object>

# 리스트(추가: append(), 삽입: insert(), 삭제: pop(), 수정: ~[index] = 값, 
#       검색: .index(), 카운트: .count(), 전체삭제: clear())


# subway = [10,20,30]
# subway.append(40)               #추가 [10, 20, 30, 40]
# subway.insert(1,100)            #삽입 [10, 100, 20, 30, 40]
# value = subway.pop()            #제거 [10, 100, 20, 30]
# subway[0] = 200                 #수정 [200, 100, 20, 30]
# indexValue = subway.index(100)  #검색  1
# subway.append(100)              #추가 [200, 100, 20, 30, 100]
# countValue = subway.count(100)  #카운트 2
# subway.clear()                  #전체삭제 [ ]
# print(subway)

# subway = ['감자','수박','참외']
# subway.append('오이')            #추가  ['감자', '수박', '참외', '오이']
# subway.insert(1,'옥수수')        #삽입  ['감자', '옥수수', '수박', '참외', '오이']
# value = subway.pop()            #제거  ['감자', '옥수수', '수박', '참외']
# subway[0] ='돼지감자'            #수정  ['돼지감자', '옥수수', '수박', '참외']
# indexValue = subway.index('옥수수')   #검색 1 
# subway.append('옥수수')          #추가 ['돼지감자', '옥수수', '수박', '참외', '옥수수']
# countValue = subway.count('옥수수')  #카운트 2
# # subway.clear()                  #전체삭제 [ ]
# print(countValue)


# 정렬: sort() 오름차순, sort(reverse=True) 내림차순, 역정렬: reverse()
# 리스트에서 값이 존재하는지확인(in)
# 원본에 정렬진행
# sum(리스트): 전체합계를 계산

subway = [90,10,20,30,40,60]
print( 60 in subway)
total = sum(subway)
print(total)
# subway.sort(reverse=True)
# subway.reverse()
# print(subway)


# 깊은복사진행을 해서 정렬: 복사리스트 = sorted(원본리스트)
# subway = [90,10,20,30,40,60]
# print(subway)
# newSub = sorted(subway)
# print(subway)
# print(newSub)

# 리스트 합집합
# mixList1 = [10,True,"호박",[1,2,3,4]]
# mixList2 = [30,False,'수박']
# print(mixList1)
# print(mixList2)

# mixList1.extend(mixList2)
# print(mixList1)