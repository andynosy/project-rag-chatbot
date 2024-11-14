from langchain.embeddings import OpenAIEmbeddings
from ..core.config import settings
import numpy as np

class EmbeddingService:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=settings.OPENAI_API_KEY
        )

    def create_embedding(self, text: str) -> list[float]:
        try:
            embedding = self.embeddings.embed_query(text)
            return embedding
        except Exception as e:
            raise Exception(f"Error creating embedding: {str(e)}")