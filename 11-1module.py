# import theater_module
# theater_module.price(3) # 3 명이 영화 보러 갔을 때 가격
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# #price_soldier(7)

from theater_module import price_soldier as price # 군인 가격을 "price"로 별명지정
price(5)