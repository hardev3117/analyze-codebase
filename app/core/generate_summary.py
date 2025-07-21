from app.config.settings import SOURCES_DIR, CHUNK_SIZE, OUTPUT_JSON
from app.utils.file_helpers import  helper
import json

class GenerateSummary:
    def __init__(self,Extractor,Parser):
        self.extractor=Extractor
        self.parser =Parser        

    def generate_code_summary(self, chunk_size):
        file_extions= self.parser.get_unique_extensions()
        all_code = self.parser.get_code_files(file_extions)
        results = []   
        
        for file, content in all_code.items():
            chunks = helper.chunk_code(content, chunk_size)       
            for chunk in chunks:
                try:     
                    # analyse code chunk                      
                    json_str = self.extractor.analyze_code_chunk(file, chunk)     
                
                    # Ensure it's valid JSON: strip whitespace and check
                    cleaned_str = json_str.strip()                 
                    
                    data = json.loads(cleaned_str)
                    data["file"] = file
                    results.append(data)  
                
                except Exception as e:
                    print(f"Error in {file}: {e}")
        
        return results



if __name__ == "__main__":
    pass
    # source_dir=SOURCES_DIR
    # chunk_size=CHUNK_SIZE   
    # all_code = get_code_files(source_dir)  
    # generateSummary=GenerateSummary()
    # results = generateSummary.generate_code_summary(source_dir,chunk_size)
    # print(results) 
    # OUTPUT_JSON = "analysis_summary.json"
    # # Check if results list is not empty and doesn't contain only None
    # valid_results = [r for r in results if r is not None]

    # if valid_results:
    #     self.saveResult.save_to_json(valid_results, OUTPUT_JSON)
    #     print(f"Saved {len(valid_results)} results to {OUTPUT_JSON}")
    # else:
    #     print("No valid results to save.")