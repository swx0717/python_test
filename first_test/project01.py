from operator import itemgetter

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

#添加学生
def add_student(students):
    name = input("输入学生名称:")
    score = float(input("输入成绩"))
    if name not in students:
        if score > 100 or score < 0:
            print("无效成绩")
            return
        else:
            students.update({name:score})
            print(f"学生{name}：成绩：{students[name]}，添加成功")
    else:
        print("已经存在")
        return
#查看全部学生
def show_students(students):
    if not students:
        print("暂无数据")
        return
    for name, score in students.items():
        print(f"{name}: {score} 分，等级：{get_grade(score)}")

#查询学生
def search_student(students):
    find_name = input("输入查询名称：").strip()
    for name,score in students.items():
        if name == find_name:
            print(f"{find_name},{get_grade(score)}")
            return
    print("未查询到该学生")
#修改成绩
def update_score(students):
    find_name = input("输入需要修改成绩的学生姓名：").strip()
    update_score = float(input("成绩修改为："))
    for name in students:
        if name == find_name:
            students[find_name] = update_score
            print(f"{find_name}:{students[find_name]}")

#删除学生
def delete_student(students):
    find_name = input("输入需要删除的学生姓名：")
    if find_name not in students:
        print("未找到该学生")
        return
    del students[find_name]
    print(f"学生 {find_name} 已删除")
#平均分
def calculate_average(students):
    average = 0
    scores =[]
    scores = students.values()
    sum_score = sum(scores)
    print(sum_score / len(scores))
#最高分学生
def show_top_student(students):
    max_score = max(students.values())
    for name,score in students.items():
        if score == max_score:
            print(name)
#不及格学生
def show_failed_students(students):
    name_failed = []
    for name,score in students.items():
        if score < 60:
            name_failed.append(name)
    print(name_failed)
#成绩排序
def sort_students(students):
    sorted_students = sorted(students.items(), key=itemgetter(1), reverse=True)
    print(sorted_students)



def main():
    students = {"张三": 85.5,
    "李四": 92.0,
    "王五": 78.0,
    "赵六": 59.5,
    "孙七": 100.0}
# 全局数据
    while True:
        print("\n===== 学生成绩管理系统 =====")
        print("1. 添加学生")
        print("2. 查看全部学生")
        print("3. 查询学生")
        print("4. 修改成绩")
        print("5. 删除学生")
        print("6. 显示平均分")
        print("7. 显示最高分学生")
        print("8. 显示不及格学生")
        print("9. 按成绩从高到低显示")
        print("0. 退出")
        choice = input("请选择操作（输入数字）：").strip()
        if choice == '0':
            print("感谢使用，再见！")
            break
        elif choice == '1':
            add_student(students)
        elif choice == '2':
            show_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_score(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            calculate_average(students)
        elif choice == '7':
            show_top_student(students)
        elif choice == '8':
            show_failed_students(students)
        elif choice == '9':
            sort_students(students)
        else:
            print("无效输入，请重新选择")

if __name__ == "__main__":
    main()