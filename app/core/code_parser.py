from pathlib import Path
import os
from collections import defaultdict

class Parser:
    def __init__(self, base_path):
        self.base_path=base_path


    def get_code_files(self, exts={".java", ".py"}):
        code_files = {}
        for ext in exts:
            for file in Path(self.base_path).rglob(f"*{ext}"):
                try:
                    code_files[str(file)] = file.read_text(encoding='utf-8', errors='ignore')
                except Exception as e:
                    print(f"Failed to read {file}: {e}")
        return code_files


    def get_unique_extensions(self):
        extensions = set()

        for file in Path(self.base_path).rglob("*"):
            if file.is_file():
                ext = file.suffix.lower()
                if ext:  # Skip files with no extension
                    extensions.add(ext)

        return extensions


    def add(self, a:int, b:int):
        return (a + b)