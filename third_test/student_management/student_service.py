from storage import load_students, save_students
from validators import is_valid_name, is_valid_score
import logging

def get_all_students():
    """获取所有学生（加载）"""
    return load_students()

def add_student(students, name, score):
    if not is_valid_name(name):
        logging.warning(f"尝试添加无效姓名：{name}")
        return False, "姓名无效"
    if not is_valid_score(score):
        logging.warning(f"尝试添加无效成绩：{score}")
        return False,"成绩无效"
    students.append({"name": name.strip(), "score": float(score)})
    save_students(students)
    return True, f"学生 {name} 添加成功"

def find_student(students, name):
    if not is_valid_name(name):
        logging.warning(f"尝试添加无效姓名：{name}")
        return False, "姓名无效"
    for student in students:
        if student["name"] == name.strip():
            return True,student
    return False,"未找到"

def update_score(students, name, new_score):
    if not is_valid_name(name):
        logging.warning(f"尝试修改无效姓名：{name}")
        return False, "姓名无效"
    if not is_valid_score(new_score):
        logging.warning(f"尝试修改无效成绩：{new_score}")
        return False,"成绩无效"
    for student in students:
        if student["name"] == name.strip():
            student["score"] = float(new_score)
            save_students(students)
            return True,f"成绩修改成功"
    return False,"未找到该学生"

def delete_student(students, name):
    if not is_valid_name(name):
        logging.warning(f"尝试删除无效姓名：{name}")
        return False, "姓名无效"
    for i, s in enumerate(students):
        if s["name"] == name.strip():
            del students[i]
            save_students(students)
            return True,f"学生{name}删除成功"
    return False,f"未找到学生{name}"

def calculate_grade(students):
    if not students:
        return False,"无学生数据6"
    total = sum(s["score"] for s in students)
    return True, total / len(students)

def max_grade(students):
    if not students:
        return False,"无学生数据"
    max_grade = max(s["score"] for s in students)
    return True,f"最高成绩：{max_grade}"

def get_failed_students(students):
    if not students:
        return True, []   # 或返回 (False, "无学生")
    failed = [s for s in students if s["score"] < 60]
    return True, failed

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

