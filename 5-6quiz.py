# # Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle과 sample을 활용

# # shuffle, sample 활용
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))


# from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print("당첨자 발표")
# shuffle(lst)
# print("치킨당첨자", sample(lst, 1))

# shuffle(lst)
# print("커피 당첨자", sample(lst, 1))

# shuffle(lst)
# print(sample(lst, 1))


from random import *
users = range(1,21) # 1부터 20까지 숫자를 생성
# print(type(users))
users = list(users)
# print(type(users))
print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 뽑아서 1명은 치킨, 3명은커피

print("-- 당첨자 발표--")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("--축하합니다--")