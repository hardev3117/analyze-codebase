import tiktoken
from langchain.text_splitter import TokenTextSplitter

class helper:
    @staticmethod
    def chunk_code(code_text, max_tokens=2000):
        enc = tiktoken.get_encoding("cl100k_base")
        tokens = enc.encode(code_text)
        chunks = []
        while tokens:
            chunk = tokens[:max_tokens]
            tokens = tokens[max_tokens:]
            chunks.append(enc.decode(chunk))
        return chunks
    
    
    @staticmethod
    def token_chunk_code(code_text, max_tokens=2000, chunk_overlap=200):
        splitter = TokenTextSplitter(
            encoding_name="cl100k_base",  # same tokenizer
            chunk_size=max_tokens,
            chunk_overlap=chunk_overlap
        )
        chunks = splitter.split_text(code_text)
        return chunks