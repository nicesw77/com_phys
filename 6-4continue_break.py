# 출석번호별로 부르면서 책을 읽게 하기 결석한 학생은 넘어감
absent = [2, 5] # 결석
no_book = [7] # 책을 안가져옴
for student in range (1, 11): # 1부터 10번까지
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))