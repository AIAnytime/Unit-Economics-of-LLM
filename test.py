import tiktoken 
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    print(num_tokens)
    return num_tokens

prompt_text = "GPT4 is the best"
token_counts = num_tokens_from_string(prompt_text, "cl100k_base")
print(token_counts)