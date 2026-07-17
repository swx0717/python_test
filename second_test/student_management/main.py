from student_service import (
    get_all_students,
    add_student,
    update_score,
    delete_student,
    calc_average
)

def main():
    students = get_all_students()
    while True:
        print("\n--- 学生成绩管理系统 ---")
        print("1. 查看所有学生")
        print("2. 添加学生")
        print("3. 修改成绩")
        print("4. 删除学生")
        print("5. 计算平均分")
        print("6. 退出")
        choice = input("请选择：")
        if choice == "1":
            if not students:
                print("暂无学生数据。")
            else:
                for s in students:
                    print(f"{s['name']}: {s['score']}")
        elif choice == "2":
            name = input("姓名：")
            score = input("成绩：")
            success, msg = add_student(students, name, score)
            print(msg)
        elif choice == "3":
            name = input("要修改的学生姓名：")
            new_score = input("新成绩：")
            success, msg = update_score(students, name, new_score)
            print(msg)
        elif choice == "4":
            name = input("要删除的学生姓名：")
            success, msg = delete_student(students, name)
            print(msg)
        elif choice == "5":
            avg = calc_average(students)
            print(f"平均分：{avg:.2f}" if students else "暂无学生，平均分0")
        elif choice == "6":
            print("再见！")
            break
        else:
            print("无效选项")

if __name__ == "__main__":
    main()