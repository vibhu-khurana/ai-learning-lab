from dotenv import load_dotenv
import os
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from pinecone import Pinecone, ServerlessSpec


load_dotenv()

# ------------------------
# Environment Variables
# ------------------------
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_environment = os.getenv("PINECONE_ENVIRONMENT")  # e.g. us-east-1
pinecone_index = os.getenv("PINECONE_INDEX_NAME")

# ------------------------
# Initialize Pinecone
# ------------------------
print(f"Initializing Pinecone {pinecone_api_key} {pinecone_environment} {pinecone_index}")
pc = Pinecone(api_key=pinecone_api_key)

existing_indexes = [index.name for index in pc.list_indexes()]

if pinecone_index not in existing_indexes:
    pc.create_index(
        name=pinecone_index,
        dimension=3072,  # for text-embedding-3-large
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region=pinecone_environment,
        ),
    )

index = pc.Index(pinecone_index)

# ------------------------
# Load PDF
# ------------------------
pdf_path = Path(__file__).parent / "nodejs.pdf"
loader = PyPDFLoader(str(pdf_path))
docs = loader.load()

# ------------------------
# Split Documents
# ------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = text_splitter.split_documents(docs)

# ------------------------
# Embeddings
# ------------------------
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# ------------------------
# Create Vector Store
# ------------------------
vector_store = PineconeVectorStore(
    index=index,
    embedding=embedding_model,
)

# Add documents to index
vector_store.add_documents(chunks)

print("✅ Indexing completed successfully.")