import unittest
import tempfile              # Required for creating temp directories
import shutil                # Required to delete temp directories
from pathlib import Path     # For file path creation
from app.core.code_parser import Parser

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        parser = Parser(base_path="dummy")  # base_path is not used in add()
        result = parser.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        parser = Parser(base_path="dummy")
        result = parser.add(-5, -2)
        self.assertEqual(result, -7)

    def test_add_zero(self):
        parser = Parser(base_path="dummy")
        result = parser.add(0, 0)
        self.assertEqual(result, 0)

    
    def setUp(self):
        # Step 1: Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

        # Step 2: Add .py, .java, and other test files
        self.py_file = Path(self.test_dir) / "sample.py"
        self.java_file = Path(self.test_dir) / "Example.java"
        self.txt_file = Path(self.test_dir) / "notes.txt"

        self.py_file.write_text("print('Hello from Python')", encoding='utf-8')
        self.java_file.write_text("public class Example {}", encoding='utf-8')
        self.txt_file.write_text("Just a text file", encoding='utf-8')

        # Step 3: Create Parser instance
        self.parser = Parser(base_path=self.test_dir)

    def tearDown(self):
        # Step 4: Clean up the temporary directory
        shutil.rmtree(self.test_dir)

    def test_get_code_files(self):
        code_files = self.parser.get_code_files()

        # Assert that only .py and .java files are returned
        self.assertIn(str(self.py_file), code_files)
        self.assertIn(str(self.java_file), code_files)
        self.assertNotIn(str(self.txt_file), code_files)

        # Check if the content matches
        self.assertEqual(code_files[str(self.py_file)], "print('Hello from Python')")
        self.assertEqual(code_files[str(self.java_file)], "public class Example {}")


    def test_get_unique_extensions(self):
        extensions = self.parser.get_unique_extensions()

        # Expected: .py (lowercase), .java, .txt
        # 'README' should be skipped (no extension), 'script.PY' → .py (converted to lowercase)
        expected_extensions = {".py", ".java", ".txt"}

        self.assertEqual(extensions, expected_extensions)


if __name__ == '__main__':
    unittest.main()
