# 내부 package에서 가져오는 방법

# travel 패키지속에 thailand 모듈을 가져옴
# import 안에 해당되는 클래스나 함수는 가져오면 안됨
import travel.thailand

thailand_obj = travel.thailand.ThailandModule()
thailand_obj.detail_travel()

# from travel.thailand import ThailandModule

# thailand_obj = ThailandModule()
# thailand_obj.detail_travel()

# from travel.vietnam import VietnamModule

# viemtnam_obj = VietnamModule()
# viemtnam_obj.detail_travel()

# 해당되는 패키지에 모두 모듈을 가져오는 방법
# from travel import *

# t_obj = thailand.ThailandModule()
# t_obj.detail_travel()

# v_obj = vietnam.VietnamModule()
# v_obj.detail_travel()

# 패키지 모듈위치
# import inspect
# import random

# # inspect를 사용해서 randam 패키지위치 검사
# print(inspect.getfile(random))

# import inspect
# from travel import *
# # print(inspect.getfile(thailand))

# t_obj2 = thailand.ThailandModule()
# t_obj2.detail_travel()

# v_obj2 = vietnam.VietnamModule()
# v_obj2.detail_travel()