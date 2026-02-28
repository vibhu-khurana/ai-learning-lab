from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"system", "content":"You are a Mathematics teacher. You need to assist the user related to Mathematics queries only"},
              {"role": "user", "content": "Can you explain me the sum of 2+2?"}], 
)

print(response.choices[0].message.content)