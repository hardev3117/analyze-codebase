
from app.config.settings import SOURCES_DIR, CHUNK_SIZE, OUTPUT_JSON
from app.core.generate_summary import GenerateSummary
from app.core.code_parser import Parser
from app.core.llm_extractor import Extractor 
from app.core.save_results import SaveResult 


source_dir=SOURCES_DIR
chunk_size=CHUNK_SIZE
output_json=OUTPUT_JSON

extractor=Extractor()
parser=Parser(source_dir)
saveResult=SaveResult(output_json)

generateSummary=GenerateSummary(extractor,parser)
results = generateSummary.generate_code_summary(chunk_size)


# Check if results list is not empty and doesn't contain only None
valid_results = [r for r in results if r is not None]

if valid_results:
    saveResult.save_to_json(valid_results)
    print(f"Saved {len(valid_results)} results to {output_json}")
else:
    print("No valid results to save.")





