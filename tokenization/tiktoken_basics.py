import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o-mini")

text = "Hi AI learners"

tokens = enc.encode(text)

print(f"Intial text {text}")
print(f"tokens are {tokens}")
print(f"Length of tokens {len(tokens)}")

decoded_text = enc.decode(tokens)
print(f"decoded text are {decoded_text}")
