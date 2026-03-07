#1. Import OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, Bedrock-LLM
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.indexes import VectorstoreIndexCreator
from langchain_aws import ChatBedrock
from pathlib import Path

 
#5c. Wrap within a function
def hr_index():
    #2. Define the data source and load data with PDFLoader(https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf)
    
    data_load=PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')
    #pdf_path = Path(__file__).parent / "Nagarro_Canada_Employee_Handbook_2025.pdf"
    #pdf_path = Path(__file__).parent / "nodejs.pdf"
    #data_load = PyPDFLoader(str(pdf_path))

    # Load the documents
    docs = data_load.load()

    # Remove Table of Contents pages
    docs = [d for d in docs if "........" not in d.page_content]
    #data_load=PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')  
 
    #3. Split the Text based on Character, Tokens etc. - Recursively split by character - ["\n\n", "\n", " ", ""]
    #data_split=RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=1000,chunk_overlap=100)
    data_split=RecursiveCharacterTextSplitter(chunk_size=600,chunk_overlap=200)

    chunks = data_split.split_documents(docs)
    #4. Create Embeddings -- Client connection
    data_embeddings=BedrockEmbeddings(
    credentials_profile_name= 'default',
    model_id="amazon.titan-embed-text-v2:0")
    #5à Create Vector DB, Store Embeddings and Index for Search - VectorstoreIndexCreator
    data_index=VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding=data_embeddings,
        vectorstore_cls=FAISS)
    #5b  Create index for HR Policy Document
    db_index=data_index.from_loaders([data_load])
    print('db_index',db_index)
    return db_index
#6a. Write a function to connect to Bedrock Foundation Model - Claude Foundation Model
def hr_llm():
    llm=ChatBedrock(
        credentials_profile_name='default',
        model_id="anthropic.claude-3-haiku-20240307-v1:0",
        model_kwargs={
        "max_tokens":1000,
        "temperature": 0.2,
        "top_p": 0.9})
    return llm
#6b. Write a function which searches the user prompt, searches the best match from Vector DB and sends both to LLM.
def hr_rag_response(index,question):
    rag_llm = hr_llm()

    # Step 1: get retriever from FAISS
    retriever = index.vectorstore.as_retriever(search_kwargs={"k":10,
        "fetch_k":30})

    # Step 2: retrieve relevant chunks
    docs = retriever.invoke(question)

    print("\n------ Retrieved Chunks ------\n")
    for i, d in enumerate(docs):
        print(f"\nChunk {i+1}:\n")
        print(d.page_content[:500])
        print("\n------------------\n")

    # Step 3: build context
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question based only on the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    response = rag_llm.invoke(prompt)

    return response.content