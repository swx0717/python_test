import json
import os
import logging

def load_students(filepath="data/students.json"):
    try:
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                logging.warning(f"⚠️ 数据格式错误，使用空列表")
                return []
    except FileNotFoundError:
        logging.warning(f"📄 文件 {filepath} 不存在，使用空列表")
        return []
    except json.decoder.JSONDecodeError:
        logging.error(f"⚠️ JSON 文件损坏，使用空列表")
        return []

def save_students(students, filepath="data/students.json"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode="w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)



