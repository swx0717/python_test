def get_score():
    score = int(input("输入成绩："))
    return score

def get_grade(score):
    if 90 <= score <= 100:
        return '优秀'
    elif 80 <= score < 90:
        return '良好'
    elif 60 <= score < 80:
        return '及格'
    elif 0 <= score <60:
        return '不及格'
    else:
        return '无效成绩'

def print_grade(grade):
    print({grade})

def main():
    score = get_score()
    grade = get_grade(score)
    print_grade(grade)

if __name__ == "__main__":
    main()
