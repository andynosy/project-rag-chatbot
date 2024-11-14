from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..services.llm import LLMService
from ..models.vector_store import Document
from ..services.embedding import EmbeddingService
from typing import List
import numpy as np
from sqlalchemy import text

router = APIRouter()

@router.post("/query")
async def query(
    query: str,
    model_name: str,
    db: Session = Depends(get_db)
):
    try:
        # Create embedding for the query
        embedding_service = EmbeddingService()
        query_embedding = embedding_service.create_embedding(query)

        # Find similar documents
        similar_docs_query = text("""
            SELECT content, url, title
            FROM documents
            ORDER BY embedding <-> :embedding
            LIMIT 3
        """)
        
        similar_docs = db.execute(
            similar_docs_query,
            {"embedding": query_embedding}
        ).fetchall()

        if not similar_docs:
            raise HTTPException(status_code=404, content="No relevant documents found")

        # Prepare context from similar documents
        context = "\n\n".join([f"From {doc.title} ({doc.url}):\n{doc.content}" 
                             for doc in similar_docs])

        # Generate response using LLM
        llm_service = LLMService(model_name)
        response = llm_service.generate_response(query, context)

        return {
            "answer": response,
            "sources": [{"title": doc.title, "url": doc.url} 
                       for doc in similar_docs]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))