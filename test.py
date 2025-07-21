from pathlib import Path
from collections import defaultdict

def get_unique_extensions(base_path):
    extensions = set()

    for file in Path(base_path).rglob("*"):
        if file.is_file():
            ext = file.suffix.lower()
            if ext:  # Skip files with no extension
                extensions.add(ext)

    return extensions


path="sakila-project"
print(get_unique_extensions(path))