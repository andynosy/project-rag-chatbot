# RAG Chatbot with Confluence Integration

This project implements a RAG (Retrieval-Augmented Generation) chatbot that uses Confluence as its knowledge base. It features vector search capabilities using pgvector and supports multiple LLM providers (OpenAI and Anthropic).

## Features

- Confluence space synchronization using Personal Access Token (PAT)
- Vector search using pgvector
- Support for multiple LLM providers (OpenAI, Anthropic)
- Real-time chat interface
- Source attribution for answers
- Docker containerization

## Prerequisites

- Docker and Docker Compose
- Confluence Personal Access Token (PAT)
- OpenAI API key (for GPT-3.5/4)
- Anthropic API key (for Claude)

## Setup

1. Clone the repository
2. Create a `.env` file in the backend directory with the following variables:

```env
CONFLUENCE_URL=your_confluence_url
CONFLUENCE_PAT=your_personal_access_token
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
DATABASE_URL=postgresql://postgres:postgres@db:5432/ragbot
```

3. Start the application:

```bash
docker-compose up --build
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## Usage

1. Open the web interface
2. Enter your Confluence space key and click "Sync" to import content
3. Select your preferred LLM model
4. Start chatting with your knowledge base

## Architecture

- Frontend: React + TypeScript + Tailwind CSS
- Backend: FastAPI + SQLAlchemy + pgvector
- Database: PostgreSQL with pgvector extension
- LLM Integration: Langchain
- Containerization: Docker + Docker Compose

## Development

To run the application in development mode:

1. Start the database:
```bash
docker-compose up db
```

2. Start the backend:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

3. Start the frontend:
```bash
cd frontend
npm install
npm run dev
```