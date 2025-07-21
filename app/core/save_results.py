import json

class SaveResult:
    def __init__(self, output_path):
        self.output_path=output_path

    def save_to_json(self, results):
        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)