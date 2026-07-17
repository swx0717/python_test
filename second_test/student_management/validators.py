def is_valid_name(name):
    """检查姓名是否非空且只包含字母和空格（示例）"""
    if not name or not name.strip():
        return False
    return all(c.isalpha() or c.isspace() for c in name)

def is_valid_score(score):
    """检查成绩是否在 0-100 之间且为数字"""
    try:
        s = float(score)
        return 0 <= s <= 100
    except ValueError:
        return False