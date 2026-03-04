from dotenv import load_dotenv
import os

from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from openai import OpenAI


load_dotenv()

# ------------------------
# Environment Variables
# ------------------------
pinecone_index = os.getenv("PINECONE_INDEX_NAME")

# ------------------------
# OpenAI Client
# ------------------------
openai_client = OpenAI()

# ------------------------
# Embeddings
# ------------------------
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# ------------------------
# Connect to Existing Pinecone Index
# ------------------------
vector_db = PineconeVectorStore.from_existing_index(
    index_name=pinecone_index,
    embedding=embedding_model,
)

# ------------------------
# User Input
# ------------------------
user_query = input("Ask something: ")

# ------------------------
# Retrieve Relevant Documents
# ------------------------
search_results = vector_db.similarity_search(user_query, k=3)

context = "\n\n".join(
    [
        f"Page Content: {doc.page_content}\n"
        f"Page Number: {doc.metadata.get('page_label')}\n"
        f"Source: {doc.metadata.get('source')}"
        for doc in search_results
    ]
)

# ------------------------
# Prompt
# ------------------------
SYSTEM_PROMPT = f"""
You are a helpful AI assistant.

Answer strictly using the provided context.

IMPORTANT:
- Always include the page number and source in your final answer.
- Format the answer like:

Answer: <your explanation>

Source: <source>
Page Number: <page number>

Context:
{context}
"""

# ------------------------
# Generate Answer
# ------------------------
response = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ],
)

print("\n🤖 Answer:\n")
print(response.choices[0].message.content)