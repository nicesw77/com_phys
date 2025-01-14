# Quiz) 표준 체중을 구하는 프로그램

# * 표준체중: 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자: 키(m) x 키(m) x 22
# 여자: 키(m) x 키(m) x 21

def std_weight(height, gender): # 키는 m 단위 (실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 165 # cm 단위
gender = "남자"
weight = round(std_weight (height / 100, gender), 2)
print ("키 {0}cm {1}의 표준체중은 {2}kg 입니다.". format (height, gender, weight))