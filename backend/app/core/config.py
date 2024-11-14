from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    CONFLUENCE_URL: str
    CONFLUENCE_PAT: str  # Changed from USERNAME/API_TOKEN to PAT
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()