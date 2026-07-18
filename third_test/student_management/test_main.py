import unittest
import os
import tempfile
import shutil
import json
from unittest.mock import patch

# 导入被测试模块
import student_service
from student_service import (
    get_all_students,
    add_student,
    find_student,
    update_score,
    delete_student,
    calculate_grade,
    max_grade,
    get_grade,
)
import validators


class TestValidators(unittest.TestCase):
    """测试校验函数"""

    def test_is_valid_name(self):
        self.assertTrue(validators.is_valid_name("张三"))
        self.assertTrue(validators.is_valid_name("John Doe"))
        self.assertFalse(validators.is_valid_name(""))      # 空字符串
        self.assertFalse(validators.is_valid_name("  "))    # 空格
        self.assertFalse(validators.is_valid_name("123"))   # 数字
        self.assertFalse(validators.is_valid_name("张-三")) # 特殊字符

    def test_is_valid_score(self):
        self.assertTrue(validators.is_valid_score("90"))
        self.assertTrue(validators.is_valid_score("75.5"))
        self.assertTrue(validators.is_valid_score("0"))
        self.assertTrue(validators.is_valid_score("100"))
        self.assertFalse(validators.is_valid_score("-1"))
        self.assertFalse(validators.is_valid_score("101"))
        self.assertFalse(validators.is_valid_score("abc"))


class TestStudentService(unittest.TestCase):
    """测试学生服务业务函数（使用模拟数据，不读写真实文件）"""

    def setUp(self):
        """每个测试前准备一个初始学生列表"""
        self.students = [
            {"name": "Alice", "score": 85.0},
            {"name": "Bob", "score": 72.5},
            {"name": "Charlie", "score": 45.0},
        ]
        # 使用 patch 避免 save_students 实际写文件（可选）
        # 但为了简单，我们只操作内存列表，不调用 save（测试时我们会自行控制）

    def test_add_student_success(self):
        success, msg = add_student(self.students, "David", "92")
        self.assertTrue(success)
        self.assertEqual(len(self.students), 4)
        self.assertEqual(self.students[-1]["name"], "David")
        self.assertEqual(self.students[-1]["score"], 92.0)

    def test_add_student_invalid_name(self):
        success, msg = add_student(self.students, "", "80")
        self.assertFalse(success)
        self.assertEqual(len(self.students), 3)  # 未添加

    def test_add_student_invalid_score(self):
        success, msg = add_student(self.students, "Eve", "150")
        self.assertFalse(success)
        self.assertEqual(len(self.students), 3)

    def test_find_student_found(self):
        success, result = find_student(self.students, "Bob")
        self.assertTrue(success)
        self.assertEqual(result["name"], "Bob")
        self.assertEqual(result["score"], 72.5)

    def test_find_student_not_found(self):
        success, result = find_student(self.students, "NotExist")
        self.assertFalse(success)
        self.assertEqual(result, "未找到学生 NotExist")

    def test_find_student_invalid_name(self):
        success, result = find_student(self.students, "  ")
        self.assertFalse(success)
        self.assertEqual(result, "姓名无效")

    def test_update_score_success(self):
        success, msg = update_score(self.students, "Alice", "95")
        self.assertTrue(success)
        self.assertEqual(self.students[0]["score"], 95.0)

    def test_update_score_not_found(self):
        success, msg = update_score(self.students, "Unknown", "90")
        self.assertFalse(success)
        self.assertEqual(msg, "未找到学生 Unknown")

    def test_update_score_invalid_score(self):
        success, msg = update_score(self.students, "Alice", "200")
        self.assertFalse(success)

    def test_delete_student_success(self):
        success, msg = delete_student(self.students, "Charlie")
        self.assertTrue(success)
        self.assertEqual(len(self.students), 2)
        names = [s["name"] for s in self.students]
        self.assertNotIn("Charlie", names)

    def test_delete_student_not_found(self):
        success, msg = delete_student(self.students, "Ghost")
        self.assertFalse(success)
        self.assertEqual(msg, "未找到学生 Ghost")

    def test_calculate_grade(self):
        success, avg = calculate_grade(self.students)
        self.assertTrue(success)
        self.assertAlmostEqual(avg, (85 + 72.5 + 45) / 3, places=2)

    def test_calculate_grade_empty(self):
        success, result = calculate_grade([])
        self.assertFalse(success)
        self.assertEqual(result, "无学生数据")

    def test_max_grade(self):
        success, result = max_grade(self.students)
        self.assertTrue(success)
        self.assertEqual(result, "最高成绩：85.0")

    def test_max_grade_empty(self):
        success, result = max_grade([])
        self.assertFalse(success)
        self.assertEqual(result, "无学生数据")

    def test_get_grade(self):
        self.assertEqual(get_grade(95), "A")
        self.assertEqual(get_grade(85), "B")
        self.assertEqual(get_grade(75), "C")
        self.assertEqual(get_grade(65), "D")
        self.assertEqual(get_grade(55), "F")


class TestStorageWithTempFile(unittest.TestCase):
    """测试存储模块（使用临时文件）"""

    def setUp(self):
        # 创建临时目录
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_students.json")
        # 将 storage 的默认路径指向测试文件（通过 monkey patch）
        self.original_load = student_service.load_students
        self.original_save = student_service.save_students
        # 重新绑定到测试路径
        import storage
        storage.load_students = lambda filepath=self.test_file: self._load(filepath)
        storage.save_students = lambda data, filepath=self.test_file: self._save(data, filepath)
        # 重新导入 student_service 使修改生效（简单方式：使用 patch）
        # 这里我们直接使用 patch 装饰器更简单，但为了清晰，我们使用 patch

    def _load(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _save(self, data, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def tearDown(self):
        # 清理临时目录
        shutil.rmtree(self.temp_dir)
        # 恢复原始函数（可选）
        import storage
        storage.load_students = self.original_load
        storage.save_students = self.original_save

    @patch('storage.load_students')
    @patch('storage.save_students')
    def test_save_and_load(self, mock_save, mock_load):
        # 模拟保存和加载
        test_data = [{"name": "Test", "score": 88}]
        # 让 load 返回模拟数据
        mock_load.return_value = test_data
        # 测试 get_all_students
        result = get_all_students()
        self.assertEqual(result, test_data)
        # 测试 save 被调用（在 add_student 中）
        mock_save.assert_not_called()
        # 实际调用 add_student 会触发保存
        # 但我们不在此测试中实际写文件，只验证逻辑


if __name__ == "__main__":
    unittest.main()