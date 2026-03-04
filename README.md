# AI Learning Lab

A hands-on experimentation repository for understanding Large Language Models (LLMs) and AI system internals.

## Topics Covered

- Tokenization using OpenAI tiktoken

## Project Structure

ai-learning-lab/
├── rag/
│   ├── index.py
│   ├── chat.py
│   ├── nodejs.pdf
│   ├── docker-compose.yml
│
├── tokenization/
│   └── tiktoken_basics.py
|
├── weather_agent/
│   └── main.py
│
├── .gitignore
└── README.md

## Setup Instructions

1. Create virtual environment:
   python3 -m venv venv

2. Activate:
   source venv/bin/activate

## Weather Agent

This agent demonstrates:
- Tool calling
- JSON structured output
- Multi-step reasoning (START → PLAN → TOOL → OUTPUT)
- External API integration
- Controlled system command execution

## RAG Implementation

This module demonstrates:

- PDF ingestion using PyPDFLoader
- Recursive text chunking
- OpenAI embedding generation
- Qdrant vector database integration
- Retrieval-based answering

### To Run

1. Start Qdrant:
   docker-compose up -d

2. Index documents:
   python rag/index.py

3. Run chat:
   python rag/chat.py