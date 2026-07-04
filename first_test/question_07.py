def calculate_average(scores):
    if len(scores) == 0:
        print("无成绩输入")
    else:
        print(f"平均分：{sum(scores)/len(scores)}")

def count_passed(scores):
    passed_score =[]
    for score in scores:
        if score >= 60:
            passed_score.append(score)
    print(f"及格人数：{len(passed_score)}")

def display_results(scores):
    display_scores = []
    for score in scores:
        if score < 60:
            display_scores.append(score)
    print(f"不及格人数：{len(display_scores)}")

def main():
    scores = []
    while True:
        numbers = float(input("输入成绩(输入-1结束)："))
        if 0 <= numbers <=100:
            if numbers != -1:
                scores.append(numbers)
        elif numbers == -1:
            print("输入结束")
            break
        else:
            print("输入成绩无效")
    if not scores:
        print("无成绩输入")
    else:
        print(len(scores))
        calculate_average(scores)
        print(max(scores))
        print(min(scores))
        count_passed(scores)
        display_results(scores)

if __name__ == "__main__":
    main()