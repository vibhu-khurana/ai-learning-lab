# AI Learning Lab

A hands-on experimentation repository for understanding Large Language Models (LLMs) and AI system internals.

## Topics Covered

- Tokenization using OpenAI tiktoken

## Project Structure

ai-learning-lab/
├── chatbot/
│   ├── chatbot_backend.py
│   ├── chatbot_backend_intermediate.py
│   ├── chatbot_frontend.py
├── rag/
│   ├── index.py
│   ├── chat.py
│   ├── nodejs.pdf
│   ├── docker-compose.yml
│
├── tokenization/
│   └── tiktoken_basics.py
├── UI_sme_assistant/
│   ├── lambda_function.py
│   ├── sample_test_event.json
│   ├── streamlit_app.py
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

## To Run

1. Start Qdrant:
   docker-compose up -d

2. Index documents:
   python rag/index.py

3. Run chat:
   python rag/chat.py


## 🧠 GenAI Equipment SME Assistant (Production Architecture)

Overview

This project demonstrates a production-style GenAI system that enables equipment Subject Matter Experts (SMEs) to interact with an AI assistant powered by Amazon Bedrock foundation models.

The system follows a serverless architecture using AWS managed services to provide scalability, security, and observability.

## Flow

1️⃣ User Prompt
The Equipment SME submits a query from the frontend interface.

2️⃣ API Layer – AWS API Gateway
API Gateway receives the request and securely forwards it to a Lambda function.

3️⃣ Compute Layer – AWS Lambda
The Lambda function:

Processes the request

Injects a system prompt

Invokes an Amazon Bedrock foundation model

4️⃣ GenAI Layer – Amazon Bedrock
The Lambda invokes a foundation model such as:

Claude

Amazon Nova

Gemini

The model generates a response based on the system prompt and user query.

5️⃣ Observability – CloudWatch + SNS

Monitoring is implemented using:

Amazon CloudWatch Logs – captures application logs

CloudWatch Metrics – tracks invocation metrics

CloudWatch Alarms – detects anomalies

Amazon SNS – sends alert notifications

## AI Learning Lab – Bedrock Chatbot with LangChain

This project demonstrates how to build a conversational AI chatbot using AWS Bedrock, LangChain, and Streamlit. The chatbot maintains conversation context using memory and interacts with Amazon Bedrock foundation models to generate responses.

The goal of this repository is to experiment with LLM integrations, conversational memory, and AI application architecture.

## Flow Explanation

User Input

User enters a question in the Streamlit interface.

Conversation History Retrieval

LangChain memory retrieves previous conversation history.

Prompt Construction

The prompt is built using:

Current user query

Past messages from memory

LLM Invocation

The prompt is sent to Amazon Bedrock foundation model.

Response Processing

The output from the model is parsed.

UI Response

Streamlit displays the response to the user.

The conversation history is stored using LangChain ConversationSummaryBufferMemory which ensures context-aware responses.