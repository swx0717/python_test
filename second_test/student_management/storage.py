import json
import os

def load_students(filepath="data/students.json"):
    """从JSON文件加载学生列表，若文件不存在或损坏返回空列表"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print(f"⚠️ 数据格式错误，使用空列表")
                return []
    except FileNotFoundError:
        print(f"📄 文件 {filepath} 不存在，使用空列表")
        return []
    except json.JSONDecodeError:
        print(f"⚠️ JSON 文件损坏，使用空列表")
        return []

def save_students(students, filepath="data/students.json"):
    """保存学生列表到JSON文件"""
    # 确保 data 目录存在
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)