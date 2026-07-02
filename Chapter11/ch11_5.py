# 외장함수
#  glob == window dir기능
import glob
import os
# print(glob.glob("chapter11\*.py"))

# print(os.getcwd())

# 현재 디렉토리에서 디렉토리를 생성하고, 삭제를 진행할 수 있다
# if os.path.exists("sample_text") :
#   print("sample_text 존재합니다")
#   os.rmdir("sample_text")
# else:
#   print("sample_text 찾을수가 없습니다.")
#   os.mkdir("sample_text")

# 현재 작업하는 폴더안의 리스트를 볼 수 있는지 점검
# print(os.listdir())

# 외장 함수 time
import time

# print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# 외장함수 datetime
import datetime
print("오늘의 날짜는",datetime.date.today())
today = datetime.date.today()
# 현재 날짜에서 100일이 지난 날짜
td = datetime.timedelta(days=100)
print(today + td)
