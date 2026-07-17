from storage import load_students, save_students
from validators import is_valid_name, is_valid_score

def get_all_students():
    """获取所有学生（加载）"""
    return load_students()

def add_student(students, name, score):
    """添加学生，返回 (成功标志, 消息)"""
    if not is_valid_name(name):
        return False, "姓名无效"
    if not is_valid_score(score):
        return False, "成绩无效（需为0-100的数字）"
    students.append({"name": name.strip(), "score": float(score)})
    save_students(students)
    return True, f"学生 {name} 添加成功"

def update_score(students, name, new_score):
    """修改成绩"""
    if not is_valid_name(name):
        return False, "姓名无效"
    if not is_valid_score(new_score):
        return False, "成绩无效"
    for s in students:
        if s["name"] == name.strip():
            s["score"] = float(new_score)
            save_students(students)
            return True, f"学生 {name} 成绩已更新"
    return False, f"未找到学生 {name}"

def delete_student(students, name):
    """删除学生"""
    if not is_valid_name(name):
        return False, "姓名无效"
    for i, s in enumerate(students):
        if s["name"] == name.strip():
            del students[i]
            save_students(students)
            return True, f"学生 {name} 已删除"
    return False, f"未找到学生 {name}"

def calc_average(students):
    """计算平均分，若列表为空返回0"""
    if not students:
        return 0
    total = sum(s["score"] for s in students)
    return total / len(students)