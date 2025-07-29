from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from app.config.settings import MODEL_NAME
from dotenv import load_dotenv
load_dotenv()

class Extractor:
    def __init__(self):
        pass

    def analyze_code_chunk(self,file, chunk):
        TEMPLATE = """
        You are a senior developer. Extract structured knowledge from this code and return STRICT, VALID JSON.
        Add required information summary, complexity,methods, notes
        DO NOT include trailing commas,.

        Filename: {file_name}

        {code_chunk}

        Return JSON:
        {{  // Use double curly braces to escape
          "file": "{file_name}",
          "summary": "...",
          "methods": [
            {{"name": "...", "signature": "...", "description": "..."}}
          ],
          "complexity": "...",
          "notes": "..."
        }}
        """

        llm = ChatOpenAI(model=MODEL_NAME, temperature=0)
        #llm = Ollama(model=MODEL_NAME, temperature=0)  # or any local model you've installed

        prompt = PromptTemplate.from_template(TEMPLATE)
        #chain = LLMChain(prompt=prompt, llm=llm)
        #chain = prompt | llm
        # Modern chaining
        chain = prompt | llm

        # Invoke with input
        response = chain.invoke({"file_name": file, "code_chunk": chunk})
        output_text =response.content
        #print(output_text)
        #result = chain.invoke({"file_name": file, "code_chunk": chunk})
        #output_text = result['text']  # Extract text from dict
        #return output_text.replace("```json", "").replace("```", "")
        return output_text