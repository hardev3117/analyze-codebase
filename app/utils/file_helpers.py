import tiktoken

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