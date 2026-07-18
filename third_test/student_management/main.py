import logging
from student_service import (
    get_all_students,
    add_student,
    find_student,
    update_score,
    delete_student,
    calculate_grade,
    max_grade,
    get_grade,
    # negative_students 有严重 bug，暂不引入
)

# 配置日志（输出到控制台）
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def print_menu():
    """显示菜单"""
    print("\n" + "=" * 40)
    print("        学生成绩管理系统")
    print("=" * 40)
    print("1. 查看所有学生")
    print("2. 添加学生")
    print("3. 查找学生")
    print("4. 修改成绩")
    print("5. 删除学生")
    print("6. 计算平均分")
    print("7. 显示最高分")
    print("8. 成绩等级查询（输入分数）")
    print("0. 退出")
    print("=" * 40)


def main():
    students = get_all_students()  # 加载已有数据
    while True:
        print_menu()
        choice = input("请输入操作编号: ").strip()
        if choice == "0":
            print("感谢使用，再见！")
            break

        elif choice == "1":
            if not students:
                print("暂无学生数据。")
            else:
                print("\n所有学生信息：")
                for idx, s in enumerate(students, 1):
                    print(f"{idx}. 姓名：{s['name']}，成绩：{s['score']}")

        elif choice == "2":
            name = input("请输入姓名: ").strip()
            score = input("请输入成绩（0-100）: ").strip()
            success, msg = add_student(students, name, score)
            print(msg)
            if success:
                # 重新加载最新数据（因为 add_student 内部已保存，students 引用已更新）
                pass

        elif choice == "3":
            name = input("请输入要查找的姓名: ").strip()
            success, result = find_student(students, name)   # 注意：此处去掉多余的 score 参数
            if success:
                print(f"找到学生：{result['name']}，成绩：{result['score']}")
            else:
                print(result)  # 错误信息

        elif choice == "4":
            name = input("请输入要修改的学生姓名: ").strip()
            new_score = input("请输入新成绩（0-100）: ").strip()
            success, msg = update_score(students, name, new_score)
            print(msg)

        elif choice == "5":
            name = input("请输入要删除的学生姓名: ").strip()
            success, msg = delete_student(students, name)   # 去掉多余的 score
            print(msg)

        elif choice == "6":
            success, avg = calculate_grade(students)
            if success:
                print(f"全班平均分：{avg:.2f}")
            else:
                print(avg)  # 错误信息

        elif choice == "7":
            success, result = max_grade(students)
            if success:
                print(result)
            else:
                print(result)  # 可能返回 "无学生数据"

        elif choice == "8":
            score_str = input("请输入分数: ").strip()
            try:
                score = float(score_str)
                grade = get_grade(score)
                print(f"分数 {score} 对应的等级是：{grade}")
            except ValueError:
                print("请输入有效的数字。")

        else:
            print("无效的选项，请重新输入。")


if __name__ == "__main__":
    main()