from app.models.base import Base
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Track(Base):
    __tablename__ = "tracks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    spotify_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False) 
    preview_url = Column(String, nullable=True) 
    spotify_url = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, server_default="now()") 
