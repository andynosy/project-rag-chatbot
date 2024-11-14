from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..services.confluence import ConfluenceService
from ..services.embedding import EmbeddingService
from ..models.vector_store import Document

router = APIRouter()

@router.post("/sync/{space_key}")
async def sync_confluence_space(
    space_key: str,
    db: Session = Depends(get_db)
):
    try:
        # Get content from Confluence
        confluence_service = ConfluenceService()
        content = confluence_service.get_space_content(space_key)

        # Create embeddings and store in database
        embedding_service = EmbeddingService()
        
        for page in content:
            # Create embedding for the page content
            embedding = embedding_service.create_embedding(page['content'])

            # Check if document already exists
            existing_doc = db.query(Document).filter(
                Document.url == page['url']
            ).first()

            if existing_doc:
                # Update existing document
                existing_doc.content = page['content']
                existing_doc.embedding = embedding
                existing_doc.title = page['title']
                existing_doc.last_updated = page['last_updated']
            else:
                # Create new document
                doc = Document(
                    content=page['content'],
                    embedding=embedding,
                    url=page['url'],
                    title=page['title'],
                    last_updated=page['last_updated'],
                    space_key=space_key
                )
                db.add(doc)

        db.commit()
        return {"message": f"Successfully synced {len(content)} pages"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))