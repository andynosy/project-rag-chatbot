from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from ..core.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    embedding = Column(ARRAY(Float))
    url = Column(String)
    title = Column(String)
    last_updated = Column(DateTime)
    space_key = Column(String)